import datetime
import bcrypt
import pymongo
from flask import *
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['COVID_19']
mycol = mydb['Patient']
admin = mydb['Login']
analamanga = mydb['Analamanga']
alaotraMangoro = mydb['alaotra_magoro']
amoromania = mydb['Amoromania']
analanjirofo = mydb['Analanjorofo']
androy = mydb['Androy']
antsinanana = mydb['Antsinanana']
atsimoAndrefana = mydb['AtsimoAndrefana']
atsimoAntsinanana = mydb['AtsimoAntsinanana']
betsiboka = mydb['Betsiboka']
boeny = mydb['Boeny']
bongolava = mydb['Bongolava']
diana = mydb['DIANA']
ihorombe = mydb['Ihorombe']
itasy = mydb['Itasy']
matsiatra_Ambony = mydb['MatsiatraAmbony']
melaky = mydb['Melaky']
menabe = mydb['Menabe']
sava = mydb['SAVA']
sofia = mydb['Sofia']
anosy = mydb['Anosy']
vakinankaratra = mydb['Vakinakaratra']
vatovavy_Fitovinany = mydb['VatovavyFitovinany']
madaTotal = mydb['MadaTotal']
totalRegion = mydb['TotalRegion']
commentaire = mydb['commentaire']
commentaire.drop()
@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/Analamanga')
def cdcsd():
    o = analamanga.find()
    myquery = {"_id": 2}
    mydoc = analamanga.find(myquery)
    for x in mydoc:
        z = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']

    return render_template("Analamanga.html", o=o, z=z, b=b, c=c)


@app.route('/Anosy')
def cscxd():
    o = anosy.find()
    myquery = {"mois": "Octobre"}
    mydoc = anosy.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    return render_template("Anosy.html", o=o, a=a, b=b, c=c)


@app.route('/Alaotra-Mangoro')
def cvsuib():
    myquery = {"mois": "Octobre"}
    mydoc = alaotraMangoro.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = alaotraMangoro.find()
    return render_template("Alaotra-Mangoro.html", o=o, a=a, b=b, c=c)


@app.route('/Amoron_i_Mania')
def cdvf():
    myquery = {"mois": "Octobre"}
    mydoc = amoromania.find(myquery)
    for x in mydoc:
        z = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = amoromania.find()
    return render_template("Amoron_i_Mania.html", o=o, z=z, b=b, c=c)


@app.route('/Analanjirofo')
def vf():
    myquery = {"mois": "Octobre"}
    mydoc = analanjirofo.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = analanjirofo.find()
    return render_template("Amoron_i_Mania.html", o=o, a=a, b=b, c=c)


@app.route('/Androy')
def lf():
    myquery = {"mois": "Octobre"}
    mydoc = androy.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = androy.find()
    return render_template("Androy.html", o=o, a=a, b=b, c=c)


@app.route('/Atsimo-Andrefana')
def fl():
    myquery = {"mois": "Octobre"}
    mydoc = atsimoAntsinanana.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = atsimoAntsinanana.find()
    return render_template("Atsimo-Atsinanana.html", o=o, a=a, b=b, c=c)


@app.route('/Atsimo-Atsinanana')
def fl3():
    myquery = {"mois": "Octobre"}
    mydoc = atsimoAndrefana.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    o = atsimoAndrefana.find()
    return render_template("Atsimo-Atsinanana.html", o=o, a=a, b=b, c=c)


@app.route('/Atsinanana')
def xs3():
    myquery = {"mois": "Octobre"}
    mydoc = antsinanana.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = antsinanana.find()
    return render_template("Atsinanana.html", i=i, a=a, b=b, c=c)


@app.route('/Betsiboka')
def xscx3():
    myquery = {"mois": "Juin"}
    mydoc = betsiboka.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = betsiboka.find()
    return render_template("Betsiboka.html", i=i, a=a, b=b, c=c)


@app.route('/Boeny')
def xscxv3():
    myquery = {"mois": "Octobre"}
    mydoc = boeny.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = boeny.find()
    return render_template("Boeny.html", i=i, a=a, b=b, c=c)


@app.route('/Bongolava')
def xcscxv3():
    myquery = {"mois": "Octobre"}
    mydoc = bongolava.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = bongolava.find()
    return render_template("Bongolava.html", i=i, a=a, b=b, c=c)


@app.route('/Diana')
def xcsccxv3():
    myquery = {"mois": "Octobre"}
    mydoc = diana.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = diana.find()
    return render_template("Diana.html", i=i, a=a, b=b, c=c)


