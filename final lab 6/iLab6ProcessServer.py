
# Lab6
# Process client: As ac server to call methods for processes to interact with the mutual exclusion logic.
# Name: Jatin K rai
#DawID
import Pyro5.api
from Lib.clsLab6TokenManager import myLab6TokenManager
from Lib.URLHelper import URLHelper
from pathlib import Path
import os

def Start_Lab6SuzukiKasami_srv():
    #Act as Server.
    try:
        #make it server ready for remote process.
        daemon = Pyro5.api.Daemon()
    except Exception as error:
        print("rPyro5.api.Daemo(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo(): completed successfully.")

    try:
        #make it server ready for remote process.
        uri = daemon.register(myLab6TokenManager)
    except Exception as error:
        print("Pyro5.api.Daemo.register(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.register() : completed successfully.")

    try:
        currentworkingdir = os.getcwd()
        """
            data_folder = Path("source_data/text_files/")
            file_to_open = data_folder / "raw_data.txt"
            print(file_to_open.read_text())
        """

        URLPath = currentworkingdir + "\\ServerOutput\\UrlfileforTimeServer.txt"
        URLFileObj = URLHelper(URLPath)
        URLFileObj.writeServerURLFile(str(uri))


        #make it server ready for remote process.
        print("UnicastRemoteObject for Suzuki-Kasami=")
        print("Ready. UnicastRemoteObject URI=", uri)
        daemon.requestLoop()
    except Exception as error:
        print("Pyro5.api.Daemo.requestLoop(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.requestLoop() : completed successfully.")

if __name__ == "__main__":
    Start_Lab6SuzukiKasami_srv()
