import random

class ToWait:

    def __init__(self, command, timeReceiveCommand, timeWorkCooker, timeWorkServeur):

        #Number random of workers
        self.nbCooker = 0
        self.nbSeveur = 0

        #Command receive
        self.command = command

        #Command receive in function of the last command time prepare
        #nb plate and their preparation time
        self.counterPreparationPlate = timeReceiveCommand
        self.travelServeur = 0

        #Time work from workers
        self.timeWorkCooker  = timeWorkCooker
        self.timeWorkServeur = timeWorkServeur

        #Where is that, oh an unicorn ! 
        self.constanteNonRobot = 5
        self.constanteSourire = 2

        self.ratioMap = 1000


    def generateWorker(self):
        """Generate cookers and serveurs"""

        self.nbCooker  = random.randrange(1, 5)
        self.nbSeveur  = random.randrange(1, 5)


    def countTimeProd(self):
        """Associate time of the plate"""

        prod5, prod10, prod15, _ = self.command

        prod5  = prod5  * 5
        prod10 = prod10 * 10
        prod15 = prod15 * 15

        self.counterPreparationPlate += (prod5 + prod10 + prod15)
        #print("preparation theoric: ", self.counterPreparationPlate)

    def cookerTakeCommand(self):
        """Count delais cooker"""

        #print("cooker are: ", self.nbCooker, "works from: ", self.timeWorkCooker)

        #Plate divide by number of cooker
        self.counterPreparationPlate = self.counterPreparationPlate / self.nbCooker
        #Constante and gamma who's up in function of time work.
        constante = self.constanteNonRobot + (self.timeWorkCooker * 0.8)
        #print("constante fatigue + non robot: ", constante)

        #Theoric preparation + constante + sigma.
        self.counterPreparationPlate = self.counterPreparationPlate + constante

        #print("final preparation: ", self.counterPreparationPlate)
        return self.counterPreparationPlate



    def timeTravelServeurInCourse(self):
        """Serveur delais"""

        #Convert distance to km. (1 euclidian = 1m)
        distanceKm = self.command[3] / 1000
        #Time traval of serveur (he walk 3 km/h)
        timeGoAndReGoH = distanceKm / 3
        #Convert that in minute
        timeMin = (timeGoAndReGoH * 60)

        #print("nb serveur: ", self.nbSeveur)
        #print("serveur time to go to table: ", timeMin)

        #Make his constante + sigma who' up in function of time work.
        constante = self.constanteSourire + (self.timeWorkServeur * 0.9)
        #Add theric traval + constante + sigma.
        finalTimeMin = timeMin + constante
        #print("serveur time to go to table: ", finalTimeMin)

        return finalTimeMin


    def finalTime(self, finalTimeMinServeur, finalTimeCooker):
        """Return final time in hour + min"""
        finalTimeMin = finalTimeMinServeur + finalTimeCooker
        timeDelais = str(int(finalTimeMin / self.nbSeveur / 60)) + " h et " +\
                          str(int((finalTimeMin / self.nbSeveur) % 60)) +  " min"

        return timeDelais




























