# Lab6
# Process client: As ac client to call methods for processes to interact with the mutual exclusion logic. 
# Name: Jatin K rai
#DawID

from Lib.clsLab6Process import myiLab6Process
from Lib.URLHelper import URLHelper
from pathlib import Path
import os

def Start_suzukikasamiProcessClient():
    try:
        MyProcessName = "P2"
        currentworkingdir = os.getcwd()
        """
            data_folder = Path("source_data/text_files/")
            file_to_open = data_folder / "raw_data.txt"
            print(file_to_open.read_text())
        """
        #read url from file
        URLPath = currentworkingdir + "\\ServerOutput\\UrlfileforTimeServer.txt"
        URLFileObj = URLHelper(URLPath)
        uri = URLFileObj.readserverURLFile()

        if ((uri is None) or (len(uri) < 1)):
            uri = input("Enter the UnicastRemoteObject for Time Server URI: ")

        print (f"URI of the TimeServer is : {uri}")    

        remote_process = myiLab6Process(uri,  MyProcessName)
        
    except Exception as error:
            print("Pyro5.api.Proxy(): Suzuki Kasami Pyro5.api.Proxy failed while calling")
            print (error)
    finally:
            print("Pyro5.api.Proxy(): Suzuki Kasami Pyro5.api.Proxy completed successfully while calling.")

    try:    

        try:
            CSValue = remote_process.requestCriticalSection()
            print("remote_process.requestCriticalSection(): Critical Section:", CSValue)
        except Exception as error:
            print("remote_process.requestCriticalSection():  failed.")
            print (error)
        finally:
            print("remote_process.requestCriticalSection(): completed successfully.")
        
        try:
            CSValue = remote_process.releaseCriticalSection()
            print("remote_process.releaseCriticalSection(): Critical Section:", CSValue)
        except Exception as error:
            print("remote_process.releaseCriticalSection():  failed.")
            print (error)
        finally:
            print("remote_process.releaseCriticalSection(): completed successfully.")
        
  
        """
            while True:
                print("1. Request Critical Section")
                print("2. Relase Critical Section")
                print("3. Get Sequence Number")
                print("4. Close")
                choice = input("Choose an option: ")

                if choice == '1':
                    try:
                        CSValue = remote_process.requestCriticalSection()
                    except Exception as error:
                        print("remote_process.requestCriticalSection():  failed.")
                        print (error)
                    finally:
                        print("remote_process.requestCriticalSection(): completed successfully.")
                    
                    print("remote_process.requestCriticalSection(): Critical Section:", CSValue)

                elif choice == '2':
                    try:
                        CSValue = remote_process.releaseCriticalSection()
                    except Exception as error:
                        print("remote_process.releaseCriticalSection():  failed.")
                        print (error)
                    finally:
                        print("remote_process.releaseCriticalSection(): completed successfully.")
                    
                    print("remote_process.releaseCriticalSection(): Critical Section:", CSValue)

                elif choice == '3':
                    try:
                        CSValue = remote_process.getSequenceNumber()
                    except Exception as error:
                        print("remote_process.getSequenceNumber():  failed.")
                        print (error)
                    finally:
                        print("remote_process.getSequenceNumber(): completed successfully.")
                    
                    print("remote_process.getSequenceNumber(): Sequence Number:", CSValue)

                elif choice == '4':
                    print ("Thanks for the closing application")
                    break
            """
    except Exception as error:
            print("remote_process.requestCriticalSection() process failed.")
            print (error)
    finally:
                print("remote_process.requestCriticalSection() completed successfully.")

if __name__ == "__main__":
    Start_suzukikasamiProcessClient()
