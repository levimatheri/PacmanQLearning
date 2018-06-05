from subprocess import Popen

### LAUNCH FUNCTIONS ###
def launchKeyboard():
    Popen(['python', 'pacman.py', '-p', 'KeyboardAgent'], shell=True).communicate()

def launchApproxQLearning(no_total=None, no_training=None, layout=None):
    attr_list = ['python', 'pacman.py', '-p', 'ApproximateQAgent', '-a', 'extractor=SimpleExtractor']

    if no_total is not None and no_training is not None:
        attr_list.extend(['-x', str(no_training), '-n', str(no_total)])
    if layout is not None:
        attr_list.extend(['-l', str(layout)])
    Popen(attr_list, shell=True).communicate()

def launchQLearning(no_total=None, no_training=None, layout=None, watch=None):
    attr_list = ['python', 'pacman.py', '-p', 'PacmanQAgent']

    if no_total is not None and no_training is not None:
        attr_list.extend(['-x', str(no_training), '-n', str(no_total)])
    if layout is not None:
        attr_list.extend(['-l', str(layout)])
    Popen(attr_list, shell=True).communicate()

def launchQLearningWatch(no_training, layout=None):
    train_attr = 'numTraining=' + no_training

    attr_list = ['python', 'pacman.py', '-p', 'PacmanQAgent', '-n', str(no_training), train_attr, '-l', str(layout)]
    Popen(attr_list, shell=True).communicate()