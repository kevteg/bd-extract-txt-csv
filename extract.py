#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
    Author: Keeeevin
'''
import argparse
class extract():
    def __init__(self, filename):
        try:
            with open(filename, "r", encoding='latin-1') as _file:
                lines = _file.readlines()
                self.processFile(lines)
        except Exception as e:
            print("Error: ")
            print(e)

    def processFile(self, lines):
        # data = 'hola como '
        for index, l  in enumerate(lines):
            print(str(l))
            a = l.split('	')

            #Hay lineas en blanco
            for i, e in enumerate(a):
                print("Line " + str(i) + ": ")
                print(e)

            if index == 2:
                break
            # print(str(l).split(" ")[3])



parser = argparse.ArgumentParser(prog='extract', usage='%(prog)s [options]',description='Script to extract data from a txt file to csv')
parser.add_argument('-f','--file', required =True, dest='file',type=str, help='File to read')

args = parser.parse_args()
ext = extract(args.file)
