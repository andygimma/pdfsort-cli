import click

from rotate_all import rotate_all as rotate_function

@click.group(invoke_without_command=False)
@click.pass_context
def cli(ctx):
    click.echo('Thank you for using pdfsort %s' % ctx.invoked_subcommand)

@cli.command()
@click.option('--degrees', default=180, help='degrees to rotate by')
@click.argument('input_pdf')
@click.argument('output_pdf')
def rotate_all(input_pdf, output_pdf, degrees):
    print input_pdf, output_pdf, degrees
    rotate_function(input_pdf, output_pdf, degrees)
