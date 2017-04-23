import click
import time
import PyPDF2
import subprocess

from rotate_all import rotate_all as rotate_function
from generate_new_pdf import generate_new_pdf
from rotate_pages_by_degrees import rotate_pages_by_degrees
from split import loop_scripts

@click.group(invoke_without_command=False)
@click.pass_context
def cli(ctx):
    click.echo('Thank you for using pdfsort %s' % ctx.invoked_subcommand)

@cli.command()
@click.option('--degrees', default=180, help='degrees to rotate by')
@click.argument('input_pdf')
@click.argument('output_pdf')
def rotate_all(input_pdf, output_pdf, degrees):
    time1 = time.time()
    description = "Rotating " + input_pdf + " by " + str(degrees) + " degrees"
    click.secho(description, fg='green')
    rotate_function(input_pdf, output_pdf, degrees)
    click.secho("Created: " + output_pdf, fg='green')
    time2 = time.time()
    time_string = '%0.3f seconds' % ((time2-time1))
    click.secho(time_string, fg='green')

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
@click.argument('pages_list')
def generate(input_pdf, output_pdf, pages_list):
    print "GENERATE"
    time1 = time.time()
    description = "Creating " + output_pdf + " from " + input_pdf + " pages " + pages_list
    click.secho(description, fg='green')

    generate_new_pdf(input_pdf, pages_list, output_pdf)

    click.secho("Created: " + output_pdf, fg='green')
    time2 = time.time()
    time_string = '%0.3f seconds' % ((time2-time1))
    click.secho(time_string, fg='green')

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
@click.argument('pages_list')
@click.argument('degrees')
def rotate_pages(input_pdf, output_pdf, pages_list, degrees):
    time1 = time.time()
    description = "Rotating pages " + pages_list + " " + degrees + " from " + input_pdf + " to " + output_pdf
    click.secho(description, fg='green')

    rotate_pages_by_degrees(input_pdf, pages_list, output_pdf, int(degrees))

    click.secho("Created: " + output_pdf, fg='green')
    time2 = time.time()
    time_string = '%0.3f seconds' % ((time2-time1))
    time_string = "Finished: " + time_string
    click.secho(time_string, fg='green')

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
@click.argument('first_page')
@click.argument('last_page')
@click.argument('increment')
def split(input_pdf, output_pdf, first_page, last_page, increment):
    time1 = time.time()
    description = "Splitting " + input_pdf
    click.secho(description, fg='green')

    loop_scripts(input_pdf, int(first_page), int(last_page), int(increment), output_pdf)

    time2 = time.time()
    time_string = '%0.3f seconds' % ((time2-time1))
    time_string = "Finished: " + time_string
    click.secho(time_string, fg='green')

#pdfsort kedsort --input file.pdf --trackers 1,2,3 --sign_in 24,25,26 --canvass 4-23 --increment 4

@cli.command()
@click.argument('input_pdf')
@click.option('--tracker_pages')
@click.option('--sign_in_pages')
@click.option('--canvass_pages')
@click.option('--increment')

def kedsort(input_pdf, tracker_pages, sign_in_pages, canvass_pages, increment):
    if tracker_pages:
        tracker_pdf = input_pdf.replace(" ", "").replace(".pdf", "") + "-tracker.pdf"
        bashCommand = "pdfsort generate " + input_pdf + " " + tracker_pdf + " " + tracker_pages
        subprocess.call(['bash','-c', bashCommand])

    if sign_in_pages:
        sign_in_pdf = input_pdf.replace(" ", "").replace(".pdf", "") + "-sign_in.pdf"
        bashCommand = "pdfsort generate " + input_pdf + " " + sign_in_pdf + " " + sign_in_pages
        subprocess.call(['bash','-c', bashCommand])

    if canvass_pages:
        canvass_pdf = input_pdf.replace(" ", "").replace(".pdf", "") + "-canvass.pdf"
        bashCommand = "pdfsort generate " + input_pdf + " " + canvass_pdf + " " + canvass_pages
        subprocess.call(['bash','-c', bashCommand])

        if increment:
            total_pages = PyPDF2.PdfFileReader(canvass_pdf, False).getNumPages()
            bashCommand = "pdfsort split " + canvass_pdf + " " + canvass_pdf + " 1 " + str(total_pages) + " " + str(increment)
            subprocess.call(['bash','-c', bashCommand])
