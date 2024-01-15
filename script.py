import os
import socket
from datetime import datetime
import shutil
import tkinter as tk
from tkinter import filedialog

deviceName = socket.gethostname()
date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

try:
    scriptPath = os.path.dirname(__file__)
    configs = open(scriptPath + "\config.txt", "r")
except Exception as e:
    print("Failed to open config.txt")
    print(e)
    raise SystemExit

configs = configs.readlines()

mcDir = configs[0][0:-1]
backupDir = configs[1][0:-1]
backupSaves = configs[2][0:-1]
backupMods = configs[3][0:-1]
backupSchems = configs[4][0:-1]
backupScreenshots = configs[5][0:-1]
backupLogs = configs[6][0:-1]
backupResourcePacks = configs[7][0:-1]
deleteOldBackups = configs[8][0:-1]
showGUI = configs[9][0:-1]

hasBackedUp = False
hasDeleted = False

# ensure destination directory exists, create if not
if os.path.exists(backupDir + "minecraft-backups" + "\\" + deviceName) is not True:
    if os.path.exists(backupDir + "minecraft-backups") is not True:
        os.mkdir(backupDir + "minecraft-backups")

    os.mkdir(backupDir + "minecraft-backups" + "\\" + deviceName)

backupDir = backupDir + "minecraft-backups" + "\\" + deviceName + "\\"

# Backup saves, skip if false
if backupSaves == "True":
    # skip if saves folder doesn't exist
    # implicitly means there are no saves to backup
    if os.path.exists(mcDir + "saves"):
        try:
            shutil.copytree(mcDir + "saves", backupDir + "saves" + "\\" + date)
        except Exception as e:
            print("Failed to backup saves")
            print(e)
        else:
            print("Successfully backed up saves")
            hasBackedUp = True

# Backup mods, skip if false
if backupMods == "True":
    # skip if mods folder doesn't exist
    # implicitly means there are no mods to backup
    if os.path.exists(mcDir + "mods"):
        try:
            shutil.copytree(mcDir + "mods", backupDir + "mods" + "\\" + date)
        except Exception as e:
            print("Failed to backup mods")
            print(e)
        else:
            print("Successfully backed up mods")
            hasBackedUp = True

# Backup schematics, skip if false
if backupSchems == "True":
    # skip if schematics folder doesn't exist
    # implicitly means there are no schematics to backup
    if os.path.exists(mcDir + "config\\worldedit\\schematics"):
        try:
            shutil.copytree(mcDir + "config\\worldedit\\schematics",
                            backupDir + "schematics" + "\\" + date)
        except Exception as e:
            print("Failed to backup schematics")
            print(e)
        else:
            print("Successfully backed up schematics")
            hasBackedUp = True

# Backup screenshots, skip if false
if backupScreenshots == "True":
    # skip if screenshots folder doesn't exist
    # implicitly means there are no screenshots to backup
    if os.path.exists(mcDir + "screenshots"):
        try:
            shutil.copytree(mcDir + "screenshots", backupDir +
                            "screenshots" + "\\" + date)
        except Exception as e:
            print("Failed to backup screenshots")
            print(e)
        else:
            print("Successfully backed up screenshots")
            hasBackedUp = True

# Backup logs, skip if false
if backupLogs == "True":
    # skip if logs folder doesn't exist
    # implicitly means there are no logs to backup
    if os.path.exists(mcDir + "logs"):
        try:
            shutil.copytree(mcDir + "logs", backupDir + "logs" + "\\" + date)
        except Exception as e:
            print("Failed to backup logs")
            print(e)
        else:
            print("Successfully backed up logs")
            hasBackedUp = True

# Backup resource packs, skip if false
if backupResourcePacks == "True":
    # skip if resource packs folder doesn't exist
    # implicitly means there are no resource packs to backup
    if os.path.exists(mcDir + "resourcepacks"):
        try:
            shutil.copytree(mcDir + "resourcepacks",
                            backupDir + "resourcepacks" + "\\" + date)
        except Exception as e:
            print("Failed to backup resource packs")
            print(e)
        else:
            print("Successfully backed up resource packs")
            hasBackedUp = True

# if no backups were made, do not print that backup is complete
if hasBackedUp:
    print("Backup complete")

# Delete old backups, skip if false
# Deletes all subfolders of logs, mods, resourcepacks, saves, schematics, screenshots that are older than 14 days
if deleteOldBackups == "True":
    for folder in os.listdir(backupDir):
        if os.path.isdir(backupDir + folder):
            for subfolder in os.listdir(backupDir + folder):
                if os.path.isdir(backupDir + folder + "\\" + subfolder):
                    if (datetime.now() - datetime.strptime(subfolder, "%Y-%m-%d_%H-%M-%S")).days > 14:
                        try:
                            shutil.rmtree(backupDir + folder +
                                          "\\" + subfolder)
                        except Exception as e:
                            print("Failed to delete " + folder +
                                  " backups older than 14 days")
                            print(e)
                        else:
                            print("Successfully deleted " + folder +
                                  " backups older than 14 days")
                            hasDeleted = True

    # if no backups were deleted, do not print that all backups older than 14 days were deleted
    if hasDeleted:
        print("All backups older than 14 days deleted")

# display GUI if selected
if showGUI == "True":
    root = tk.Tk()
    root.withdraw()

    if hasBackedUp:
        if hasDeleted:
            tk.messagebox.showinfo(
                "Success", "Minecraft backup complete\nAll Minecraft backups older than 14 days deleted")
        else:
            tk.messagebox.showinfo(
                "Success", "Minecraft backup complete\nNo Minecraft backups older than 14 days to delete")
    else:
        if hasDeleted:
            tk.messagebox.showinfo(
                "Success", "No Minecraft backups to create\nAll Minecraft backups older than 14 days deleted")
        else:
            tk.messagebox.showinfo(
                "Success", "No Minecraft backups to create\nNo Minecraft backups older than 14 days to delete")

print("Done!")
