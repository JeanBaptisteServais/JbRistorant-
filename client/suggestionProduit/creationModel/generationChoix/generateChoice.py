#!/usr/bin/env python
# -*-coding: utf-8 -*


"""----------------------- IMPORTATIONS -----------------------"""
#For paths.
import sys
sys.path.append("../..")
#For .csv file.
import csv
#For random operation.
import random

#path of the csv folder
from constantes import PATH_CSV
#path of list items plate.
from constantes import LIST_ITEMS_MENU


"""-------------------------- CLASS -----------------------"""

class GenerateCombo:
    """Class for create & write products in csv"""

    def __init__(self, creationMenuNb):
        self.randomChoiceMenu = []
        self.creationMenuNb = creationMenuNb


    def generate(self):
        """Generate random choices from items"""

        for menu in range(self.creationMenuNb):

            randomMenu = []
            for categoryPlate, plate in LIST_ITEMS_MENU.items():

                randomPlate = random.choice(plate)
                if randomPlate != "None":
                    randomMenu.append(randomPlate)

            self.randomChoiceMenu.append(randomMenu)


    def writeMenuInCsv(self):
        """Write in a csv, random menu choice"""

        csvfile = open(PATH_CSV, 'w')
        for i in self.randomChoiceMenu:
            line = ";".join(i) + "\n"
            csvfile.write(line)

        csvfile.close()
