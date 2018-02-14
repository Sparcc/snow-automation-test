from toms-driver import *

class CustomEnvironment(Environment):
    def buildEnvironmentAttributes(self):
        self.usrName = config['DEFAULT']['usrName']
        self.usrPass = config['DEFAULT']['usrPass']
        self.portalURL = config['DEFAULT']['portalURL']
        self.ITIL_URL = config['DEFAULT']['ITIL_URL']
        
class CustomCommandActionSystem(CommandActionSystem):
    def buildPrefabArgs(self):
        self.prefabArgs = {'UTAS' : [self.config['DEFAULT']['usrName'],
                                    self.config['DEFAULT']['usrPass']
                                    ]
                    
                    }
    
    def buildPrefabActions(self):
        self.prefabActions = {'LoginUTAS' : 'login UTAS'
                    }