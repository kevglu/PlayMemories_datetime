# PlayMemories Datetime

Renames folders in a root folder if those folders match the German datetime format "DD.MM.YYYY". German version of Sony's Play Memories Home automatically creates this folder structure, a feature not beloved by its users.

This small programm renames these folders to "YYYYMMDD" or another format, the user can specify.

![PyPI version](https://img.shields.io/pypi/v/PlayMemories_datetime.svg)
[![Documentation Status](https://readthedocs.org/projects/PlayMemories_datetime/badge/?version=latest)](https://PlayMemories_datetime.readthedocs.io/en/latest/?version=latest)

Convert (German) Sony Playmemorie folders to sensible format.

* PyPI package: https://pypi.org/project/PlayMemories_datetime/
* Free software: MIT License
<!-- * Documentation: https://PlayMemories_datetime.readthedocs.io. -->

## How to run:

Root folder is specified by option ```-r [folder]``` or ```--root [folder] ``` 

Calling Entry point With uv:
```
uv run pm_dt -r "C:/Pictures" 
```

Alternative name format can be specified with --format option
```
uv run pm_dt -r "C:/Pictures" --format "pictures_%Y%-m%-%d"
```

## ToDO:
- set up new uv lock file (current one is over-full)

## Features

* TODO

## Mass convert RAW to img
- activate the virtual env in terminal:
```raw-to-img-venv\Scripts\activate```
- toinstall raw image converter ```pip3 install raw_image_converter```
- 

## Credits

This package was created with [Cookiecutter](https://github.com/audreyfeldroy/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
