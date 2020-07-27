#!/usr/bin/env python
# -*-coding: utf-8 -*

"""Manuel and django importation"""
try:
    from .data.generateFakeCommand import FakeCommand
    from .tableDelais.waitingTable import ToWait
except ModuleNotFoundError:
    from data.generateFakeCommand import FakeCommand
    from tableDelais.waitingTable import ToWait

import random


class Main:

    def __init__(self):
        self.rush = []


    def generateDataSituation(self, timeReceiveCommand, timeWorkCooker, timeWorkServeur, menu):

        assignateTable = None
        #Class instance.
        fakeData = FakeCommand()
        #Generate fake commands randomly.
        fakeData.generateSituation()
        #Recuperate menu user if one.
        if menu != None: assignateTable = fakeData.generateCommand(menu)
        #Recuperate commands.
        self.rush = fakeData.getterRush()

        #Time delais for cooker and serveur.
        finalTimeMinServeur = 0
        finalTimeCookerPrep = 0

        commandTime = []

        for nbCommand, command in enumerate(self.rush):

            #Command.
            if command[0] > 0 or command[1] > 0 or command[2] > 0:

                #Instance of class wait program.
                waiting = ToWait(command, timeReceiveCommand, timeWorkCooker, timeWorkServeur)
                #Genrate cooker and serveur.
                waiting.generateWorker()
                #Associate at each product his time.
                waiting.countTimeProd()
                #Add time to the cooker delais.
                finalTimeCookerPrep += waiting.cookerTakeCommand()

                #Not first command so Go and re go the kitchen from serveur
                if nbCommand > 0:
                    #Go and re go the kitchen from serveur
                    time = waiting.timeTravelServeurInCourse() * 2
                    #Add it to serveur delais
                    finalTimeMinServeur += time
                    #Recuperate time.
                    commandTime.append(time)
 
                #First command
                else:
                    #Recuperate time of serveur
                    time = waiting.timeTravelServeurInCourse()
                    #Add it to his final time.
                    finalTimeMinServeur += time

            #No command (can be a drink).
            else:
                commandTime.append(0)


        try:
            #Final time.
            timeDelais = waiting.finalTime(finalTimeMinServeur, finalTimeCookerPrep)
        except UnboundLocalError:
            pass

        return timeDelais, commandTime, assignateTable

    def getterNbCommand(self):
        """Recuperate all commands"""
        return self.rush



if __name__ == "__main__":

    #Construction manuel to a command.
    otherCommand = [1, 0, 0]

    main = Main()

    timeWorkCooker  = random.randrange(1, 10)
    timeWorkServeur = random.randrange(1, 8)
    lastPreparationTime = 0

    timeDelais, commandTime, assignateTable = main.generateDataSituation(
        lastPreparationTime, timeWorkCooker, timeWorkServeur, otherCommand)

    commands = main.getterNbCommand()

    for i, j in zip(commands, commandTime):
        print(i, j)

    print(timeDelais)
