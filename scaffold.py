import click
import yaml
import os
from pathlib import Path
from shutil import copyfile
import errno

verbose_mode = True

class Document:
    """
    Class to contains a single scaffolding file
    """
    def __init__(self, file_src_path, file_dest_path, document_dict):
        """
        :param file_src_path: pathlib.Path() to source file path
        :param file_dest_path: pathlib.Path() to destination file path
        :param document_dict: yaml config dictiinary
        """
        self.file_src_path = file_src_path
        self.file_dest_path = file_dest_path
        self.document_dict = document_dict
        self.new_file_name = self.document_dict.get("rename_file", False)

        if self.new_file_name:
            save_path = self.file_dest_path.parent / self.new_file_name
            # if no extension given, it will add the extension
            if save_path.suffix != self.file_src_path.suffix:
                self.save_path = Path(str(save_path) + self.file_src_path.suffix)
        else:
            self.save_path = self.file_dest_path

        # make sure that directory is exist
        if not self.file_dest_path.exists():
            try:
                os.makedirs(os.path.dirname(self.file_dest_path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        print("Scaffolding    : {} --> {}".format(self.file_src_path, self.save_path))

    def process(self):
        """
        Code to call several smaller code:
            - process keywords recursively
            - change file name
            - save file to dest
        """

        # recursively process keywords
        keywords_dict = self.document_dict.get("keywords", {})
        original_stream = processed_stream = open(self.file_src_path).read()

        # process replacement according to the configuration
        processed_stream = self.process_keyword(keywords_dict, processed_stream)

        # save file
        if processed_stream != original_stream:
            self.save_file(processed_stream)
        else:
            self.save_file()

        if verbose_mode:
            print()


    def process_keyword(self, sub_dictionary, stream):
        """
        Recursively process a keyword dictionnary
        :param sub_dictionary:
        :param stream:
        :return:
        """

        for key, value in sub_dictionary.items():
            # print(key, value)
            if isinstance(value, str):
                stream = stream.replace(key, value)
                if verbose_mode: print('\tchange', key, 'to', value[:15], '...')
            elif isinstance(value, dict):
                # process the child keywords first
                template_path = value.get('file', '')
                keyword_dict = value.get('keywords', {})

                if not template_path:
                    print("\tno 'file' key found on YML, skipping {}.".format(key))
                    return stream

                template_path = Path(template_path)

                if not template_path.exists():
                    print("File not found : {}".format(str(template_path)))
                    return stream

                with open(template_path) as template_file:
                    original_stream = template_file.read()

                processed_stream = self.process_keyword(keyword_dict, original_stream)

                if processed_stream != original_stream:
                    stream = stream.replace(key, processed_stream.lstrip())
        return stream

    def save_file(self, stream = None):
        """
        Open a file according to the save path and write the stream (if given)
        :param stream: string stream to be written
        """
        if stream:
            with open(self.save_path, 'w') as output_file:
                output_file.write(stream)
        else:
            copyfile(self.file_src_path, self.save_path)

        if verbose_mode: print("\tsaving file: {}".format(self.save_path))




"""
Main scaffold code goes here
"""

@click.command()
@click.option('--scaffold_source', default='default_folder', prompt='Scaffolding source', help = """Folder source that will be copied. The available folder sources are all under the "scaffolder" folder.""")
@click.option('--scaffold_config', default='config.yml', prompt='Scaffolding config', help = """Path to YAML config file.""")
@click.option('--scaffold_target', default='output', prompt='Scaffolding target', help = """Destination folder to be copied to from source folder after the renaming process is done""")
@click.option('-v', count=True, help = """Verbose mode: will print each content change/replace""")

def scaffold(scaffold_source, scaffold_config, scaffold_target, v):
    """
    Scaffold a given directory recursively to any specified directory with predefined YAML config.
    """
    global verbose_mode
    verbose_mode = bool(v)

    # init several filepath
    scaffold_source_root = Path('scaffolder', scaffold_source)
    scaffold_config_root = Path(scaffold_config)
    scaffold_dest_root = Path(scaffold_target)

    # reading yaml config
    yaml_dict = yaml.load(open(scaffold_config_root))

    """
    Logic:
    for each yaml key (file):
        get if it is renamed or not. if yes, rename it
        parse the keywords key into recursive function
            start of recursive function:
                if config value is string (mean only replace):
                    replace accordingly
                    return the current processed stream
                else:
                    call this function and pass the current stream and the lower level of the config
        save the file    
    """
    print()
    for key in yaml_dict.keys():
        template_path = scaffold_source_root / key

        if template_path.exists():
            document = Document(file_src_path= scaffold_source_root / key,
                                file_dest_path= scaffold_dest_root / key,
                                document_dict=yaml_dict[key])
            document.process()
        else:
            print("file not found : {}".format(template_path))
            if verbose_mode: print()
            continue

scaffold()

# todo: write unit test
