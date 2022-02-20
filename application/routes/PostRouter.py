from crypt import methods
from flask import Blueprint

#Get PostController
from application.controllers.posts.PostController import PostController
PostRouter = Blueprint('post_controller', __name__)

PostRouter.route('/',methods=['GET'])(PostController.home)
