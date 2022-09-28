import os
import zipfile
import shutil

print("Building release...")
os.system("cargo build --release")
print("Building done.")

# Get the current version
with open("version.txt", "r") as f:
    version = f.read().strip()
    print("Current version: " + version)

# Create the release directory
os.makedirs("Release/" + version, exist_ok=True)
print("Created release directory")

# Copy the files
shutil.copyfile("target/debug/autologupload_rs.exe", "Release/" + version + "/autologupload_rs.exe")
print("Copied .EXE file")
shutil.copyfile("target/debug/autologupload_rs.pdb", "Release/" + version + "/autologupload_rs.pdb")
print("Copied .PDB file")
shutil.copyfile("Release/autologupload.config.json", "Release/" + version + "/autologupload.config.json")
print("Copied config file")

# Zip the files
with zipfile.ZipFile(f"Release/{version}/{version}.zip", "w") as zip:
    zip.write("Release/" + version + "/autologupload_rs.exe", "autologupload_rs.exe")
    zip.write("Release/" + version + "/autologupload_rs.pdb", "autologupload_rs.pdb")
    zip.write("Release/" + version + "/autologupload.config.json", "autologupload.config.json")
    print("Zipped files")
print("Done")