from flask import Flask, render_template
from logic.character import Character
import sqlite3

path="/workspaces/HUBRIS/HUBRIS.db"

app = Flask(__name__)

@app.route("/sheet")
def sheet():
    con=sqlite3.connect(path)
    character=Character("El",con)
    return render_template("sheet.html",character=character)

@app.route('/')
def home():
    return render_template("home.html")