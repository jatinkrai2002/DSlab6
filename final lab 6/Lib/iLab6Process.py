
# Lab6
# Process Interface: This interface defines methods for processes to interact with the mutual exclusion logic. 
# Name: Jatin K rai
#DawID

import Pyro5.api
from abc import ABC, abstractmethod

# Create a interface iVectorClock
@Pyro5.api.expose
class iLab6Process(ABC):
    @Pyro5.api.expose
    @abstractmethod
    def requestCriticalSection(self):
        pass
    	
    @abstractmethod
    @Pyro5.api.expose
    def releaseCriticalSection(self):
        pass

    @abstractmethod
    @Pyro5.api.expose
    def getSequenceNumber(self):
        pass
		