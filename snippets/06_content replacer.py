# import massedit
# import re
#
# filenames = [
#     'sandbox/base_class.php'
# ]
# massedit.edit_files(filenames, ["re.sub('_REPLACE_CLASS_NAME_', 'Animal.', line)"])


from pathlib import Path

a_string = """
    one = 1
    two = 2
    three = 3
    
    def func():
        for i in range(10):
            pass
            break
        
"""


stream = open('sandbox/base_class.php').read()
stream = stream.replace('_REPLACE_CLASS_NAME_', 'Animal')
stream = stream.replace('_REPLACE_CLASS_CONTENT_', a_string)

o = open(Path('sandbox', 'output.php'), 'w')
o.write(stream)
o.close()
