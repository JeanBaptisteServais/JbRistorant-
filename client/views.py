"""
   View who's response of templates
"""

#Import for return a template
from django.shortcuts import render
from django.http import HttpResponse
#Import for load a template
from django.template import loader

#It for our random data.
import random

#Paths
from .constantes import pathHome
from .constantes import pathTableService
from .constantes import pathDelais

from .constantes import pathVisualisationProduct
from .constantes import pathSelectionProduct1
from .constantes import pathSelectionProduct2
from .constantes import pathSelectionProduct3

from .constantes import DICO_PRODUCT_LOCATION
from .constantes import DICO_NAME_SITE_TO_MODEL

from .suggestionProduit.constantes import LIST_ITEMS_MENU
from .suggestionProduit.mainUtilisationModel import UseModelSuggestion
from .serviceDelais.mainWaitingTableUse import Main
from .followServiceTable.mainUseMinSearch import MainTableAssignation



def home(request):
    """Home template"""
    return render(request, pathHome)


"""--------------------------------------- SERVICE TABLE ------------------------------------"""
def makeRandomCommands():
    """We choose 10 tables beetween 0 to 27 randomly"""

    roadTable = []
    #Choose 10 tables randomly.
    for _ in range(10):

        #Avoid doublon.
        continuer = True
        while continuer:
            #Choose a table 0 to 27.
            table = random.randrange(0, 27)
            #Verify it none in list(roadTable).
            if table not in roadTable:
                roadTable.append(table)
                #Stop the while loop.
                continuer = False

    return roadTable


def serviceTable(request):
    """service Table template, we display animation of the minimal road of a serveur."""

    #Call the backend from template.
    if request.method == "POST":

        #We choose 10 tables beetween 0 to 27 randomly
        roadTable = makeRandomCommands()
        #Choice randomly from roadTable a table in list.
        main = MainTableAssignation()
        #Create a picture with coordinates, number of table as circle.
        main.animationTable()
        #Recuperate randomly table from all 27 tables.
        #Generate a minimal road for bring plates to tables.
        roads = main.recuperateTable(roadTable)
        #Recuperate the instance animation of class.
        objectClass = main.getterObjectClassAnim()
        #Savegarde pictures of the trajects.
        myTable = main.animationRoad(roads, objectClass)

        #Return data of the navebarre.
        data = {"categoryPage": "Table dans la file: " + str(myTable),
                "navebarre":"Accueil", "naveBarreUrl":"/"}
        return render(request, pathTableService, data)

    #Return data of the navebarre.
    data = {"categoryPage": "Simulation",
            "categoryPage": "Délais", "navebarre":"Accueil", "naveBarreUrl":"/"}
    return render(request, pathTableService, data)




"""------------------------------------- DELAIS OF SERVICE ------------------------------------"""
def treatStrPost(infoData):
    """Receive str data so treat it"""

    #Delete some character of the String(data)
    command = filterProduct(infoData)
    #Split virgule.
    command = command.split(",")

    #List of command plate, delete first space.
    plates = [i[1:] if i[0] == " " else i for i in command]
    #Add "" if the user hasnt got 3 plates.
    for _ in range(3 - len(command)):
        plates.append("")

    return plates, command


def recuperatePictureLocation(plates):
    """Convert name of plate template to plate constante
    and their picture location"""

    #Récuperate picture of user plate.
    convertPlate = []
    for i in plates:
        if i != "":
            #Convert template name to constante name.
            convertPlate.append(treatNamePlate(i))
        else:
            convertPlate.append("")

    #Recuperate plate location url.
    for name, path in DICO_PRODUCT_LOCATION.items():
        if   convertPlate[0] == name: convertPlate[0] = path
        elif convertPlate[1] == name: convertPlate[1] = path
        elif convertPlate[2] == name: convertPlate[2] = path

    return convertPlate


