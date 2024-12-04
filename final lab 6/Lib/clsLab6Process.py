
# Lab6
#iLab6Process This class implements the iLab6Process interface. 
#This class implements the Process interface. It maintains: 
#• A local sequence number (integer value). 
#• A boolean flag indicating critical section access status. 
#• A reference to a shared TokenManager object (explained later). 
#• It implements methods from the interface: 

# Name: Jatin K rai
#DawID
import random
import Pyro5.api
import sys
import threading
from datetime import datetime
from time import sleep
from Lib.iLab6Process import iLab6Process


@Pyro5.api.expose
class myiLab6Process(iLab6Process):
    # assign static
    SequenceNumber = 0

    #Constuctor
    def __init__(self, remoteuri,  MyProcessName):
        self.criticalsectionstatus = False
        self.TokenManager = Pyro5.api.Proxy(remoteuri)
        self.ProcessNumber = MyProcessName # "P" # let us assume process
        self.SequenceNumber = 0
        self.TokenManagerMessage = ""
        self.cs_lock = threading.Lock()
        self.in_cs = 0
        self.has_token = 0


    #requestCriticalSection(): Increments the local sequence number, sends a REQUEST message 
    # with the current sequence number to all processes using RMI. 
    @Pyro5.api.expose
    def  requestCriticalSection(self):
        try:
           myiLab6Process.SequenceNumber += 1
           print(f"requestCriticalSection(): Critical Section send request for Process : {self.ProcessNumber} Started.")
           self.TokenManagerMessage = self.send_request ("Request", self.ProcessNumber, myiLab6Process.SequenceNumber)
           print(f"requestCriticalSection(): Critical Section send request for Process : {self.ProcessNumber} Finished.")

           if (self.TokenManagerMessage.lower() == "grant"):
                self.has_token = 1
                print(f"requestCriticalSection(): Critical Section Enter request for Process : {self.ProcessNumber} Started.")
                self.EnterCriticalSection()
                print(f"requestCriticalSection(): Critical Section Finished request for Process : {self.ProcessNumber} Completed.")
                #stay for proces
                
        except Exception as error:
            print("requestCriticalSection(): Critical Section request failed.")
            print (error)
        finally:
            print("requestCriticalSection(): Critical Section request completed successfully.")
        return self.TokenManagerMessage


    #releaseCriticalSection(): Sets the critical section flag to false, sends a RELEASE message with its 
    #sequence number to the TokenManager using RMI. 
    @Pyro5.api.expose
    def releaseCriticalSection(self):
        try:
            self.criticalsectionstatus = False
            print(f"releaseCriticalSection(): Critical Section send release for Process : {self.ProcessNumber} Started.")
            self.ReleaseTokenMessage = self.send_release("Release", self.ProcessNumber, myiLab6Process.SequenceNumber)
            print(f"releaseCriticalSection(): Critical Section send release for Process : {self.ProcessNumber} Completed.")
            if (self.ReleaseTokenMessage.lower() == "release"):
                self.has_token = 0
                print(f"releaseCriticalSection(): Critical Section Exit request for Process : {self.ProcessNumber} Started.")
                self.ExitCriticalSection()
                print(f"releaseCriticalSection(): Critical Section Exit request for Process : {self.ProcessNumber} Completed.")
        except Exception as error:
            print("releaseCriticalSection(): Critical Section release failed.")
            print (error)
        finally:
            print("releaseCriticalSection(): Critical Section release completed successfully.")
        
        return self.ReleaseTokenMessage

   #getSequenceNumber(): Returns the current local sequence number
    @Pyro5.api.expose
    def getSequenceNumber(self):
        try: 
           pidsequencenumber = myiLab6Process.SequenceNumber
        except Exception as error:
            print("getSequenceNumber(): Sequence Number gets failed.")
            print (error)
        finally:
            print("getSequenceNumber(): Sequence Number gets completed successfully.")
        return pidsequencenumber
	#Supporting method	
    #send_request : send request to all process
    def send_request (self, Requestmsg, processId, sequencenumber):
        try:
           #send request.
            if(len(Requestmsg) > 1):
                Reuestmsg = "Request"
            print(f"send_request(): RMI requestEntry from Token Manager  for Process : {self.ProcessNumber} Started.")
            self.TokenManagerMessage =  self.TokenManager.requestEntry(processId, sequencenumber)
            print(f"send_request(): RMI requestEntry from Token Manager  for Process : {self.ProcessNumber} Completed.")
        except Exception as error:
            print("send_request(): send request failed.")
            print (error)
        finally:
            print("send_request(): send request  completed successfully.")
        return  self.TokenManagerMessage
    
    #Supporting method
    #send_release : send release from process
    def send_release (self, Requestmsg, processId, sequencenumber):
        try:
           #receive request.
            if(len(Requestmsg) > 1):
                Reuestmsg = "Release"
            #for processId in self.ProcessNumber:
            print(f"send_release(): RMI release Entry from Token Manager  for Process : {self.ProcessNumber} Started.")
            self.TokenManagerMessage =  self.TokenManager.releaseToken(processId, sequencenumber)
            print(f"send_release(): RMI release Entry from Token Manager  for Process : {self.ProcessNumber} Completed.")
        except Exception as error:
            print("send_release(): send release failed.")
            print (error)
        finally:
            print("send_release(): send release  completed successfully.")
        return  self.TokenManagerMessage
    
    #Supporting method
    def EnterCriticalSection(self):
        try:
            with self.cs_lock:
                if self.has_token == 1:
                    in_cs = 1
                    print("%s: I am proccesid %s and sequence number %d doing in CS." % (datetime.now().strftime('%M:%S'), 
                                                                                         self.ProcessNumber, myiLab6Process.SequenceNumber))
                    sys.stdout.flush()
                    sleep(random.uniform(2, 5))
                    self.releaseTokenMessage = self.releaseCriticalSection()

        except Exception as error:
            print("EnterCriticalSection(): failed.")
            print (error)
        finally:
            print("EnterCriticalSection(): send completed successfully.")
        return self.releaseTokenMessage;

    #Supporting method 
    def ExitCriticalSection(self):
        try:

            if self.has_token == 0:
                self.in_cs = 0
                print("%s: I am proceesid %s and sequence number %d finished doing in CS." % (datetime.now().strftime('%M:%S'), 
                                                                                              self.ProcessNumber, myiLab6Process.SequenceNumber))
                sys.stdout.flush()

        except Exception as error:
            print("ExitCriticalSection():failed.")
            print (error)
        finally:
            print("ExitCriticalSection(): completed successfully.")
        return
"""        
    #Test code for Process
    testmyiLab6Process = myiLab6Process()
    print(testmyiLab6Process.requestCriticalSection())
"""