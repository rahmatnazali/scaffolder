import click
import os

# @click.command()
# @click.option('--scaffold_source', default='default_folder', prompt='Scaffolding source', help = """Folder source that will be copied. The available folder sources are all under the "scaffolder" folder.""")
# @click.option('--scaffold_config', default='config.yml', prompt='Scaffolding config', help = """Path to config file on how to process the scaffold files (yaml file).""")
# @click.option('--scaffold_target', default='output', prompt='Scaffolding target', help = """Target folder to be copied from source folder after the renaming process is done""")
def custom(scaffold_source, scaffold_config, scaffold_target):

    # todo: source should target foldername inside scaffolder folder
    print(os.path.join('scaffolder', scaffold_source))
    print(scaffold_config)
    print(scaffold_target)

# if __name__ == '__main__':
#     custom()

custom('default_folder', 'config.yml', 'output')