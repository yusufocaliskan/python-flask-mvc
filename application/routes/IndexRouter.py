from crypt import methods
from flask import Blueprint

#import IndexController
from application.controllers.index.IndexController import IndexController

IndexRouter = Blueprint('index_controller', __name__)
IndexRouter.route('/', methods=['GET'])(IndexController.home)