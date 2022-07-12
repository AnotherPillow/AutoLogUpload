import requests
import urllib.parse
import os
def main():
    appdata = os.environ.get("APPDATA")
    log_path = os.path.join(appdata, "StardewValley/ErrorLogs/SMAPI-latest.txt")
    #read the contents of log_path
    with open(log_path, "r") as f:
        log_content = f.read()
    log = urllib.parse.quote(log_content)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    r = requests.post('https://smapi.io/log/', data="input={0}".format(log), headers=headers)
    return r.text.split('</strong> <code>')[1].split('</code>')[0]