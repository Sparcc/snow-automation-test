import sys, os
sys.path.append(os.getcwd())
from toms-driver-extensions import *

#main
#env = Environment()
env = CustomEnvironment()

driverManager = DriverManagement(env, True)#set env

#utilise command system
com = CustomCommandActionSystem(driverManager, False)#debug off
com.acceptInput()