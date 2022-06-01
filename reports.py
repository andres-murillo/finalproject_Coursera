#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

desc_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/descriptions/'
desc_filelist = os.listdir(desc_path)

today = date.today().strftime('%B %d, %Y')
styles = getSampleStyleSheet()
report = SimpleDocTemplate('processed.pdf')
report_title = Paragraph(f'Processed Update on {today}', styles['h1'])

items = {'name': '', 'weight': ''}

def items_weight(filelist, filepath):
    for textfile in filelist:
        


def generate_report(attachment, title, paragraph):
    pass
