#!/usr/bin/env python
# -*-coding: utf-8 -*

"""----------------------- IMPORTATIONS -----------------------"""
import os
PATHDIR = os.path.dirname(os.path.abspath(__file__))


"""----------------------- CONSTANTES -----------------------"""

#path of csv list items.
PATH_CSV = PATHDIR + "/csvProduct/csvChoicesMenu.csv"
#path of csv list items.
PATH_CSV_MODEL = PATHDIR + "/model/model.csv"

#list items.
LIST_ITEMS_MENU = {
    "entrées":[
        "oeufs mimosa", "salade de tomate", "tartines", "quiche", "olive", "cacahuette","None",
    ],
    "plats":[
        "steack fritte", "hamburger fritte", "lasgne à la carbonara", "None","pizza", "kebab", "tacos", "lasagne a la carbonara", "lasagne",
    ],
    "desserts":[
        "ile flottante", "glace", "mousse framboise", "None","granitas", "crepe", "gauffre au nutelat",
    ],
}
#List of plate separatly
LIST_ITEMS = [
    "oeufs mimosa", "salade de tomate", "tartines", "pizza", "kebab", "tacos",
    "steack fritte", "hamburger fritte", "lasgne à la carbonara",
    "ile flottante", "glace", "mousse framboise", "quiche", "olive", "cacahuette",
    "lasagne a la carbonara", "lasagne", "granitas", "crepe", "gauffre au nutelat", 
]
