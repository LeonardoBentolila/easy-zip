# easy-zip
Easy CLI to zip entire folders into zip file using python with progress bar and total files listed.

# installation:
Install requirements.txt

create executable with command: ```pyinstaller .\main.py --name=easyzip```

add ```.\dist\easyzip``` to path

# Usage:
positional arg:

 => path of the folder to zip;

options:

-o / --output : zip output file path (if none given, will create file with the same name as target folder at the current directory);

-ae / --addEmpty : flag to indicate that you want to add empty sub folders to final zip file. Default is set to False (won't save empty folders to zip file);

-f / --filter : files filter to add specific files types to final zip. Defalt is set to ("*") all files;

-h : print help;

# Copyright:
@leobazao 2024
