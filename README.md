# Automated Playlist

## Overview

This command line application runs automatically a playlist depending on the current day date.
The user can choose on which platform (Spotify, YouTube or Soudcloud) the music is playing on.
This application uses the Chrome browser to open the platform Soundcloud and Spotify.

## Technologies

* Python - version 3.8.3
* selenium - version 3.141.0
* urllib3 - version 1.26.4
* webdriver-manager - version 3.3.0
* Chrome driver - version 89.0.4389
* Chrome Broswer

## Setup

Use the [pip](https://pip.pypa.io/en/stable/) package manager to install the following packages:

Install all dependencies:

```bash
pip install selenium
```

```bash
pip install webdriver-manager
```

or \
Use the requirements file which describes the packages that have been installed in virtual environment. This file allow to restore those packages using pip.
```bash
pip install -r requirements.txt
```

## Usage

Run the file:
```
cd PATH_TO_PYTHON_FILE
python3 main.py
```

## Status

ToDo:
* Tests
* Add Error Handling
* Troubleshooting

## Contact

Created by aude11 
