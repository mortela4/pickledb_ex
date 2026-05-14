# PickleDB example project

Show use of 'pickledb' Python package to 
- set up PickleDB to use JSON-file as storage
- insert some key-value pairs
- write the data to JSON file
- read back data from file
- modify data, and write back again

## Usage

Run 'python setup.py' standalone to get a "settings.json" settings-file.
The content will be:
```json
{"hostname":"192.168.1.1","port_number":8080}
```

Next - run 'python main.py' and watch the content of the settings 'database' change.
The final "settings.json" can be viewed in any text editor.

Example session:
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
