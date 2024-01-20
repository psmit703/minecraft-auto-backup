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
backupServerList = configs[8][0:-1]
deleteOldBackups = configs[9][0:-1]
showGUI = configs[10][0:-1]
numDaysAutoDelete = configs[11][0:-1]
minBackupsForDeletion = configs[12][0:-1]
maxBackupsForDeletion = configs[13][0:-1]

hasBackedUp = False
hasDeleted = False

# ensure destination directory exists, create if not
if os.path.exists(backupDir + "minecraft-backups" + "\\" + deviceName) is not True:
    if os.path.exists(backupDir + "minecraft-backups") is not True:
        os.mkdir(backupDir + "minecraft-backups")

    os.mkdir(backupDir + "minecraft-backups" + "\\" + deviceName)

backupDir = backupDir + "minecraft-backups" + "\\" + deviceName + "\\"

# Backup server list, skip if false
if backupServerList == "True":
    # skip if server list file (servers.dat) doesn't exist
    if os.path.exists(mcDir + "servers.dat"):
        try:
            os.makedirs(backupDir + "server-list" + "\\" + date)
            shutil.copy(mcDir + "servers.dat", backupDir +
                        "server-list" + "\\" + date + "\\" + "servers.dat")
        except Exception as e:
            print("Failed to backup server list")
            print(e)
        else:
            print("Successfully backed up server list")
            hasBackedUp = True

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
# Deletes all subfolders of logs, mods, resourcepacks, saves, schematics, screenshots that are older than numDaysAutoDelete days
if deleteOldBackups == "True":
    for folder in os.listdir(backupDir):
        if os.path.isdir(backupDir + folder) and (len(os.listdir(backupDir + folder)) >= int(minBackupsForDeletion)
                                                  or int(minBackupsForDeletion) == -1):
            for subfolder in os.listdir(backupDir + folder):
                if os.path.isdir(backupDir + folder + "\\" + subfolder):
                    if (datetime.now() - datetime.strptime(subfolder, "%Y-%m-%d_%H-%M-%S")).days > int(numDaysAutoDelete):
                        try:
                            shutil.rmtree(backupDir + folder +
                                          "\\" + subfolder)
                        except Exception as e:
                            print("Failed to delete " + folder +
                                  " backups older than %s days" % numDaysAutoDelete)
                            print(e)
                        else:
                            print("Successfully deleted " + folder +
                                  " backups older than %s days" % numDaysAutoDelete)
                            hasDeleted = True

    for folder in os.listdir(backupDir):
        if os.path.isdir(backupDir + folder) and len(os.listdir(backupDir + folder)) > int(maxBackupsForDeletion) and int(maxBackupsForDeletion) != -1:
            # sort subfolders by date, oldest first
            subfolders = os.listdir(backupDir + folder)
            subfolders.sort(key=lambda x: datetime.strptime(
                x, "%Y-%m-%d_%H-%M-%S"))

            while len(subfolders) > int(maxBackupsForDeletion):
                try:
                    shutil.rmtree(backupDir + folder + "\\" + subfolders[0])
                except Exception as e:
                    print("Failed to delete " + folder +
                          " backups older than %s days" % numDaysAutoDelete)
                    print(e)

                subfolders.pop(0)

                hasDeleted = True

    # if no backups were deleted, do not print that all backups older than numDaysAutoDelete days were deleted
    if hasDeleted:
        print("All backups older than %s days or outside of specified arguments deleted" %
              numDaysAutoDelete)

# display GUI if selected
if showGUI == "True":
    root = tk.Tk()
    root.withdraw()

    if hasBackedUp:
        if hasDeleted:
            tk.messagebox.showinfo(
                "Success", "Minecraft backup complete\nAll Minecraft backups older than %s days or outside of specified arguments deleted" % numDaysAutoDelete)
        else:
            tk.messagebox.showinfo(
                "Success", "Minecraft backup complete\nNo Minecraft backups older than %s days or outside of specified arguments to delete" % numDaysAutoDelete)
    else:
        if hasDeleted:
            tk.messagebox.showinfo(
                "Success", "No Minecraft backups to create\nAll Minecraft backups older than %s days or outside of specified arguments deleted" % numDaysAutoDelete)
        else:
            tk.messagebox.showinfo(
                "Success", "No Minecraft backups to create\nNo Minecraft backups older than %s days or outside of specified arguments to delete" % numDaysAutoDelete)

print("Done!")
