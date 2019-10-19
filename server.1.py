# coding: utf-8

import socket
import xml.etree.ElementTree as ET
import time
import sqlite3
from pickle import TRUE

def creat_tab() :
    cursor = conn.cursor()
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS events(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         date_recep TEXT,
         heure_recep TEXT,
         serial TEXT,
         event_id INTEGER,
         account TEXT,
         code INTEGER,
         groupe INTEGER,
         zone INTEGER,
         num_event INTEGER,
         type_event TEXT
        )
        """)

'''
This widget script simply shows the current local IP address in a label.
'''
def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('google.com', 80))
		ip = s.getsockname()[0]
		s.close()
	except:
		ip = 'N/A'
	return ip


try:
    conn = sqlite3.connect('event.db')
    curseur = conn.cursor()
    creat_tab()
    conn.commit()
except sqlite3.OperationalError:
    print('Erreur la table existe déjà')
except Exception as e:
    print("Erreur")
    conn.rollback()
    # raise e
#finally:
#    conn.close()
      

server = get_local_ip()
print(server)
port = 1518

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except :
    socket.close()
    
socket.bind((server, port))

i = 1

while True:
        socket.listen(1)
        client, address = socket.accept()
        response = client.recv(512)
        if response != "":
                tree = ET.fromstring(response)
                for child in tree :
                    tree [0].iter('event')
                    tree [0][0][5].iter('event')
                    print ("Date:",time.strftime("%A %d %B %Y"), " | Heure:",time.strftime("%H:%M:%S"), " | event id :",tree[0].attrib["id"]," | serial number :", tree[0][0][0].text, " | account :", tree[0][0][1].text, " | code :" ,tree[0][0][2].text, " | groupe :",tree[0][0][3].text, " | zone:",tree[0][0][4].text, " | type:", tree[0][0][5].attrib["id"],"-",tree[0][0][5].attrib["type"])
                    print ("-" * 250)     
                    donnees = (time.strftime('%A %d %B %Y'), time.strftime('%H:%M:%S'), tree[0].attrib['id'], tree[0][0][0].text, tree[0][0][1].text, tree[0][0][2].text, tree[0][0][3].text, tree[0][0][4].text, tree[0][0][5].attrib['id'], tree[0][0][5].attrib['type'])
                    curseur.execute( """
                            INSERT INTO events (date_recep, heure_recep, serial, event_id, account, code, groupe, zone, num_event, type_event) 
                            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
                            """, donnees)
                    conn.commit()
                i += 1
client.close()
socket.close()
conn.close()
print("Close")
