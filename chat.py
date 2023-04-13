import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    response = "No entiendo..."

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
    
    writeConversation(msg, response)

    return response

def writeConversation(msg, response):
    conversation = {
                    "input": msg,
                    "output": response
                }
    
    with open("conversation.json", "rb") as archivo:
        datos = json.load(archivo)

    datos["conversaciones"].append(conversation)

    with open("conversation.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("¡Hablemos! (escriba 'salir' para finalizar la conversación)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("Tú: ")
        if sentence == "salir":
            break

        resp = get_response(sentence)
        print(resp)

