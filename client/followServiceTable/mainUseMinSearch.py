#For treat picture
import cv2

#For .csv file.
import csv
import numpy as np



#Import paths for localisation picture
from .constantes import PATH_TABLE_PICTURE
#Import paths for localisation csv coords
from .constantes import PATH_COORDINATES_TABLE


from .minSearch.minSearch import SearchMinDistance
from .animation.animation import Animation


class MainTableAssignation:
    """Generate min distance beetween table for a server"""

    def __init__(self):

        #Picture of tables 600 * 1200 white.
        self.picture = np.zeros([600,1200,3],dtype=np.uint8)
        self.picture.fill(255)

        self.objectClassAnim = None

    def animationTable(self):
        """Create from csv coordiantes, table plan."""

        #Instace class animation
        animation = Animation(self.picture, PATH_COORDINATES_TABLE)
        #From csv recuperate coordinates.
        animation.recuperateCoordinatesTables()
        #Draw it in copy picture.
        animation.displayTable()
        #Put number of the table
        animation.displayNumeroTable()
        #Recuperate picture
        self.picture = animation.getterCopy()
        #Recuperate instance class animation
        self.objectClassAnim = animation


    def getterObjectClassAnim(self):
        """Return class instance animation"""
        return self.objectClassAnim


    def recuperateTable(self, roadTable):
        """From departure search earch table min distance."""
        #Class instance
        searchMinDistance = SearchMinDistance()
        #Recuperate each coordiante of each table from current pos.
        searchMinDistance.recuperateCoordinates()
        #Search min distance from our current pos and all coordinate.
        searchMinDistance.searchMinDistance(roadTable)
        #Recuperate min road table.
        roads = searchMinDistance.getterRoad()

        #print(roads)
        return roads


    def animationRoad(self, roads, objectClassAnim):
        #Sauvegarde all trajets picture in static.
        myTable = objectClassAnim.makeRoad(roads)
        return myTable


if __name__ == "__main__":

    roadTable = [15, 20, 2, 5]

    main = MainTableAssignation()
    main.animationTable()
    roads = main.recuperateTable(roadTable)
    objectClass = main.getterObjectClassAnim()
    main.animationRoad(roads, objectClass)
