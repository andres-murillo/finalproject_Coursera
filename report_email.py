#!/usr/bin/env python3

import os 
from datetime import date
import reports

desc_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/descriptions/'
desc_filelist = os.listdir(desc_path)
today = date.today().strftime('%B %d, %Y')
title =  (f' Processed Update on {today}')
attachment = '/home/amurillo/workspace/finalproject_Coursera/processed.pdf'

def generate_paragraph(filelist, files_path):
    fruits = {}
    fruit = ''
    table_data = []
    for textfile in filelist:
        file = files_path + textfile
        keynumber = 0
        with open(file, 'r')  as f:
            for line in f.readlines():
                if keynumber <= 1:
                    if keynumber == 0:
                        fruit = line.strip()
                    else:
                        fruits[fruit] = line.strip()
                    keynumber += 1
    for k, v in fruits.items():
        name_fruit = 'name: ' + k + '\n'
        weight_fruit = 'weight: ' + v
        fruit_complete = name_fruit + weight_fruit
        separator = '\n'
        table_data.append([fruit_complete, separator])
    return table_data

def main():
    paragraph = generate_paragraph(desc_filelist, desc_path)
    reports.generate_report(attachment, title, paragraph)

if __name__ == '__main__':
    main()
