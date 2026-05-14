# PickleDB example project

Show use of 'pickledb' Python package to 
- set up PickleDB to use JSON-file as storage
- insert some key-value pairs
- write the data to JSON file
- read back data from file
- modify data, and write back again


## Introduction

The project has 3 Python source files under "src" subfolder:
- setup.py --> contains the key-value storage(='database') initialization and update/modification logic 
- read_modify_write.py --> has a single function 'use_settings_and_process()' that conditionally modify 'port_number' value
- main.py --> sample code for demonstration; 


## Usage

Run 'python setup.py' standalone to get an initial "settings.json" settings-file.
The content will be:
```json
{"hostname":"192.168.1.1","port_number":8080}
```

Next - run 'python main.py' and watch the content of the settings 'database' change.
The final "settings.json" can be viewed in any text editor.

Example first-run session output:
```sh
Settings:
192.168.1.1
8080
Port number 8080 is INVALID (not set or >5000). Forcing to 3000.
Processing with port number: 3000
Processing complete.
Settings now:
192.168.1.1
3000
Port number 3000 is valid. Proceeding with processing...
Processing with port number: 3000
Processing complete.
Settings now:
192.168.1.1
3000
```

And final JSON content:
```json
{"hostname":"192.168.1.1","port_number":3000}
```

Example of next run (and every run afterwards):
```sh
Settings:
192.168.1.1
3000
Port number 3000 is valid. Proceeding with processing...
Processing with port number: 3000
Processing complete.
Settings now:
192.168.1.1
3000
Port number 3000 is valid. Proceeding with processing...
Processing with port number: 3000
Processing complete.
Settings now:
192.168.1.1
3000
```
Until e.g. code is modified to change the key-value database.
 
