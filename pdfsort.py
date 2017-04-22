import click
import time

from rotate_all import rotate_all as rotate_function
from generate_new_pdf import generate_new_pdf
from rotate_pages_by_degrees import rotate_pages_by_degrees

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
