
# Lab6
#TokenManager Implementation: This class implements the TokenManager interface. It maintains: 
# An identifier for the process currently holding the token (initially unassigned). 
# A queue for holding received REQUEST messages with process ID and sequence number. 
# It implements methods from the interface: 

# Name: Jatin K rai
#DawID

from collections import deque
import Pyro5.api
from Lib.iLab6TokenManager import iLab6TokenManager


@Pyro5.api.expose
class myLab6TokenManager(iLab6TokenManager):
    # assign
    def __init__(self):
        self.tokenholderprocessid = 0
        self.queueotoholdrequest = deque()
        self.GrantMessage = "GRANT"
        self.ReleaseMessage = "RELEASE"
        self.returnMessage = "Empty"

# requestEntry(processId, sequenceNumber): 
# Updates the queue with the received request. 
# Checks if the requesting process has the highest combined priority based on Suzuki
# Kasami's rules (considering both process ID and sequence number). 
# If the request is allowed, sets the holder and sends a GRANT message to the requesting 
# process using RMI. 

    @Pyro5.api.expose
    def requestEntry(self, processId, sequenceNumber):
        try:

            print(f"myLab6TokenManager: requestEntry(): Critical Section request Entry for Process : {processId} Started.")
            processIdandSequenceNumber = str(processId) + (":") + str (sequenceNumber)
            maximumsequencenumber = 0;
            priorityprocessid = ""
            prioritysequencenumber = 0

            if (processIdandSequenceNumber in self.queueotoholdrequest):

                #check for maximum sequence number and give to prirotiy,
                for processIdandSequenceNumber in  self.queueotoholdrequest:
                #check 
                    myproccessid = processIdandSequenceNumber.split(":")[0]
                    mysequencenumber= processIdandSequenceNumber.split(":")[1]

                    if (eval(mysequencenumber) > maximumsequencenumber):
                        priorityprocessid = myproccessid
                        prioritysequencenumber = mysequencenumber
                        maximumsequencenumber = mysequencenumber
                if ((processId == priorityprocessid) and (sequenceNumber == prioritysequencenumber)):   
                        self.returnMessage = self.GrantMessage
                        self.tokenholderprocessid = priorityprocessid
            else:
                self.queueotoholdrequest.append(processIdandSequenceNumber)
                self.tokenholderprocessid = processId
                self.returnMessage = self.GrantMessage
            print(f"myLab6TokenManager: requestEntry(): Critical Section request Entry for Process : {processId} Completed.")
           
        except Exception as error:
            print("requestEntry(): failed.")
            print(error)
        finally:
            print("requestEntry(): completed successfully.")
            
        return self.returnMessage
         
	
# releaseToken(processId, sequenceNumber): 
# Removes the process from the request queue if present. 
# If the queue is not empty, selects the next eligible process based on Suzuki-Kasami's 
# rules and sends a RELEASE message to current process and Grant message to the next elgible process..

    @Pyro5.api.expose
    def releaseToken(self, processId, sequenceNumber):
        try:
            print(f"myLab6TokenManager: releaseToken(): Critical Section request Entry for Process : {processId} Started.")
            processIdandSequenceNumber = str(processId) + (":") + str (sequenceNumber)
            if (processIdandSequenceNumber in  self.queueotoholdrequest):
               #check and remode
               self.queueotoholdrequest.remove(processIdandSequenceNumber)
            #next process
            if (len(self.queueotoholdrequest) > 0):
                processIdandSequenceNumber = self.queueotoholdrequest[0]
                myproccessid = processIdandSequenceNumber.split(":")[0]
                mysequenceid = processIdandSequenceNumber.split(":")[1]
                #request entry to next process id.
                self.requestEntry (myproccessid, mysequenceid)
            else:
                self.returnMessage = "Release"
        except Exception as error:
            print("releaseToken(): failed.")
            print(error)
        finally:
            print("releaseToken(): completed successfully.")

        print(f"myLab6TokenManager: releaseToken(): Critical Section request Entry for Process : {processId} Completed.")
        return self.returnMessage
    
"""
    #Test code for Token Manager
    testmyLab6TokenManager = myLab6TokenManager()
    print(testmyLab6TokenManager.requestEntry("P", 1))
    print(testmyLab6TokenManager.requestEntry("P", 2))
    print(testmyLab6TokenManager.releaseToken("P", 1))
"""