def delaisApplication(menu):
    """estimate time of preparation of all command with
        simulate data"""

    #Delais application
    delais = Main()

    #Initialize random numbers workers.
    timeWorkCooker  = random.randrange(1, 10)
    timeWorkServeur = random.randrange(1, 8)
    lastPreparationTime = 0

    #Lunch delais programme.
    #Recuperate time total of waiting, command of user waiting and the
    #table assignation.
    timeDelais, commandTime, assignateTable = delais.generateDataSituation(
        lastPreparationTime, timeWorkCooker, timeWorkServeur, menu)

    #Recuperate all command plate.
    commandInCourse = delais.getterNbCommand()

    #Recuperate for the template the command plate and his time estimation.
    commands = [i[:3] + [j] for i, j in zip(commandInCourse, commandTime)]

    return timeDelais, assignateTable, commands

    
def regulationOfUserPlateCat(command):
    """User only can take entrance, plate, dessert"""

    #Régulation of user plate.
    commandDico = {"entrées": "", "plats":"", "desserts":""}
    #Recuperate for delais, sorted plate by category.
    for i in command:
        #Convert template name to constante name.
        treated = treatNamePlate(i)
        #Make a match of the category and the plate.
        for k, v in LIST_ITEMS_MENU.items():
            if treated in v:
                commandDico[k] = treated

    #Recuperate sorted menu plate by category.
    menu = [plate for _, plate in commandDico.items()]

    return menu


def attenteDelais(request):
    
    if request.method == "POST":

        #Recuperate data send from template
        infoData = request.POST.get('toDelaisApplication')

        #Treat data post receive.
        plates, command = treatStrPost(infoData)

        #Assign variables to plates list.
        plate1, plate2, plate3 = plates

        #Récuperate picture of user plate.
        convertPlate = recuperatePictureLocation(plates)

        #Remove plate in a same category, keep the last choice.
        menu = regulationOfUserPlateCat(command)

        #Application of time delais, recuperate
        #total command time, command user time, assignate table and all command details.
        timeDelais, assignateTable, commands = delaisApplication(menu)

        data = {"plate1": plate1, "plate2":plate2, "plate3":plate3,
                "locPlate1":convertPlate[0], "locPlate2":convertPlate[1], "locPlate3":convertPlate[2],
                "estimation": timeDelais, "commands":commands, "assignationTable":assignateTable,
                "categoryPage": "Délais", "navebarre":"Accueil", "naveBarreUrl":"/"}

        return render(request, pathDelais, data)


    #Application of time delais, recuperate
    #total command time, command user time, assignate table and all command details.
    timeDelais, assignateTable, commands = delaisApplication(None)

    data = {"categoryPage": "Délais", "navebarre":"Accueil", "naveBarreUrl":"/",
            "estimation": timeDelais, "commands":commands}
    return render(request, pathDelais, data)


"""------------------------------------- SELECTION OF PRODUCTS ------------------------------------"""
def recupData(postRequest):
    """infoData = visualization,
       infoProd = return to last page from visualisation
       infoPage = navigation of the selectionProduct1/2/3"""

    infoData = postRequest.get('jojo')
    infoProd = postRequest.get('products')
    infoPage = postRequest.get("page")

    return infoData, infoProd, infoPage


def filterProduct(pannier):
    """Filter product string with removing some character"""
    #Character to delete from the command of the user.
    character = ["&#x27", ']', '[', ';', '']
    #Replace character in the string to ''.
    for i in character:
        pannier = pannier.replace(i, '')
    return pannier


def desplitJs(pannier):
    """Split data by ',' and avoid space first letter"""

    filterPannier = []
    for i in pannier:
        #split ','
        splited = i.split(',')
        #Avoid space.
        for j in splited:
            if j not in ('', ' ', ','):
                if j[0] in ('', ' '):
                    filterPannier.append(j[1:])
                else:
                    filterPannier.append(j)

    return filterPannier



