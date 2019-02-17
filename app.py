from ctypes import cdll
from flask import Flask
from sys import platform

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

# Set up FFI
MAPI = cdll.LoadLibrary('mapi.rs/lib/target/debug/{}mapi.{}'.format(prefix, ext))

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
