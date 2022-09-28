# AutoLogUpload
A tool to automatically upload SMAPI logs upon crashing.

## Installation
- Unzip the latest release, can go anywhere.
- Open the `autologupload.config.json` file and edit the `game_path` value to point to your SMAPI install
- If you wish, change your Steam launch options to point to the `autologupload_rs.exe` file instead SMAPI.
  
## Compiling
- Install Rust
- Run `cargo build --release`