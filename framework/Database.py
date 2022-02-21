import config
from flask_mysqldb import MySQL

class Database:

    #MySQL Connector.
    Conntector = ""

    #MySQL
    mysql      = ""

    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)