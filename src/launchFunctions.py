from subprocess import Popen

### LAUNCH FUNCTIONS ###
def launchKeyboard(no_total=None, layout=None):
    attr_list = ['python', 'pacman.py', '-p', 'KeyboardAgent']

    if layout is not None:
        attr_list.extend(['-l', str(layout)])
    if no_total is not None:
        attr_list.extend(['-n', str(no_total)])
    Popen(attr_list, shell=True).communicate()

def launchApproxQLearning(no_total=None, no_training=None, layout=None):
    if no_training >= no_total:
        raise ValueError("Value of training must be less than total number of games to play!")
   
    attr_list = ['python', 'pacman.py', '-p', 'ApproximateQAgent', '-a', 'extractor=SimpleExtractor']

    if no_total is not None and no_training is not None:
        attr_list.extend(['-x', str(no_training), '-n', str(no_total)])
    if layout is not None:
        attr_list.extend(['-l', str(layout)])
    Popen(attr_list, shell=True).communicate()

def launchQLearning(no_total=None, no_training=None, layout=None, watch=None):
    if no_training >= no_total:
        raise ValueError("Value of training must be less than total number of games to play!")

    attr_list = ['python', 'pacman.py', '-p', 'PacmanQAgent']

    if no_total is not None and no_training is not None:
        attr_list.extend(['-x', str(no_training), '-n', str(no_total)])
    if layout is not None:
        attr_list.extend(['-l', str(layout)])
    if str(watch) == 'Yes':
        train_attr = 'numTraining=' + str(int(no_total) - int(no_training))
        attr_list = ['python', 'pacman.py', '-p', 'PacmanQAgent', '-n', str(no_training), '-l', str(layout), '-a', train_attr]
    Popen(attr_list, shell=True).communicate()

# def launchQLearningWatch(no_training, layout=None):
#     train_attr = 'numTraining=' + no_training

#     attr_list = ['python', 'pacman.py', '-p', 'PacmanQAgent', '-n', str(no_training), no_training, '-l', str(layout), train_attr]
#     Popen(attr_list, shell=True).communicate()