from ctypes import cdll
from flask import Flask
from sys import platform

import os
import os.path

#########
# SETUP #
#########

app = Flask(__name__)

if platform == 'darwin':
    prefix = 'lib'
    ext = 'dylib'
elif platform == 'win32':
    prefix = ''
    ext = 'dll'
else:
    prefix = 'lib'
    ext = 'so'

lib = '{}mapi.{}'.format(prefix, ext)

# Set up FFI
if os.path.isdir('../mapi.rs/lib/target/release') == True and os.path.isfile('../mapi.rs/lib/target/release/{}'.format(lib))== True:
    MAPI = cdll.LoadLibrary('../mapi.rs/lib/target/release/{}'.format(lib))
elif os.path.isdir('mapi.rs/lib/target/debug') == True and os.path.isfile('mapi.rs/lib/target/debug/{}'.format(lib)):
    MAPI = cdll.LoadLibrary('/mapi.rs/lib/target/debug/{}'.format(lib))
else:
    if os.path.basename(os.getcwd()) == 'mapi':
        print('Creating shared library...')
        os.system('cd ../mapi.rs/lib/; make clean; make test')
        MAPI = cdll.LoadLibrary('target/release/{}'.format(lib))
    elif os.path.basename(os.getcwd()) == 'mapi.py':
        print('Creating shared library...')
        os.system('cd mapi.rs/lib; make clean; make test')
        MAPI = cdll.LoadLibrary('target/debug/{}'.format(lib))
    else:
        print('Something went wrong. Are you working with a clean download of the source code?')
        exit(1)


#############
# VARIABLES #
#############

helpMsg = """MAPI usage:
eg. curl $SERVER_ADDR:$PORT/{endpoint}
These endpoints can be:
/filescount\n
For more information, consider visiting https://github.com/naltun/mapi.py"""

##########
# ROUTES #
##########

@app.route('/')
def index():
    print('[*] Request to / called...')
    return helpMsg


@app.route('/filescount')
def filescount():
    print('[*] Request to /filescount called...')
    return 'File Count: ' + str(MAPI.get_files_count())

@app.route('/hdd-available')
def getHddAvail():
    print('[*] Request to /hdd-available called...')
    return "HDD Space Available: {} GB's".format(int(MAPI.get_harddisk_avail() / 1024))

@app.route('/ram-used')
def getRamUsed():
    print('[*] Request to /ram-used called...')
    return "RAM Used: {} GB's".format(int(MAPI.get_ram_used() / 1024))

if __name__ == '__main__':
    app.run()
