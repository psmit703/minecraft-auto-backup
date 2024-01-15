# Minecraft (Java Edition) Auto Backups

This is a utility for automatically creating local backups of Minecraft (Java Edition) data. It is intended for use on Windows machines and has been tested on Windows 10. This utility can be used in conjunction with tools such as Windows File Explorer's built-in OneDrive functionality to allow for cloud-based backups, however that is not handled by this program and is entirely reliant on OneDrive or whatever other external technology is being used.

This program has not been tested with Minecraft (Bedrock Edition). I am not familiar with how the relevant game data is stored for Bedrock Edition and I currently have no need to learn that. Other people are welcome to create that functionality if desired and, perhaps more importantly, if possible given the weirdness of Windows at times.

## Usage

Firstly, download the file listed at <code>https://github.com/psmit703/minecraft-auto-backup/blob/main/script.py</code>.

It is recommended to use Windows Task Scheduler to automatically run this program. This can be done once daily, at some other interval, or based on some action.

To manually run this program, open File Explorer and either double click the program or right click it and either select "Open" or "Open with -> Python {version}." As long as Python is installed, (and as long as the option has not been changed) Python should be the default option for double-clicking or selecting "Open." Any requried directory permissions are the responsibility of the user.

The program copies files in the Minecraft directory based on what is selected in config.txt (see "Requirements / Config.txt") and pastes them in a directory specified in config.txt. This file, config.txt, allows the user to specify what specific data to back up, whether to automatically delete backups older than thirty days, and whether to display a dialog box upon completion.

## Requirements

### Python

This program requires Python to be installed on the computer it is being run on. It has been tested with Python 3.11.7; I expect it to work with other versions, however I have not tested that.

### Python Modules

This program uses the <code>os</code>, <code>socket</code>, <code>datetime</code>, <code>shutil</code>, and <code>tkinter</code> modules. These modules should automatically be installed alongside Python.

### Config.txt

A file called <code>config.txt</code> should be in the same directory as the program. It should follow the formatting of <code>configFormat.txt</code>. The proper format of each field is listed below:

#### mcDir

mcDir should be the directory that Minecraft data. By default, this directory can be found by typing <code>%appdata%</code> in the File Explorer address bar and selecting <code>.minecraft</code>. For Windows operating systems, the result should be followed by a backslash (<code>\\</code>).

#### backupDir

backupDir should be the directory that Minecraft data will be backed up to. The result of this should be followed be a backslash (<code>\\</code>). Inside this directory, the program will automatically create a subdirectory called <code>minecraft-backups</code>. This process will recursively be done by the program with several more folders and should result in a file tree similar to the following diagram:

Root (user-specified)
|-> minecraft-backups
    |-> {device-name}
        |-> saves
            |-> {backup date}
                |-> copied content of mcDir\saves
        |-> mods
            |-> {backup date}
                |-> copied content of mcDir\mods
        |-> schems
            |-> {backup date}
                |-> copied content of mcDir\config\worldedit\schematics
        |-> screenshots
            |-> {backup date}
                |-> copied content of mcDir\screenshots
        |-> logs
            |-> {backup date}
                |-> copied content of logs from mcDir
        |-> resourcepacks
            |-> {backup date}
                |-> copied content of mcDir\resourcepacks

#### Lines 3 through 8

Assuming the file is zero-indexed, lines 3 inclusive through 8 inclusive should each either be <code>True</code> or <code>False</code>, depending on which data the user wants to have backed up. Lines 3 through 8 are in the following order:

backupSaves
backupMods
backupSchems
backupScreenshots
backupLogs
backupResourcePacks

#### deleteOldBackupsThirtyDays

Like with lines 3 through 8, this should be either <code>True</code> or <code>False</code>. This option determines whether or not to delete backups older than thirty days.

#### tkinter

Like with lines 3 through 8, this should be either <code>True</code> or <code>False</code>. This option determines whether or not the program will display a tkinter system dialog box upon completion.

### Windows

This program is intended for use on Windows machines and was tested on Windows 10. It should also work on Windows 11 due to their similar high-level file tree structuring, however this has not been tested. Similarly, I have not tested this program with other operating systems such as any of the Linux distributions or any of Apple's operating systems.
