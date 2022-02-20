from flask import Flask, render_template, request, Blueprint


from framework.Router import Router
import config

print(config.VIEWS_DIR)
#Start the app..
app = Flask(__name__, template_folder=config.VIEWS_DIR)

#Confing start...
app.config.from_object(config)

Router.run(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
