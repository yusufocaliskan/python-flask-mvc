from sqlite3 import Cursor
from flask import Flask, render_template, request, Blueprint
from flask_mysqldb import MySQL

#Custom..
from framework.Router import Router
import config

#Start the app..
app = Flask(__name__, template_folder=config.VIEWS_DIR)


#Confing start...
app.config.from_object(config)

mysql = MySQL()
#---------------------[ Database ]---------------------
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "---"
app.config["MYSQL_DB"] = "book_store"
app.config["MYSQL_HOST"] = "localhost" 

#Database connection
mysql.init_app(app)


@app.route("/")
def index():

    cur = mysql.connection.cursor()
    cur.execute("select * from books")
    data = cur.fetchall()
    mysql.connection.commit()
    print(str(data))
    return "test"

Router.run(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
