from flask import Flask
from glob import glob
from datetime import datetime
import OpenSSL
import os

app = Flask(__name__)

def certChecker(cert_files):
    content = []
    for file in cert_files:
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open(file).read())  
        cert_path=os.path.basename(file)+":"
        not_before= "Not before: "+ datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ').strftime("%b %-m %H:%M:%S %Y GMT")
        not_after = "Not after: "+  datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ').strftime("%b %-m %H:%M:%S %Y GMT")
        content.append(cert_path+" | "+not_before+" | "+ not_after)
    return content

@app.route('/')
def main():
    cert_files=glob('/etc/kubernetes/pki/*.crt')
    certchecker_output=certChecker(cert_files)
    return certchecker_output

@app.route('/test')
def test():
    return "Test, this is working!"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)