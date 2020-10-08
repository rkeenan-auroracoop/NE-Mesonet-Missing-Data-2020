import pandas as pd
from openpyxl import load_workbook
from string import Template
import numpy as np
from csv import reader
import xlrd
import os
import datetime
from fuzzywuzzy import fuzz

locationDictionary = {"Ainsworth 2NE": "Ainsworth 2NE (AKA Ainsworth)", 'Alda 3W': 'Alda 3W (AKA Grand Island)', 'Alliance 6NW': 'Alliance 6NW (AKA Alliance North)', 'Arthur 8S': 'Arthur 8S', 'Axtell 5NE': 'Axtell 5NE (AKA Minden)', 'Big Springs 8NE': 'Big Springs 8NE (AKA Brule North Table)', 'Broadwater 7N': 'Broadwater 7N', 'Brule 6SW': 'Brule 6SW (AKA Brule Platte Valley)', 'Central City 3W': 'Central City 3W (AKA Central City Airport)', 'Champion 5SE': 'Champion 5SE (AKA Champion)', 'Concord 2E': 'Concord 2E (AKA Concord)', 'Cozad 8N': 'Cozad 8N (AKA Cozad)', 'Curtis 1N': 'Curtis 1N (AKA Curtis Agriculture Station)', 'Decatur 7S': 'Decatur 7S', 'Dickens 1NE': 'Dickens 1NE', 'Dunning 6NW': 'Dunning 6NW (AKA Halsey)', 'Eagle 3NW Beta': 'Eagle 3NW Beta (AKA Rogers Farm Tower)', 'Elgin 6W': 'Elgin 6W (AKA Elgin)', 'Emmet 2E': "Emmet 2E (AKA O'Neill)", 'Firth 3N': 'Firth 3N (AKA Firth)', 'Fordyce 4N': 'Fordyce 4N (AKA Chalkrock)', 'Gordon 4SE': 'Gordon 4SE (AKA Gordon)', 'Gothenburg 2NW': 'Gothenburg 2NW (AKA Gothenburg)', 'Grant 1E': 'Grant 1E', 'Guide Rock 3E': 'Guide Rock 3E (AKA Red Cloud)', 'Harrison 4NW': 'Harrison 4NW', 'Harvard 4SW': 'Harvard 4SW (AKA Clay Center)', 'Hayes Center 3N': 'Hayes Center 3N', 'Holdrege 5N': 'Holdrege 5N (AKA Holdrege 4N)', 'Indianola 8SW': 'Indianola 8SW', 'Kearney 3E': 'Kearney 3E (AKA Kearney)', 'Keystone 4W': 'Keystone 4W', 'Leigh 1W': 'Leigh 1W', 'Lexington 4S': 'Lexington 4S (AKA Lexington 3S)', 'Lincoln 1500 N 45th':
                      'Lincoln 1500 N 45th (AKA Lincoln IANR)', 'Lincoln 1700 N 10th': 'Lincoln 1700 N 10th (AKA Lincoln 10th and Military Road)', 'Lincoln 5700 S 27th': 'Lincoln 5700 S 27th (AKA Lincoln 27th and Old Cheney Road)', 'Lincoln 9100 S 78th': 'Lincoln 9100 S 78th', 'Long Pine 20S': 'Long Pine 20S (AKA Barta)', 'Memphis 4N': 'Memphis 4N', 'Memphis 5N': 'Memphis 5N (AKA Mead Agronomy Farm)', 'Merna 2SW': 'Merna 2SW (AKA Merna)', 'Mullen 30N': 'Mullen 30N (AKA Merritt)', 'Naper 12SW': 'Naper 12SW(AKA Higgins Ranch)', 'Nebraska City 3NW': 'Nebraska City 3NW(AKA Nebraska City 2N)', 'North Platte 3SW Beta': 'North Platte 3SW Beta', 'Oakland 4W': 'Oakland 4W(AKA Oakland)', 'Ord 2N': 'Ord 2N(AKA Ord)', 'Oshkosh 6N': 'Oshkosh 6N', 'Overton 6SE': 'Overton 6SE', 'Pierce 2SW': 'Pierce 2SW', 'Plattsmouth 2SE': 'Plattsmouth 2SE', 'Plymouth 4E': 'Plymouth 4E(AKA Beatrice)', 'Ragan 5W': 'Ragan 5W(AKA Holdrege)', 'Rulo 5SW': 'Rulo 5SW', 'Scottsbluff 2NW': 'Scottsbluff 2NW(AKA Scottsbluff)', 'Scottsbluff 6NW': 'Scottsbluff 6NW(AKA Mitchell Farms)', 'Shelton 2SW': 'Shelton 2SW(AKA Shelton)', 'Sidney 2NW': 'Sidney 2NW(AKA Sidney)', 'Smithfield 2E': 'Smithfield 2E(AKA Smithfield)', 'Sparks 5NE': 'Sparks 5NE(AKA Sparks)', 'Walton 5NW': 'Walton 5NW(AKA Havelock)', 'West Point 2W': 'West Point 2W(AKA West Point)', 'Whitman 5NE': 'Whitman 5NE(AKA Gudmundsen Sandhills Laboratory)', 'Winslow 6E': 'Winslow 6E', 'Wood River 5SE': 'Wood River 5SE(AKA Binfield)', 'York 2W': 'York 2W(AKA York)'}

testDictionary = {"Ainsworth 2NE": "Ainsworth 2NE (AKA Ainsworth)"}

thisList = ['Ainsworth 2NE']


for key, value in testDictionary.items():
    # print(key)
    # print(value)
    for item in thisList:
        Ratio = fuzz.ratio(item.lower(), key.lower())
        # Ratio2 = fuzz.ratio(item.lower(), value.lower())
        print(Ratio)
        if Ratio > 80:
            item = value
            print(value)
            break
        else:
            print('not a match')
