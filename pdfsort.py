import click

@click.group(invoke_without_command=False)
@click.pass_context
def cli(ctx):
    click.echo('Thank you for using pdfsort %s' % ctx.invoked_subcommand)

@cli.command()
@click.argument('name')
def sync(name):
    # click.echo('The subcommand')
    click.echo(name)
    # click.secho('I am green!', fg='green')
    # click.secho('Some more text', bg='blue', fg='white')
    # click.secho('ATTENTION', blink=True, bold=True)
