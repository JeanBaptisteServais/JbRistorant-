#!/usr/bin/env python
# -*-coding: utf-8 -*

"""File .py for create and write items into a .csv file"""


"""----------------------- IMPORTATIONS -----------------------"""

#For paths.
import sys
sys.path.append("../..")

#For .csv file.
import csv

#path of the csv folder
from constantes import PATH_CSV
#List of plate separatly
from constantes import LIST_ITEMS
#path of savegarde model
from constantes import PATH_CSV_MODEL


class GenerateModel:
    """Generate APriori suggestion of product from simulate data"""

    def __init__(self, creationMenuNb):
        self.dataMenu = []

        self.minSuppCount  = creationMenuNb * 0.5 / 100
        self.minConfidence = 60


    def displayList(self, liste):
        """Display list content"""
        [print(i) for i in liste]


    def displayDico(self, dico):
        """Display dico content"""
        [print(k, v) for k, v in dico.items()]


    def recuperateData(self):
        """Recuperate all menu random generated from the csv file"""

        with open(PATH_CSV, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                self.dataMenu.append(row)

        return self.dataMenu


    def counterItems(self, liste):
        """Counter each item presence and put it in dico"""
        dicoCount = {}

        #Create dico: item = 0
        for i in liste:
            for j in i:
                dicoCount[j] = 0
        #Item appear: item += 1
        for i in liste:
            for j in i:
                dicoCount[j] += 1

        return dicoCount


    def filter(self, dico):
        """Keep item if there are highter than minSupport"""

        dicoFilter = {}
        #Verify presence higgter minSupp.
        for k, v in dico.items():
            if v >= self.minSuppCount:
                dicoFilter[k] = v

        return dicoFilter


    def generatePair(self, dico):
        """For all item keep, make them by pairs."""

        liste = []
        #From the last filter dico, append it to a list.
        for k, v in dico.items():
            liste.append(k)

        #Make pairs.
        listePair = []
        for i in liste:
            for j in liste:
                if i != j and\
                   (i, j) not in listePair and\
                   (j, i) not in listePair:
                    listePair.append((i, j))

        return listePair


    def countPair(self, listePair, dataMenu):
        """Counter each presence of pairs from the data original"""

        #Create a dictionnary with pair = 0
        dicoPairCount = {}
        for i in listePair:
            dicoPairCount[i] = 0

        #For menu count pair presence.
        for i in dataMenu:
            for (i1, i2) in listePair:
                if i1 in i and i2 in i:
                    dicoPairCount[(i1, i2)] += 1

        return dicoPairCount


    def filterPair(self, dicoPairCount):
        """Keep pair if there are highter of minSupp"""

        dicoPairFiler = {}

        for k, v in dicoPairCount.items():
            if v >= self.minSuppCount:
                dicoPairFiler[k] = v

        return dicoPairFiler


    def associationRule(self, dicoPairFiler, dicoCount, dicoPairCount):

        dicoStrongAssocRule = {}

        for pairs, presence in dicoPairFiler.items():
            #Recuprate large item from plate.
            for plate in pairs:
                dicoStrongAssocRule[plate] = (presence / dicoCount[plate]) * 100
                #print(plate, (presence / dicoCount[plate]) * 100)

            #Make items by pairs.
            listePair = []
            for plate1 in pairs:
                for plate2 in pairs:
                    #Verify pair isn't already in list.
                    if plate1 != plate2 and\
                       (plate1, plate2) not in listePair and\
                       (plate2, plate1) not in listePair:
                        listePair.append((plate1, plate2))

            #Recuperate percent of confidence of each pairs.
            for (i1, i2) in listePair:
                try:
                    dicoStrongAssocRule[(i1, i2)] = (presence / dicoPairCount[(i1, i2)]) * 100
                    #print((i1, i2), (v / dicoPairCount[(i1, i2)]) * 100)
                except KeyError:
                    dicoStrongAssocRule[(i2, i1)] = (presence / dicoPairCount[(i2, i1)]) * 100
                    #print((i1, i2), (v / dicoPairCount[(i2, i1)]) * 100)


        #Filter pair if confidence > minConfidence.
        dicoRules = {}
        for pairs, percent in dicoStrongAssocRule.items():
            if percent >= self.minConfidence:
                dicoRules[dicoRules] = percent

        return dicoRules



    def writeModelInCsv(self, dicoRules):
        """Write in a csv, random menu choice"""

        csvfile = open(PATH_CSV_MODEL, 'w')
        for k, v in dicoRules.items():
            liste = []
            if k == tuple(k):
                for i in k:
                    liste.append(i)
            else:
                liste.append(k)

            liste.append(str(v))
            line = ";".join(liste) + "\n"
            csvfile.write(line)

        csvfile.close()
