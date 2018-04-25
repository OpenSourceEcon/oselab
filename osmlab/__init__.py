from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)

import osmlab.config.assets
import osmlab.views
