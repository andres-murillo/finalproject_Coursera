#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    '''Generates processed.pdf report using the file list and file path'''
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_table = Table(data=paragraph, hAlign='LEFT')
    report.build([report_title, report_table])
    # return report_table

# def main():
#     generate_report(desc_path, report_title, desc_filelist)

# if __name__ == '__main__':
#     main()
