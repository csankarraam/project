from flask import Blueprint, render_template

from flask import Flask, Blueprint, render_template, redirect, url_for


index_blueprint = Blueprint('index', __name__, template_folder='templates')

app = Flask(__name__)


@index_blueprint.route('/', methods= ['GET', 'POST'])
def index():
      return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)


