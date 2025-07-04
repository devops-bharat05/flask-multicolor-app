from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    color = os.environ.get('COLOR', 'red')
    html = f"""
    <html><body style='background-color:{color}; text-align:center;'>
    <h1>{color.upper()} App</h1><p>Pod: {hostname}</p><p>IP: {ip_address}</p></body></html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
