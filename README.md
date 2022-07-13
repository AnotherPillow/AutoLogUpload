# AutoLogUpload
A tool to automatically upload SMAPI logs when it crashes.
## Requirements
* [SMAPI](https://www.smapi.io/)
* [Python 3.8+](https://www.python.org/downloads/)
* psutil (`pip install psutil`)	
* urllib3 (`pip install urllib3`)
* requests (`pip install requests`)
* time (`pip install time`)
* subprocess (`pip install subprocess`)
* json (`pip install json`)
## Installation
Install the dependencies and unzip latest release/update into your game folder.

**ALWAYS DELETE LAST VERSION BEFORE INSTALLING A NEW VERSION**
## Usage
  - Run AutoLogUpload.bat in your game folder.
  - It will automatically upload the log file when the game closes and ask you to open in browser if you wish.
## Compiling
  - Run `py release.py`
## Configuration
  - `src/config.json` contains the configuration for the tool.
## Mac/Linux Support
Will come soon, shouldn't be hard to implement.