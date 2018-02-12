# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()
        
        vcurr = util.Counter()
        for i in xrange(self.iterations):
            vcurr = self.values.copy()
            for state in self.mdp.getStates():
                all_actions = self.mdp.getPossibleActions(state)
                transitions = []
                value_list = []
                if self.mdp.isTerminal(state):
                    self.values[state] = 0
                else:
                    for action in all_actions:
                        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
                        value = 0
                        for transition in transitions:
                            value += transition[1] * (self.mdp.getReward(state, action, transition[0]) + self.discount * vcurr[transition[0]])
                        value_list.append(value)
                    self.values[state] = max(value_list)
                    
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]
    
    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        value = 0
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        for transition in transitions:
            value += transition[1]*(self.mdp.getReward(state, action, transition[0]) + self.discount * self.values[transition[0]])
        return value
    
    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.
        """
        if self.mdp.isTerminal(state):
            return None
        else:
            bestval = -99999999999
            bestaction = 0
            all_actions = self.mdp.getPossibleActions(state)
            for action in all_actions:
                transitions = self.mdp.getTransitionStatesAndProbs(state, action)
                value = 0
                for transition in transitions:
                    value += transition[1]*(self.mdp.getReward(state, action, transition[0]) + self.discount * self.values[transition[0]])
                if value > bestval:
                    bestaction = action
                    bestval = value
            return bestaction
        
    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
