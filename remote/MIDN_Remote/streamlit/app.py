from flask import Flask

import socket
from requests import get

CUSTOM_OUTPUT_PATH =  'data/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024
app.config['custom_output_PATH'] = CUSTOM_OUTPUT_PATH

try :
    hostname = socket.getfqdn()
    ip_addr = socket.gethostbyname_ex(hostname)[2][0]
except:
    app.config['client_ip'] = '127.0.0.1'
else:   
    app.config['client_ip'] = ip_addr 	

try :   
    app.config['public_ip']  = get('https://api.ipify.org').content.decode('utf8')
except:
    app.config['public_ip']  = app.config['client_ip']
    
app.config['client_port'] = '6000'
app.config['client_name'] = 'Please change the remote site name'

app.config['server_app'] = 'https://127.0.0.1'


