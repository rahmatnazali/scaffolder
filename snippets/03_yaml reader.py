import yaml


yaml_default_string= """
cars:
    car0:
        type: toyota
        hp: 129
        mpg:
            city: 30
            highway: 35
        cost: 15,000
    car1:
        type: gm
        hp: 225
        mpg:
            city: 20
            highway: 25
        cost: 20,000
    car2:
        type: chevy
        hp: 220
        mpg:
            city: 22
            highway: 24
        cost: 21,000
"""

yaml_string = """
base_class.php:
  keywords:
    _REPLACE_CLASS_NAME_: testing
    _REPLACE_CLASS_CONTENT_:
      file: template/content_file.php
      keywords:
        _KEYWORD_X_: "$value"

sub/other_base_class.php:
  keywords:
    _REPLACE_CLASS_NAME_: testing

"""



f = open('../config.yml')

# a_dict = yaml.load(yaml_string)
a_dict = yaml.load(f)

print(a_dict)
print(a_dict.keys())


# to dump
print(yaml.dump(a_dict))