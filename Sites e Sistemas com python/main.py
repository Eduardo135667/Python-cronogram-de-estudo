from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# roda o nosso aplicativo
app.run()