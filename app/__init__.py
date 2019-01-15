from flask import Flask

from config import *
app = Flask(__name__, instance_relative_config=True)


from app.mods.mod_index.views import index_blueprint
from app.mods.mod_route1.views import route1_blueprint
from app.mods.mod_route2.views import route2_blueprint

#register the blueprints
app.register_blueprint(index_blueprint)
app.register_blueprint(route1_blueprint)
app.register_blueprint(route2_blueprint)

@app.context_processor
def use_dict_to_templates():
    return dict(inp1=inp1, inp2=inp2, inp3=inp3)
