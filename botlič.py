from bottle import Bottle, request, redirect
from bottle_login import LoginPlugin



app = Bottle()
app.config["SECRET_KEY"] = "skrivnost"

prijava = app.install(LoginPlugin())

@login.load_user
def nalozi_glede_na_id(uporabnikov_id):


@app.route("/")
def index():
    uporabnik = prijava.get_user()
    
    return uporabnik.name

@app.route('/odjava')
def odjava():
    prijava.logout_user()
    return redirect("/")

@app.route('/prijava')
def prijava():
    uporabnikov_id = int(request.GET.get('uporabnikov_id'))
    prijava.login_user(uporabnikov_id)
    return redirect("/")

