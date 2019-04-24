import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)



@click.command()
@click.option('--scaffold_source', default='scaffolder', prompt='Scaffolding source', help = """Folder source that will be copied. The available folder sources are all under the "scaffolder" folder.""")
@click.option('--scaffold_config', default='config.yml', prompt='Scaffolding config', help = """Path to config file on how to process the scaffold files (yaml file).""")
@click.option('--scaffold_target', default='output', prompt='Scaffolding target', help = """Target folder to be copied from source folder after the renaming process is done""")
def custom(scaffold_source, scaffold_config, scaffold_target):
    print(scaffold_source)
    print(scaffold_config)
    print(scaffold_target)

if __name__ == '__main__':
    custom()