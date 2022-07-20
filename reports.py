#!/usr/bin/env python3

import os
from posixpath import split
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

desc_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/descriptions/'
desc_filelist = os.listdir(desc_path)

today = date.today().strftime('%B %d, %Y')
styles = getSampleStyleSheet()
report = SimpleDocTemplate('processed.pdf')
report_title = Paragraph(f' Processed Update on {today}', styles['h1'])

def generate_report(attachment, title, filelist):
    '''Generates processed.pdf report using the file list and file path'''
    fruits = {}
    fruit = ''
    table_data = []
    for textfile in filelist:
        file = attachment + textfile
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
    report_table = Table(data=table_data, hAlign='LEFT')
    report.build([title, report_table])
    return report_table

def main():
    generate_report(desc_path, report_title, desc_filelist)

if __name__ == '__main__':
    main()
