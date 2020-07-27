#!/usr/bin/env python
# -*-coding: utf-8 -*


"""File .py of path of the choice algortyme application"""
"""------------------------- IMPORTATION -------------------------"""
#For .csv file.
import csv
#For picture
import cv2
#For euclidean picture
from scipy.spatial import distance

#path of savegarde model
from ..constantes import PATH_COORDINATES_TABLE



"""------------------------- CLASSES -------------------------"""
class SearchMinDistance:
    """From a current position search all other coordinates
    choose the minimal coordinate from our pos"""

    def __init__(self):

        self.coordinatesTable = []
        self.departure = 0
        self.closedList = []
        

    def recuperateCoordinates(self):
        """Recuperate table coordinate from a csv file"""

        coord = []
        #Run a csv file and recuperate coords.
        with open(PATH_COORDINATES_TABLE, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                coord.append((int(row[0]), int(row[1])))
 
        #Recuperate the deapature
        self.departure = coord[0]

        #Savegarde all other coord.
        for i in coord[1:]:
            self.coordinatesTable.append(i)


    def searchMinDistance(self, commandes):
        """From a point, search all other points of the command
        iterative: recuperate the minimal points of current pos"""

        #First point (departure).
        currentPoints = self.departure
        #Add to closed list the deaparture.
        self.closedList.append(currentPoints)

        #Recuperate all coordinates of simulate command.
        commandTable = [self.coordinatesTable[commande]
                        for commande in commandes]

        #For each table search the minimal next distance table.
        for _ in range(len(commandTable)):

            #Maximal distance with his index.
            maximumDistance = 10000000000000000
            indexTable = 0
            #Search the minimal next command table coordinates.
            for index, coordinate in enumerate(commandTable):

                #Verify coordinates isn't the current and not in closed list.
                if coordinate not in self.closedList and\
                   coordinate != currentPoints:

                    #Make euclidean distance
                    dist = distance.euclidean(currentPoints, coordinate)
                    #Verify if distance can be less of the last distance.
                    if dist < maximumDistance:
                        #Recuperate distance and his index.
                        maximumDistance = dist
                        indexTable = index
            #current is the minimal distance of the last distance table
            #Add it to closed list.
            currentPoints = commandTable[indexTable]
            self.closedList.append(currentPoints)




    def getterRoad(self):
        """Recuperate closed list who's our travel"""
        return self.closedList
