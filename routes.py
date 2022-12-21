from flask import Flask,jsonify,request
import random
import os
import json
import shutil

app = Flask(__name__)
PATH="/home/cbyk-dev/Documents/api-py-teti/static/fotos"

@app.route("/nova-sala",methods=["GET"])
def nova_sala():
    chave_acesso = random.randint(10,100)
    os.mkdir(f"{PATH}/{chave_acesso}")
    var_pasta = f'{PATH}{chave_acesso}'
    print(var_pasta)
    return jsonify(path=var_pasta)

@app.route("/entra_sala_existente",methods=["GET","POST"])
def velha_sala():
    if request.method =="POST":
        cod_da_sala = request.json["data"]
        print(cod_da_sala)
        NEWPATH = f'{PATH}/{cod_da_sala}'
        if os.path.exists(NEWPATH):
            message = {"message":True}
            return jsonify(message)
        message = {"message":False}
        return jsonify(message)
    
@app.route("/new_message",methods=["POST"])
def new_message():
    url_foto = request.json["file"]
    codigo_sala = request.json["codigo_sala"]
    user = request.json["user"]
    print(user)
    if user =="user1":
        shutil.copy(
        url_foto,
        "/home/cbyk-dev/Documents/api-py-teti/static/upload/"+codigo_sala)
    if user =="user2":
        shutil.copy(
        url_foto,
        "/home/cbyk-dev/Documents/api-py-teti/static/upload/"+codigo_sala)  
    return

@app.route("/ob-mensagem",methods=["GET"])
def obter_mensagem():
    user="user1"
    cod_room=00
    if user =="user1":
        path={
            "path":"/home/cbyk-dev/Documents/api-py-teti/static/fotos/"+str(cod_room)+"/foto-user1.png"
        }
        return jsonify(path)
    if user =="user2":
        path={
            "path":"/home/cbyk-dev/Documents/api-py-teti/static/fotos/"+str(cod_room)+"/foto-user1.png"
        }
        return jsonify(path)
    
    
if __name__=='__main__':
    app.run(debug=True)