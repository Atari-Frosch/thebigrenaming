#!/usr/bin/env python

import os
import time

class BigRenamer(object):
    def __init__(self):
        self.logfile = open("renamer.log", "w")

    def getFolderNames(self, path):
        allFolders = os.listdir(path)
        cleanFolders = self.checkFolders(allFolders)
        return cleanFolders

    def checkFolders(self, allFolders):
        cleanFolders = []
        for i in range(len(allFolders)):
            currentFoldername = allFolders[i]
            if currentFoldername != "":
                if int(currentFoldername[0]) == 2:
                    cleanFolders.append(currentFoldername)
        return cleanFolders

    def filesOfFolder(self, folder): 
        fileList = os.listdir(folder)
        return fileList

    def getFiledate(self, fileName):
        fileStat = os.stat(fileName)
        rawTimestamp = fileStat.st_mtime
        structTimestamp = time.localtime(rawTimestamp)
        fileTimestamp = time.strftime("%Y%m%d-%H%M%S", structTimestamp)
        return fileTimestamp

    def renameFile(self, oldFilename, newFilename):
        os.rename(oldFilename, newFilename)
        self.logfile.write("Renamed " + oldFilename + " to " + newFilename + "\n")

myRenamer = BigRenamer()
filepath = "/data/Fotos/CanonEOS350D/"
folderlist = myRenamer.getFolderNames(filepath)
for i in range(len(folderlist)):
    currentPath = filepath + folderlist[i] + "/"
    print "currentPath:", currentPath
    files = myRenamer.filesOfFolder(currentPath)
    for j in range(len(files)):
        oldFilename = currentPath + files[j]
        # print "oldFilename:", oldFilename 
        if oldFilename.endswith("JPG"):
            newFilename = currentPath + myRenamer.getFiledate(oldFilename) + ".jpg"
            # print "newFilename:", newFilename
        elif oldFilename.endswith("CR2"):
            newFilename = currentPath + myRenamer.getFiledate(oldFilename) + ".cr2"
            # print "newFilename:", newFilename
        else:
            print "ERROR: File extension of", oldFilename, "does not show a recognized file format!"

        myRenamer.renameFile(oldFilename, newFilename)

myRenamer.logfile.close()
