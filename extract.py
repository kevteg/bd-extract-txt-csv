#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Author: Keeeevin
'''
import argparse
import csv
from datetime import datetime
from difflib import SequenceMatcher
class extract():
    def __init__(self, filename):
        # try:
            with open(filename, "r", encoding = 'utf-8') as _file:
                lines = _file.readlines()
                self.processFile(lines)
        # except Exception as e:
        #     print("Error: ")
        #     print(e)

    def processFile(self, lines):
        dicti = {}
        name = {}
        lon = 0
        for index, l  in enumerate(lines, start = 0):
            if len(l) > 2:
                lon = lon + 1
                a = l.split('	')
                for i, e in enumerate(a):
                    if not index:
                        name[i] = e.replace("\n", "")
                        dicti[name[i]] = []
                    else:
                        dicti[name[i]].append(e.replace("\n", ""))
        # for i in names.keys():
        #     field = str(names[i])
        #     for e in dicti[names[i]]:
        #         writer.writerow({field: e})
        self.createCSV(dicti, name, lon)


    def createCSV(self, dicti, names, lon):
        with open('data1.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=names.values())
            writer.writeheader()
            all_lines = []
            diff = {}
            for index in range(0, lon - 1):
                test = {}
                p = {}
                for i in names.keys():
                    string_to_add = dicti[names[i]][index].replace('.', '').lower()
                    add = True
                    try:
                        if string_to_add not in diff[str(names[i])] and i > 1 and i < 6:
                            for similar_string in diff[str(names[i])]:
                                if self.similar(similar_string, string_to_add) > 0.85:
                                    add = False
                                    # print(string_to_add + " parecido a " + similar_string)
                                    string_to_add = similar_string
                            if add:
                                diff[str(names[i])].append(string_to_add)
                    except:
                        diff[str(names[i])] = []

                    test[(names[i])] = string_to_add
                    if i < 7:
                        p[(names[i])] = string_to_add
                try:
                    date = (test[names[0]]).replace('\x00', '')
                    datetime.strptime(date, "%d/%m/%Y")
                    if p not in all_lines:
                        # print(test)
                        all_lines.append(p)
                        writer.writerow(test)
                    else:
                        print("Línea repetida:")
                except Exception as e:
                    print("Esa fecha está mal. Razón:")
                    print(e)

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()



parser = argparse.ArgumentParser(prog='extract', usage='%(prog)s [options]',description='Script to extract data from a txt file to csv')
parser.add_argument('-f','--file', required =True, dest='file',type=str, help='File to read')

args = parser.parse_args()
ext = extract(args.file)
