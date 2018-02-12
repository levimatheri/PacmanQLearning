from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *
import random,util,math

class QLearningAgent(ReinforcementAgent):
    
    def __init__(self, **args):
        ReinforcementAgent.__init__(self, **args) # super
        self.q_values = util.Counter()
    
    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        return self.q_values[(state, action)]
    
    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  If
          there are no legal actions, which is the case at the
          terminal state, return a value of 0.0.
        """
        q_vals = []
        for action in self.getLegalActions(state):
            q_vals.append(self.getQValue(state, action))
        if len(self.getLegalAction(state)) == 0:
            return 0.0
        else:
            return max(q_vals)
        
    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  If there
          are no legal actions, which is the case at the terminal state,
          return None.
        """
        max_action = None
        max_q_val = 0
        for action in self.getLegalActions(state):
            q_val = self.getQValue(state, action)
            if q_val > max_q_val or max_action is None:
                max_q_val = q_val
                max_action = action
        return max_action
    
    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, take a random action and
          take the best policy action otherwise.  If there are
          no legal actions, which is the case at the terminal state,
          choose None as the action.
        """
        # pick action
        legalActions = self.getLegalActions(state)
        if util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)
        
    def update(self, state, action, nextState, reward):
        first_part = (1 - self.alpha) * self.getQValue(state, action)
        if len(self.getLegalActions(nextState)) == 0:
            sample = reward
        else:
            sample = reward + (self.discount * max([self.getQValue(nextState, next_action) for next_action in self.getLegalActions(nextState)]))
        second_part = self.alpha * sample
        self.q_values[(state, action)] = first_part + second_part
        
    def getPolicy(self, state):
        return self.computeActionFromQValues(state)
    
    def getValue(self, state):
        return self.computeValueFromQValues(state)
    
class PacmanQAgent(QLearningAgent):
    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)
        
    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action
    
class ApproximateQAgent(PacmanQAgent):
    
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()
        self.weight = 0
        
    def getWeights(self):
        return self.weights
    
    def getQValue(self, state, action):
        """
          Return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        q_value = 0
        features = self.featExtractor.getFeatures(state, action)
        counter = 0
        for feature in features:
            q_value += features[feature] * self.weights[feature]
            counter += 1
            
        return q_value
    
    def update(self, state, action, nextState, reward):
        features = self.featExtractor.getFeatures(state, action)
        features_list = features.sortedKeys()
        counter = 0
        for feature in features:
            difference = 0
            if len(self.getLegalActions(nextState)) == 0:
                difference = reward - self.getQValue(state, action)
            else:
                difference = (reward + self.discount * max([self.getQValue(nextState, nextAction) for nextAction in self.getLegalActions(nextState)])) - self.getQValue(state, action)
            self.weights[feature] = self.weights[feature] + self.alpha * difference * features[feature]
            counter += 1
            
    def final(self, state):
        # call the super-class final method
        PacmanQAgent.final(self, state) 
        
        # finished training?
        if self.episodesSoFar == self.numTraining:
            # print weights
            print(self.weights)