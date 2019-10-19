# coding: utf-8

import sqlite3
import sound

precd = 0
conn = sqlite3.connect('event.db')
cursor = conn.cursor()
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
            if row[9] == 4:
                print ("appeler client")
                sound.play_effect('drums:Drums_06')
                
conn.close()
