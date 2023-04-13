## Configuración inicial:
Este repositorio actualmente contiene los archivos iniciales.

Clonar el repositorio y crear un entorno virtual
```
$ git clone https://github.com/Maicolfm26/chatbot.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ .\venv\Scripts\activate.bat
```
Instalar dependencias
```
$ (venv) pip install Flask torch torchvision nltk
```
Instalar paquete nltk
```
$ (venv) python
>>> import nltk
>>> nltk.download('omw')
```
Modificar intents.json con diferentes intenciones y respuestas para su Chatbot

Ejecutar
```
$ (venv) python train.py
```
Esto generará el archivo data.pth. Luego, ejecutar
el siguiente comando para probarlo desde la interfaz grafica.
```
$ (venv) python app.py
```