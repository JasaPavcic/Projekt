from bottle import Bottle, request, redirect, run
from bottle_login import LoginPlugin
from bottle import static_file
from bottle import template
import sys
from model import uporabnik



app = Bottle()
app.config["SECRET_KEY"] = "skrivnost"

login_plugin = app.install(LoginPlugin())

@login_plugin.load_user
def load_user_by_id(id_uporabnika):
    return Uporabnik.dobi({'id': id_uporabnika})

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

@app.route("/", method='GET')
def index():
    uporabnik = login_plugin.get_user()
    if not uporabnik:
        return template('predloge/prijava.tpl')
    return template('predloge/index.tpl')


@app.route('/odjava')
def odjava():
    login_plugin.logout_user()
    return redirect("/")

@app.route('/prijava', method='POST')
def prijava():
    uporabnisko_ime = request.POST.get('ime')
    geslo = request.POST.get('geslo')
    uporabnik = Uporabnik.dobi({'ime': uporabnisko_ime, 'geslo': geslo})
    if uporabnik:
        login_plugin.login_user(uporabnik[0])
        return redirect("/")
    else:
        return template('predloge/prijava_neuspesna.tpl', msg='Napacno upor. ime ali geslo.')
    
@app.route('/registracija')
def registracija():
    return template('predloge/registracija_obrazec.tpl')

@app.route('/registracija_uspesna')
def registracija_uspesna():
    return template('predloge/registracija_uspesna.tpl')

@app.route('/registriraj', method='POST')
def registriraj():
    uporabnisko_ime = request.POST.get('ime')
    geslo = request.POST.get('geslo')
    potrditev = request.POST.get('potrditev')
    napaka = ''
    if not Uporabnik.dobi({'ime': uporabnisko_ime}):
        if geslo == potrditev:
            Uporavnik.ustvari({'ime':uporabnisko_ime, 'geslo': geslo, 'denar': 100})
            return redirect("/registracija_uspesna")
        else:
            napaka = 'Gesli se ne ujemata'
    else:
        napaka = 'Uporabnik ze obstaja'
    return template('predloge/registracija_neuspesna.tpl', msg=napaka)

run(app, host='localhost', port=8083)
