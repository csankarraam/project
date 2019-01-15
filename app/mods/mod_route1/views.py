from flask import Blueprint, render_template

from flask import Flask, Blueprint, render_template, redirect, url_for


route1_blueprint = Blueprint('route1', __name__, template_folder='templates')

app = Flask(__name__)


@route1_blueprint.route('/route1', methods= ['GET', 'POST'])
def route1():
      return render_template('route1.html')

if __name__ == '__main__':
    app.run(debug= True)


