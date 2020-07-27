#!/usr/bin/env python
# -*-coding: utf-8 -*

"""----------------------- IMPORTATIONS -----------------------"""

#Generate fake choice user of items
from creationModel.generationChoix.generateChoice import GenerateCombo
from creationModel.generationModel.generateModelApriori  import GenerateModel



class Main:
    """Create and register on csv file a random choices
    for Apriori Algorithm"""

    def __init__(self):
        self.creationMenuNb = 5000


    def generatingCombo(self):
        """Function for generating random choice for
        the Apriori Algorithm"""

        #Make an instance of class.
        generateChoice = GenerateCombo(self.creationMenuNb)
        #Generate random choices
        generateChoice.generate()
        #Write generated choices
        generateChoice.writeMenuInCsv()


    def generatingModel(self):
        """Here we do the Apriori Algorithm"""

        #Create object instance class
        generateModel = GenerateModel(self.creationMenuNb)

        #From csv recuperate simulate commands.
        dataMenu = generateModel.recuperateData()
        #generateModel.displayList(dataMenu)

        #Counter each items presence.
        dicoCount = generateModel.counterItems(dataMenu)
        #generateModel.displayDico(dicoCount)

        #Filter items if higter minSupp
        dicoFilter = generateModel.filter(dicoCount)
        #generateModel.displayDico(dicoFilter)

        #For all item keep, make them by pairs.
        listePair = generateModel.generatePair(dicoFilter)
        #generateModel.displayList(listePair)

        #Counter each presence of pairs from the data original
        dicoPairCount = generateModel.countPair(listePair, dataMenu)
        #generateModel.displayDico(dicoPairCount)

        #Keep pair if there are highter of minSupp
        dicoPairFiler = generateModel.filterPair(dicoPairCount)
        #generateModel.displayDico(dicoPairFiler)

        #Verify percent of confidence.
        assocRulesPairs = generateModel.associationRule(
            dicoPairFiler, dicoCount, dicoPairCount)

        #generateModel.displayDico(assocRulesPairs)

        #Savegarde model in a csv file.
        generateModel.writeModelInCsv(assocRulesPairs)



if __name__ == "__main__":

    #Object main
    main = Main()

    #Random choice menu
    main.generatingCombo()

    #Generate Model Apriori Algorithm
    main.generatingModel()
