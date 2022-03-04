from sqlite3 import Cursor
from flask import Flask, render_template, request, Blueprint
from framework.Database import Database

#Custom..
from framework.Router import Router
import config

#Start the app..
app = Flask(__name__, template_folder=config.VIEWS_DIR)


#Confing start...
app.config.from_object(config)


#---------------------[ Database ]---------------------
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "----"
app.config["MYSQL_DB"] = "book_store"
app.config["MYSQL_HOST"] = "localhost" 

#Database connection
Database = Database(app)


@app.route("/")
def index():

    cur = Database.mysql.connection.cursor()
    cur.execute("select * from books")
    data = cur.fetchall()
    Database.mysql.connection.commit()
    return str(data)

Router.run(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
