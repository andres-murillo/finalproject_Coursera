#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

desc_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/descriptions/'
desc_filelist = os.listdir(desc_path)

today = date.today().strftime('%B %d, %Y')
styles = getSampleStyleSheet()
report = SimpleDocTemplate('processed.pdf')
report_title = Paragraph(f'Processed Update on {today}', styles['h1'])

def items_weight(filelist, filepath):
    fruits = {}
    fruta = ''
    table_data = []
    for textfile in filelist:
        file = filepath + textfile
        keynumber = 0
        with open(file, 'r')  as f:
            for line in f.readlines():
                if keynumber <= 1:
                    if keynumber == 0:
                        fruta = line.strip()
                    else:
                        fruits[fruta] = line.strip()
                    keynumber += 1
    print(fruits)
    for k, v in fruits.items():
        name_fruit = 'name: ' + k
        weight_fruit = 'weight: ' + v
        table_data.append([name_fruit, weight_fruit])
    report_table = Table(data=table_data)
    return report_table

# def generate_report(attachment, title, paragraph):
#     pass

def main():
    # items_weight(desc_filelist, desc_path)
    reporte_tabla = items_weight(desc_filelist, desc_path)
    # print(reporte_tabla)
    report.build([report_title, reporte_tabla])

if __name__ == '__main__':
    main()
