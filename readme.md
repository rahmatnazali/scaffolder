# Python scaffolder

(this doc is work in progress)

- requirements: [requirements_01](assets/requirements_01)

##### Todo:
  - finish the doc
  - **[DONE]** Test with my own case and YAML config
  - Test with client's case of YAML config
  - my question to client
    - do you have any scaffolding example or case that suits to this testing?
    
##### Usage
```
$ python3 scaffold.py --help
Usage: scaffold.py [OPTIONS]

  Scaffold a given directory recursively to any specified directory with
  predefined YAML config.

Options:
  --scaffold_source TEXT  Folder source that will be copied. The available
                          folder sources are all under the "scaffolder"
                          folder.
  --scaffold_config TEXT  Path to YAML config file.
  --scaffold_target TEXT  Destination folder to be copied to from source
                          folder after the renaming process is done
  -v                      Verbose mode: will print each content change/replace
  --help                  Show this message and exit.

```

##### Verbose mode
![](assets/verbose_mode_on.png)

##### without Verbose mode
![](assets/verbose_mode_off.png)


