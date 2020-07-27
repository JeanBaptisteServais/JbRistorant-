#!/usr/bin/env python
# -*-coding: utf-8 -*

"""File .py of path of the choice algortyme application"""


"""----------------------- IMPORTATIONS -----------------------"""
#Recuperate coordinate of tables
from tablesCoordinates.recuperateCoordinateTable import RecuperateCoordinates
#minSearch
from minSearch.minSearch import SearchMinDistance

#Import paths for localisation picture
from constantes import PATH_TABLE_PICTURE
#Import paths for localisation csv coords
from constantes import PATH_COORDINATES_TABLE

#For treat picture
import cv2

#For .csv file.
import csv


"""----------------------- MAIN CLASS -----------------------"""
class Main:

    """Application for found coordinate of the table service
    and to savegarde it into a csv file"""

    def __init__(self, pathPicture, pathSave):
        """Load in cv2 the picture table"""

        #Picture of tables
        self.picture = cv2.imread(PATH_TABLE_PICTURE)

        #list of coordinates need for dijkstra
        self.departureCoord = None
        self.tableCoord = None
        self.pathSave = pathSave

    def recuperateCoord(self):
        """Red for table, green for departure,
        from colors we recuperate coordinates"""

        #Instance class RecuperateCoordinates
        coordTable = RecuperateCoordinates(self.picture)
        #From color recuperate coordinates
        coordTable.recuperateCoordinates()
        #Recuperate departure coord in list
        self.departureCoord = coordTable.getterDeaparture()
        #Recuperate tables coord in list
        self.tableCoord = coordTable.getterCoordTable()
        #Savegarde coord into csv file
        coordTable.savegardeCoords(
            self.pathSave, self.departureCoord, self.tableCoord)

if __name__ == "__main__":

    main = Main(PATH_TABLE_PICTURE, PATH_COORDINATES_TABLE)
    main.recuperateCoord()


