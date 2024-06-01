import sys
sys.path.append(".")

from flask import Flask
from flask import Flask, render_template, request
sys.path.append("src")
from logica.huffman_cleanCode import HuffmanCoding
from controller import ControladorRegistros
from model.Registros import Registro

app = Flask(__name__)


@app.route('/')
def index():
     return render_template('index.html')



@app.route('/codificar', methods=['GET', 'POST'])
def codificar():
    if request.method == 'POST':
        text = request.form['text']
        huffman_coding = HuffmanCoding()
        encoded = huffman_coding.encode(text=text)
        reg = Registro(decode_text=text, encode_text=encoded)
        ControladorRegistros.Insertar(fila=reg)
        return render_template('codificar.html', original=text, encoded=encoded)
    return render_template('codificar.html')


@app.route ('/decodificar',methods=['GET', 'POST'])
def decodificar():
     if request.method == 'POST':
        text_to_decode = request.form['text_to_decode']
        huffman_coding = HuffmanCoding()
        decoded_text = huffman_coding.decode(text_to_decode)
        reg = Registro(decode_text=decoded_text, encode_text=text_to_decode)
        ControladorRegistros.Insertar(fila=reg)
        return render_template('decodificar.html', original=text_to_decode, decoded=decoded_text)
     return render_template ('decodificar.html')


@app.route('/registros')
def registros():
     registros = ControladorRegistros.ObtenerRegistros()
     return render_template('registros.html', registros=registros)


if __name__ == '__main__':
    app.run(debug=True)
