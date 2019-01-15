from flask import Blueprint, render_template

from flask import Flask, Blueprint, render_template, redirect, url_for


route2_blueprint = Blueprint('route2', __name__, template_folder='templates')

app = Flask(__name__)


@route2_blueprint.route('/route2', methods= ['GET', 'POST'])
def route2():
      return render_template('route2.html')

if __name__ == '__main__':
    app.run(debug= True)


