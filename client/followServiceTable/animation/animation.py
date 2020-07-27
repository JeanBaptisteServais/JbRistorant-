import cv2
#For .csv file.
import csv

import random

class Animation:
    """Write and make traject picture"""

    def __init__(self, picture, pathCoordCsv):

        self.picture = picture
        self.pathCoordCsv = pathCoordCsv
        self.coordinatesTable = []
        self.departure = 0
        self.copy = self.picture.copy()

    def recuperateCoordinatesTables(self):
        """Recuperate all points in csv file of table coordinates"""

        with open(self.pathCoordCsv, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                self.coordinatesTable.append((int(row[0]), int(row[1])))


        self.departure = self.coordinatesTable[0]
        self.coordinatesTable = self.coordinatesTable[1:]


    def displayTable(self):
        """Make all table as red circle"""

        black = (0, 0, 0)
        red   = (0, 0, 255)
        size  = 5
        remplissage = 1

        for index, coordinates in enumerate(self.coordinatesTable):
            cv2.circle(self.copy, coordinates, size, red, remplissage)

        cv2.circle(self.copy, self.departure, size, red, remplissage)


    def displayNumeroTable(self):
        """Display number of the table"""
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 0)

        cv2.putText(self.copy, str(0), self.departure, font, 0.4, color, 1, cv2.LINE_AA)

        for index, coordinates in enumerate(self.coordinatesTable):
            cv2.putText(self.copy, str(index + 1), coordinates, font, 0.4, color, 1, cv2.LINE_AA)


    def getterCopy(self):
        """Recuperate copy"""
        return self.copy


    def makeRoad(self, road):
        """For the road draw each coordinate reliate by a line
        and save it. Choose a random table and put the line in green"""

        #Choose a table randomly
        myTable = random.randrange(2, len(road))

        copy = self.copy
        #Run the list road command
        for i in range(len(road)):
            #Regualtion of the length list.
            if i < len(road) - 1:
                #Green is table command
                if myTable == i + 1:
                    cv2.line(copy, road[i], road[i + 1], (0, 255, 0), 2)
                #Red other command
                else:
                    cv2.line(copy, road[i], road[i + 1], (255, 0, 0), 2)
                #Save if in static for display.
                cv2.imwrite("static/waitService/" + str(i) + ".jpg", copy)

        return myTable
