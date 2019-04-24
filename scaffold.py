import click
import yaml
import os
from pathlib import Path
from shutil import copyfile
import errno

class Document:

    def __init__(self, file_src_path, file_dest_path, document_dict):
        self.file_src_path = file_src_path
        self.file_dest_path = file_dest_path
        self.document_dict = document_dict
        self.new_file_name = self.document_dict.get("rename_file", False)

        print("init class Document")
        print('source file:', self.file_src_path)
        print('destination file:', self.file_dest_path)
        print(self.document_dict)
        # print(self.new_file_name)

    def process(self):
        # process keywords recursively
        # change file name
        # save file to dest

        self.save_file()
        return

        keywords_dict = self.document_dict.get("keywords", {})

    def save_file(self, stream = None):
        if self.new_file_name:
            save_path = self.file_dest_path.parent / self.new_file_name
            # if no extension given, it will add the extension
            if save_path.suffix != self.file_src_path.suffix:
                save_path = Path(str(save_path) + self.file_src_path.suffix)
        else:
            save_path = self.file_dest_path

        # make sure that directory is exist
        if not self.file_dest_path.exists():
            try:
                os.makedirs(os.path.dirname(self.file_dest_path))
                # file_dest_path.mkdir(file_dest_path.parent, exist_ok=True)
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # todo: open and write stream
        if stream:
            with open(save_path, 'w') as output_file:
                output_file.write(stream)
        else:
            copyfile(self.file_src_path, save_path)

        print("saving file: {}".format(save_path))

class Keyword:
    def __init__(self, keyword_dict):
        self.keyword_dict = keyword_dict

    def process(self):

        for k, v in self.keyword_dict.items():
            print(k, v)
            if isinstance(v, str):
                print("string")
            elif isinstance(v, dict):
                print("dict")


        pass

    def recursive(self):
        pass

    pass


# @click.command()
# @click.option('--scaffold_source', default='default_folder', prompt='Scaffolding source', help = """Folder source that will be copied. The available folder sources are all under the "scaffolder" folder.""")
# @click.option('--scaffold_config', default='config.yml', prompt='Scaffolding config', help = """Path to config file on how to process the scaffold files (yaml file).""")
# @click.option('--scaffold_target', default='output', prompt='Scaffolding target', help = """Target folder to be copied from source folder after the renaming process is done""")

def custom(scaffold_source, scaffold_config, scaffold_target):
    # todo: path is exist?

    # init
    scaffold_source_root = Path('scaffolder', scaffold_source)
    scaffold_config_root = Path(scaffold_config)
    scaffold_dest_root = Path(scaffold_target)

    # reading yaml config
    yaml_dict = yaml.load(open(scaffold_config))

    """
    logic
    
    for each key (file):
        get if it is renamed or not. if yes, save
        parse the keywords key into recursive function
            the recursive function will handle all the replacing stream, and returned.
    
    """

    for key in yaml_dict.keys():
        template_path = scaffold_source_root / key

        if template_path.exists():
            document = Document(file_src_path= scaffold_source_root / key,
                                file_dest_path= scaffold_dest_root / key,
                                document_dict=yaml_dict[key])
            document.process()
        else:
            print("file not found: {}".format(template_path))
            continue

        print()



# if __name__ == '__main__':
#     custom()

custom('default_folder', 'config.yml', 'output/to_here')