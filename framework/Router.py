
class Router:

    def run(app):
        
        print("*************[Dest pê  dike!!]*************")
        
        #UserControllers Routes..
        from application.routes.UserRouter import UserRouter
        app.register_blueprint(UserRouter, url_prefix='/users')

        #post
        from application.routes.PostRouter import PostRouter
        app.register_blueprint(PostRouter,url_prefix="/posts")

        #Index Page!
        from application.routes.IndexRouter import IndexRouter
        app.register_blueprint(IndexRouter, url_prefix="/")