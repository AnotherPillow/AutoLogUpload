import os
from upload import main as upload_log
import psutil
import subprocess
import json
import time

#use the json module to parse config.json
with open("config.json") as f:
    config = json.load(f)

#smapi_path = "C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\StardewModdingAPI.exe"
smapi_path = os.getcwd().replace("\\src", "") + "\\StardewModdingAPI.exe"
#smapi = os.popen(smapi_path)

#os.popen(smapi_path, "r")
#os.startfile("smapi.bat")
#os.popen("smapi.bat", "r")
sm = subprocess.Popen(smapi_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
#os.startfile(smapi_path)

while True:
    time.sleep(1)
    if "StardewModdingAPI.exe" not in (i.name() for i in psutil.process_iter()):
        print("SMAPI closed, uploading log...")
        log = upload_log()
        print("Your log, {0}: ".format(config["title"]) + log)
        print("Would you like to open that in your browser? (y/n)")
        answer = input()
        if answer.startswith("y"):
            os.startfile(log)
        elif answer.startswith("n"):
            print("Okay, exiting...")
        else:
            print("Not a valid answer, assuming no, exiting...")
        break