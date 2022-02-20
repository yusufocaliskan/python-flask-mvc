from crypt import methods
from flask import Blueprint

#Get UserController
from application.controllers.users.UserController import UserController
UserRouter = Blueprint('user_controller', __name__)

UserRouter.route('/',methods=['GET'])(UserController.home)
