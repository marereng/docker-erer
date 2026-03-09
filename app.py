from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/analisa-data')
def analisa_data():
    return 'Halo ini sudah analisa data'

@app.route('/analisa-rere')
def analisa_rere():
    return 'Ya, beginilah hidup'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)