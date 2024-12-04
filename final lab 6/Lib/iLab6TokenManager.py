
# Lab6
#ITokenManager Interface: This interface manages the token and communication between processes. 
# Name: Jatin K rai
#DawID

from collections import deque

import Pyro5.api
from collections import defaultdict
from abc import ABC, abstractmethod

@Pyro5.api.expose
# Create a interface ILab6TokenManager
class iLab6TokenManager(ABC):
    @Pyro5.api.expose
    @abstractmethod
    def requestEntry(self, processId, sequenceNumber):
        pass

    @Pyro5.api.expose
    @abstractmethod
    def releaseToken(self, processId, sequenceNumber):
        pass
    