@app.route('/MatsiatraAmbony')
def xcsczcxv3():
    myquery = {"mois": "Octobre"}
    mydoc = matsiatra_Ambony.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = matsiatra_Ambony.find()
    return render_template("Haute Matsiatra.html", i=i, a=a, b=b, c=c)


@app.route('/Ihorombe')
def aq():
    myquery = {"mois": "Octobre"}
    mydoc = ihorombe.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = ihorombe.find()
    return render_template("Ihorombe.html", i=i, a=a, b=b, c=c)


@app.route('/Itasy')
def avq():
    myquery = {"mois": "Octobre"}
    mydoc = itasy.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = itasy.find()
    return render_template("Itasy.html", i=i, a=a, b=b, c=c)


@app.route('/final')
def finale():
    i = madaTotal.find_one()
    o = totalRegion.find()
    return render_template('final.html', i=i, o=o)


@app.route('/Melaky')
def acvq():
    myquery = {"mois": "Octobre"}
    mydoc = melaky.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = melaky.find()
    return render_template("Melaky.html", i=i, a=a, b=b, c=c)


@app.route('/Menabe')
def acvccq():
    myquery = {"mois": "Octobre"}
    mydoc = menabe.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = menabe.find()
    return render_template("Menabe.html", i=i, a=a, b=b, c=c)


@app.route('/Sava')
def acccvccq():
    myquery = {"mois": "Octobre"}
    mydoc = sava.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = sava.find()
    return render_template("Sava.html", i=i, a=a, b=b, c=c)


@app.route('/Sofia')
def acccvcccq():
    myquery = {"mois": "Octobre"}
    mydoc = sofia.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = sofia.find()
    return render_template("Sofia.html", i=i, a=a, b=b, c=c)


@app.route('/Vakinankaratra')
def accccvcccq():
    myquery = {"mois": "Octobre"}
    mydoc = vakinankaratra.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = vakinankaratra.find()
    return render_template("Vakinankaratra.html", i=i, a=a, b=b, c=c)


@app.route('/Vatovavy-Fitovinany')
def accccvvcccq():
    myquery = {"mois": "Octobre"}
    mydoc = vatovavy_Fitovinany.find(myquery)
    for x in mydoc:
        a = x['Nouveau_cas']
        b = x['Gueris']
        c = x['Deces']
    i = vatovavy_Fitovinany.find()
    return render_template("Vatovavy-Fitovinany.html", i=i, a=a, b=b, c=c)


#########administrator##########
@app.route('/home')
def administrateur():
    return render_template('home.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/liste', methods=['GET', 'POST', 'DELETE', ])
def liste():
    # see
    afficher_liste = analamanga.find()
    # search the document to delete
    key = request.values.get("reference")
    analamanga.delete_one({"_id": key})
    return render_template("liste.html", afficher_liste=afficher_liste)


@app.route('/supprimer')
def supr():
    return render_template('supprimer.html')


@app.route('/maj')
def maj():
    return render_template('mise_a_jour.html')


@app.route('/success', methods=['POST', 'GET'])
def ajouter():
    # ajout dans la database
    nouveau_cas = None
    deces = None
    gueris = None
    if request.method == 'POST':
        reference = request.form['reference']
        nouveau_cas = request.form['nouveau_cas']
        deces = request.form['deces']
        gueris = request.form['gueris']
        mois = request.form['mois']
        # name of collection
        mydict = {"_id": reference, "Nouveau_cas": nouveau_cas,
                  "Gueris": gueris,
                  "Deces": deces, "mois": mois}
        i = analamanga.insert_one(mydict)
        i = analamanga.find()
        return render_template('success.html', i=i)


@app.route("/action", methods=['POST'])
def action():
    nouveau_cas = request.values.get("maj_nouveau_cas")
    deces = request.values.get("maj_deces")
    gueris = request.values.get("maj_gueris")
    mois = request.values.get("mois")
    id = request.values.get("_id")
    analamanga.update({"_id": id},
                      {'$set': {"Nouveau_cas": nouveau_cas, "Gueris": gueris, "Deces": deces, "mois": mois}})
    return redirect("/liste")


################CONTROLLER##############################

@app.route('/access')
def index():
    if 'username' in session:
        return render_template('home.html')

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_user = admin.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username or password'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        existing_user = admin.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            admin.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/actualite', methods=['GET', 'POST'])
def actualite():
    y = datetime.datetime.now()
    mydict = {"comment": request.values.get('text'),
              "date": y.strftime("%c"),
              "couleur": request.values.get('couleur'),
              "couleur_text": request.values.get('couleur_text')}
    x = commentaire.insert_one(mydict)
    return render_template('actualite.html', i=commentaire.find())


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
