import click
from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return message

@click.command()
@click.option('--encoding', default='utf-8', help='Establecer la codificación predeterminada.')
def runserver(encoding):
    """Inicia el servidor Flask."""
    app.run()

if __name__ == '__main__':
    runserver()