def constructDataDetails(infoData):
    """Treat data receive and send data of one tempalte to another one"""

    #Split '-' from data
    infoData, pannier = infoData.split("-")
    #Split '+' from data.
    infoData = infoData.split('+')
    #Delete indesirable characters.
    pannierFilter = filterProduct(pannier)

    #Data to send to the templates.
    data = {"lastPage":infoData[0], "picture": infoData[1], "name":infoData[2],
            "price":infoData[3], "info1":infoData[4], "info2":infoData[5],
            "info3":infoData[6], "products":pannierFilter}

    return data, infoData[2]



def suggestionToData(data, suggestion):
    """From apriory algorythm we have mutilples choice to 100%
    choice randomly 3 of them"""

    suggerate = [i for i in suggestion]

    randomChoice = []
    #Recuperate 3 suggerates plates.
    while len(randomChoice) < 3:
        rand = random.choice(suggerate)
        #Verigy suggestion isn't already present.
        if rand not in randomChoice and rand != "lasgne à la carbonara":
            randomChoice.append(rand)

    #Recuperate suggestion
    data["suggestion1"] = randomChoice[0]
    data["suggestion2"] = randomChoice[1]
    data["suggestion3"] = randomChoice[2]

    #Recuperate location url of picture.
    pictures = {"suggestion1":"", "suggestion2":"", "suggestion3":""}

    for k, v in DICO_PRODUCT_LOCATION.items():
        if randomChoice[0] == k:
            pictures["suggestion1"] = v
        elif randomChoice[1] == k:
            pictures["suggestion2"] = v
        elif randomChoice[2] == k:
            pictures["suggestion3"] = v

    #Add location to data.
    data["pictureSugg1"] = pictures["suggestion1"]
    data["pictureSugg2"] = pictures["suggestion2"]
    data["pictureSugg3"] = pictures["suggestion3"]

    return data




def suggestion(choice):
    """Use A priori algorythm"""

    #Create instance class.
    model = UseModelSuggestion()
    #Load all pairs from model.
    model.recuperateSuggestion()
    #Recuperate pairs.
    data = model.getterData()
    #Recuperate choice of plates.
    model.recuperateChoice(choice)
    #From choice of user, assign from data suggestion (better match)
    model.filterSuggestions()
    #Recuperate them
    suggestions = model.getterSuggestion()

    return suggestions


def treatNamePlate(choicePlate):
    """We transform name form template to name form model"""
    for nameTemplate, nameConstante in DICO_NAME_SITE_TO_MODEL.items():
        if nameTemplate == choicePlate:
            return nameConstante

    return choicePlate


def limitPlatEntranceDessert(productsFilter):
    """Here we choice to recuperate only one plate of each category
    so run command and put to false if we catch of category"""

    platAutorization = {"entrées": True, "plats": True, "desserts": True}
    productsCommand = []

    for product in productsFilter:
        #List template name to constante name
        for category, plates in LIST_ITEMS_MENU.items():
            #Transform template name to constante name
            transform = treatNamePlate(product)
            #Verify there are no 2 plates of same category in command
            if transform in plates:
                if platAutorization[category] is True:
                    platAutorization[category] = False
                    productsCommand.append(product)

    return productsCommand



def toVisualizeAndSuggestion(infoData):

    data, choicePlate = constructDataDetails(infoData)
    #Convert name template to name constante.
    choicePlate = treatNamePlate(choicePlate)
    #Call APriori algorythm.
    plateSuggestion = suggestion(choicePlate)
    #From all matching, generate 3 randoms plates matching.
    data = suggestionToData(data, plateSuggestion)
    #Load the template for visualisation and suggestion of products.
    template = loader.get_template(pathVisualisationProduct)

    return data, template


def visualisationToSelectionProd(infoProd):
    """Treat data receive and to send to another template"""
    #Split data '-'.
    infoProd, products = infoProd.split("-")
    #Split products '+'.
    productsSplit = infoProd.split("+")
    #Delete some character.
    products = filterProduct(products)
    #Re filter product, avoid splace and empty field.
    productsFilter = [i for i in productsSplit if i not in (' ', None, '', [])]
    #add product if isn't empty list.
    if productsFilter != []: productsFilter.append(products)
    #Split line ','
    productsFilter = desplitJs(productsFilter)
    #Limitation of category plate user.
    productsFilter = limitPlatEntranceDessert(productsFilter)
    return productsFilter



