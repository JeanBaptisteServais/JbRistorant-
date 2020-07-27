#!/usr/bin/env python
# -*-coding: utf-8 -*

"""File .py of recuperate coordinate of table for the service table application"""

class RecuperateCoordinates:
    """From a picture, we recuperate color who give coordinates"""

    def __init__(self, picture):
        self.picture = picture

        self.departure  = []
        self.tableCoord = []

    def recuperateCoordinates(self):
        """Recuperate coordinates from colors"""

        #Dimension of the picture
        height, width = self.picture.shape[:-1]

        #From 0 to dimension on x and y try to catch green and red color.
        for y in range(0, height):
            for x in range(0, width):

                #Red for table
                if self.picture[y, x][0] == 36 and\
                   self.picture[y, x][1] == 28 and\
                   self.picture[y, x][2] == 236:
                    self.tableCoord.append((x, y))

                #Green for departure
                elif self.picture[y, x][0] == 69 and\
                     self.picture[y, x][1] == 209 and\
                     self.picture[y, x][2] == 14:
                      self.departure.append((x, y))
    

    def getterDeaparture(self):
        """Make a departure coord getter list"""
        return self.departure

    def getterCoordTable(self):
        """Make a table coord getter list"""
        return self.tableCoord


    def savegardeCoords(self, PATH, departureCoord, tableCoord):
        """Savegarde coordinates into csv file"""

        #Make on list with str coord
        coordinates = []
        for i in departureCoord:
            coordinates.append([str(i[0]), str(i[1])])

        for i in tableCoord:
            coordinates.append([str(i[0]), str(i[1])])

        #run the list and write it into csv file.
        csvfile = open(PATH, 'w')
        for coord in coordinates:
            line = ";".join(coord) + "\n"
            csvfile.write(line)

        csvfile.close()
