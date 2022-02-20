from flask import render_template

class IndexController:

    def home():
       return render_template('home/index.html')
      