def selectionProduct1(request):
    """selection Products template"""

    if request.method == "POST":

        #Request post data 
        infoData, infoProd, infoPage = recupData(request.POST)
        if infoData is not None:
            """Go to visualisation product for add it and see suggestion"""
            #Selection product template to visualisation template.
            data, template = toVisualizeAndSuggestion(infoData)
            return HttpResponse(template.render(data, request))

        elif infoProd is not None:
            """Return to the plate selection recuperate choices of the visualisation template"""
            #visualisation template to Selection product template
            productsFilter = visualisationToSelectionProd(infoProd)
            data = {"products": productsFilter, "categoryPage": "Entrées",
                    "navebarre"    : "Home", "naveBarreUrl" : "/", "categoryPage" : "Entrées"}
            return render(request, pathSelectionProduct1, data)

        elif infoPage is not None:
            """Navigation to product selection from navebarre"""
            #Navigation from selection product to another.
            products = filterProduct(infoPage)
            data = {"products": [products], "navebarre" : "Home",
                    "naveBarreUrl" : "/", "categoryPage" : "Entrées"}
            return render(request, pathSelectionProduct1, data)


    data = {"navebarre":"Home", "naveBarreUrl":"/", "categoryPage":"Entrées"}
    return render(request, pathSelectionProduct1, data)




def selectionProduct2(request):
    """selection Products template"""

    if request.method == "POST":
    
        #Request post data 
        infoData, infoProd, infoPage = recupData(request.POST)

        if infoData != None:
            """Go to visualisation product for add it and see suggestion"""
            #Selection product template to visualisation template.
            data, template = toVisualizeAndSuggestion(infoData)
            return HttpResponse(template.render(data, request))

        elif infoProd != None:
            """Return to the plate selection recuperate choices of the visualisation template"""
            #visualisation template to Selection product template
            productsFilter = visualisationToSelectionProd(infoProd)
            data = {"products": productsFilter, "categoryPage": "Plat",
                    "navebarre"    : "Home","naveBarreUrl" : "/"}
            return render(request, pathSelectionProduct2, data)

        elif infoPage != None:
            """Navigation to product selection from navebarre"""
            #Navigation from selection product to another.
            products = filterProduct(infoPage)
            data = {"products": [products], "navebarre" : "Home","naveBarreUrl" : "/",
                    "categoryPage" : "Plats"}
            return render(request, pathSelectionProduct2, data)


            
    data = {"navebarre": "Home", "naveBarreUrl" : "/", "categoryPage" : "Plats"}
    return render(request, pathSelectionProduct2, data)




def selectionProduct3(request):
    """selection Products template"""

    category = "Déssert"

    if request.method == "POST":

        #Request post data 
        infoData, infoProd, infoPage = recupData(request.POST)

        if infoData != None:
            """Go to visualisation product for add it and see suggestion"""
            #Selection product template to visualisation template.
            data, template = toVisualizeAndSuggestion(infoData)
            return HttpResponse(template.render(data, request))

        elif infoProd != None:
            """Return to the plate selection recuperate choices of the visualisation template"""
            #visualisation template to Selection product template
            productsFilter = visualisationToSelectionProd(infoProd)
            data = {"products": productsFilter, "categoryPage": "Désserts"}
            return render(request, pathSelectionProduct3, data)

        elif infoPage != None:
            """Navigation to product selection from navebarre"""
            #Navigation from selection product to another.
            products = filterProduct(infoPage)
            data = {"products": [products]}
            return render(request, pathSelectionProduct3, data)

    return render(request, pathSelectionProduct3, {"categoryPage": "Désserts"})
