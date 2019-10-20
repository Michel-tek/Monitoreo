#! /usr/bin/env python3
# coding: utf-8
'''
@author: michel Pappalardo
prenom : michel
Created on : 14/10/2019
fonction du programme : lire les donnees dans une base de donnees sqlite3

'''
__version__ = '1.0'

'''
import des librairies

import pdb; pdb.set_trace() permet d'afficher une console pour debuger les variables 

import logging as lg --- librairie permettant de gerer les niveaux d'affichage de message d'erreur 

lg.basicConfig(level=lg.DEBUG) permet d'afficher le niveau d'alarme a afficher

	DEBUG : Informations détaillées dans le but d'en savoir plus sur l'exécution d'une instruction.
	INFO : Information sur le déroulement d'un programme.
	WARNING : Quelque chose d'inattendue s'est produit mais le programme continue de fonctionner.
	ERROR : A cause d'un problème important, le programme n'a pu réaliser une tâche.
	CRITICAL : Problème très sérieux qui a pu causer l'arrêt du programme.
	
	utiliser lg.warning() ou lg.error() a la place d'un print d'information a destination du developpeur
	ex ; lg.warning('attention le programme est arrete')
'''
import logging as lg
import sqlite3
import sound


lg.basicConfig(level=lg.INFO)
	
if __name__ == "__main__":
    lg.info('script interprété en tant que programe principal')
else:
    lg.info('script importé depuis un autre programe')



precd = 0
conn = sqlite3.connect('event.db')
cursor = conn.cursor()
lg.debug("valeur de la variable cursor',cursor)
cpt = 0

#cursor.execute("""SELECT * FROM events""")
#for row in cursor:
#    print('{0} : {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10}'.format(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
#    if row[9] == 20:
#        print ("appeler client")

while True:
    cursor.execute("""SELECT * FROM events GROUP BY date_recep HAVING id = MAX(id)""")
    cpt += 1
    for row in cursor:
        if row[0] != precd :
            print('{0} : {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10}'.format(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
            precd = row[0]
            lg.debug("row[9]',row[9])
            if row[9] == 4:
            	lg.info('appeler le client')
                print ("appeler client")
                sound.play_effect('drums:Drums_06')
                
conn.close()
