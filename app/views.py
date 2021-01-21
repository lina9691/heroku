# from app import app
# from flask import render_template,request
import sqlite3
import json
from flask import jsonify

f = open('MrAbreu.json')
data = json.load(f)
f.close()

def createdb():
    conn = sqlite3.connect ('base.db')
    print ("base de donnéées ouverte avec succès")
    conn.execute("CREATE TABLE Patient(Numero_utilisateur INTEGER, Mot_de_passe TEXT, Nom TEXT, Prenom TEXT, Age INTEGER, Adresse TEXT, Hematies INTEGER, Hemoglobine INTEGER, Hematocrite INTEGER, VGM INTEGER, CCMH INTEGER, TCMH INTEGER,RDW INTEGER,Polynucleaires_neutrophiles INTEGER,Polynucleaires_eosinophiles INTEGER,Polynucleaires_basophiles INTEGER,Lymphocytes INTEGER, Monocytes INTEGER)")
    print ("Table créée avec succès")
    conn.close()

def adduser(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes):
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Patient (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes))
        con.commit()
    con.close()

def showdb():
    con = sqlite3.connect('bdd.db')
    cursor = con.cursor()
    cursor.execute("SELECT * from Patients;")
    print(cursor.fetchall())


def utilisateur():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Numero_utilisateur from Patient ;")
    a = cursor.fetchall()
    b=''
    #L=[]
    for i in a:
        b = "".join(map(str, i))
        #L.append(b)
    print (b)
        


def mdp():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Mot_de_passe from Patient ;")
    a = cursor.fetchall()
    L=[]
    for i in a:
        b = "".join(map(str, i))
        L.append(b)
    print (b)

def recup(data):
    return jsonify(data)
    

def transfer(data):
    with sqlite3.connect('Mabase.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Patients")
        
def remplissagee(data):
    for i in data:
        Numero_utilisateur = data['Numero_utilisateur']
        Adresse = data['Adresse']
        Mot_de_passe = data['Mot_de_passe']
        Nom = data['Nom']
        Prenom = data['Prenom']
        Age = data['Age']
        Hematies = data['Hematies']
        Hemoglobine = data['Hemoglobine']
        Hematocrite = data['Hematocrite']
        VGM = data['VGM']
        CCMH = data['CCMH']
        TCMH = data['TCMH']
        RDW = data['RDW']
        Polynucleaires_neutrophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_eosinophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_basophiles = data['Polynucleaires_basophiles']
        Lymphocytes = data['Lymphocytes']
        Monocytes = data['Monocytes']
    adduser(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes)


            
# def checkdb():
#     conn = sqlite3.connect('bdd.db')
#     print ("base de donnéées ouverte avec succès")
#     with sqlite3.connect("bdd.db") as con:
#         cur = con.cursor()



# @app.route("/")
# def index():
#     return render_template ('index.html')

# @app.route("/new",methods=['POST'])
# def new():
#     utilisateur = request.form.get('utilisateur')
#     mdp = request.form.get ('mdp')
#     if rech_utilisateur()==utilisateur and rech_mdp()==mdp :
#         return "ok"
#     else :
#         return "Utilisateur incorrect"
