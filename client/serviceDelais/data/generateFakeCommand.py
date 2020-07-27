#!/usr/bin/env python
# -*-coding: utf-8 -*

"""----------------------- IMPORTATIONS -----------------------"""
#For paths.
import sys
sys.path.append("..")

import random


"""-------------------------- CLASS -----------------------"""
class FakeCommand:

    def __init__(self):
        self.listeDataCommand = []


    def generateSituation(self):
        """We can have 5 persons in a table, max 2 coockers and 2 serveurs
        can take the plate"""

        for _ in range(random.randrange(1, 20)):

            nbProduct5  = random.randrange(0, 2)
            nbProduct10 = random.randrange(0, 2)
            nbProduct15 = random.randrange(0, 2)

            distance  = random.randrange(1, 500)

            situation = [nbProduct5, nbProduct10, nbProduct15, distance]
            self.listeDataCommand.append(situation)


    def generateCommand(self, command):
        """Add command to precedents and assign a table"""

        #Recuperate command time (5 entrance, 10 plate, 15 dessert)
        situation = [0 if i == "" else 1 for i in command]
        #Generate a table distance randomly.
        table = random.randrange(1, 500)
        #Add distance random to the simulation.
        situation.append(table)
        #Append user situation to other command in course.
        self.listeDataCommand.append(situation)

        return table


    def getterRush(self):
        """Recuperate all commands"""
        return self.listeDataCommand
