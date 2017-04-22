import click
import subprocess
import os

def split_scripts(pdf, first_page, last_page, outputpdf):
    bashCommand = "pdfjam " + pdf + " '" + str(first_page) + "-" + str(last_page) + "'" + " --outfile " + outputpdf
    subprocess.call(['bash','-c', bashCommand], stdout=open(os.devnull, 'wb'))
    string = "Creating " + outputpdf
    click.secho(string, fg='blue')


def loop_scripts(pdf, start_page, total_pages, increment, outputpdf):
    current_page = start_page
    for index in range(start_page, total_pages+1):
        if (current_page < total_pages):
            pdfName = str(index) + "-" + outputpdf
            last_page = current_page + increment - 1
            if last_page > total_pages:
                last_page = total_pages
            split_scripts(pdf, current_page, last_page, pdfName)
            current_page = current_page + increment
