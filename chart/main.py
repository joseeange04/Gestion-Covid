from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import *
app = Flask(__name__)
myclient = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
# name of database
mydb = myclient['database_final']
# this show  the name's collection
mycol = mydb['MadaParMois']
"""@app.route('/')
def chart():
    x = mycol.find({"mois":"mars"})
    for i in x:
        a = i["deces"]
        print(a)
    return render_template('chart.html',a=a)"""
@app.route('/cas_total_region')
def cas_total_region():
    x = mycol.find({"_id": 7})
    for i in x:
        a= i["Nouveau_cas"]
        print(a)
    y=mycol.find({"_id": 6})
    for i in y:
        b= i["Nouveau_cas"]
    z= mycol.find({"_id": 5})
    for i in z:
        c = i["Nouveau_cas"]
    az = mycol.find({"_id": 4})
    for i in az:
        d = i["Nouveau_cas"]
    jkh = mycol.find({"_id": 3})
    for i in jkh:
        e = i["Nouveau_cas"]
    jkh = mycol.find({"_id": 2})
    for i in jkh:
        f = i["Nouveau_cas"]
    vq= mycol.find({"_id": 1})
    for i in vq:
        g = i["Nouveau_cas"]
    qer = mycol.find({"_id": 0})
    for i in qer:
        h = i["Nouveau_cas"]

    return render_template('cas_total_region.html',a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)