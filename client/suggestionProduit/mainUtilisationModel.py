#!/usr/bin/env python
# -*-coding: utf-8 -*

import csv

from .constantes import PATH_CSV_MODEL
from .constantes import LIST_ITEMS_MENU


class UseModelSuggestion:
    """Recuperate suggerate item from a choice"""

    def __init__(self):
        self.data = []
        self.suggestion1 = []
        self.suggestion2 = []
        self.categoryChoice = None

        self.toSuggerate = []

    def recuperateSuggestion(self):
        """Recuperate all menu random generated from the csv file"""

        with open(PATH_CSV_MODEL, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                self.data.append(row)

    def getterData(self):
        """Recuperate data"""
        return self.data


    def recuperateCategoryPlate(self, plate):
        """Recuperate the category of the current plate choice"""

        categoryPlate = None

        #From dico category, plates, we verify a matching and return category.
        for category, listPlate in LIST_ITEMS_MENU.items():
            for platesInList in listPlate:
                if plate == platesInList:
                    categoryPlate = category
                    break

        return categoryPlate


    def recuperateChoice(self, choice):
        """We recuperate all suggestion from our choice"""

        #Recuperate category of the plate
        self.categoryChoice = UseModelSuggestion.recuperateCategoryPlate(self, choice)
        #print(self.categoryChoice)

        #In data recuperate all second item in pair with the choice.
        for (item1, item2, percent) in self.data:
            if item1 == choice and item2 not in self.suggestion1:
                self.suggestion1.append(item2)
            elif item2 == choice and item1 not in self.suggestion1:
                self.suggestion1.append(item1)

        #print(self.suggestion1)

        #In data recuperate all second item in pair with the last second item
        for (item1, item2, percent) in self.data:
            for i in self.suggestion1:
                if item1 == i and item2 not in self.suggestion2:
                    self.suggestion2.append(item2)
                elif item2 == i and item1 not in self.suggestion2:
                    self.suggestion2.append(item1)

        #print(self.suggestion2)


    def filterSuggestions(self):
        """If we chosen a dessert delete all dessert"""

        self.toSuggerate = []

        #Filter the same plate category.
        for i in self.suggestion1:
            category = UseModelSuggestion.recuperateCategoryPlate(self, i)
            if category != self.categoryChoice:
                self.toSuggerate.append(i)


    def getterSuggestion(self):
        """Recuperate suggerate"""
        return self.toSuggerate

        

if __name__ == "__main__":

    choice = "tartines"

    model = UseModelSuggestion()
    model.recuperateSuggestion()
    data = model.getterData()
    #print(data)


    model.recuperateChoice(choice)
    model.filterSuggestions()

    suggestions = model.getterSuggestion()
