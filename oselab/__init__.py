from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)

import oselab.config.assets
import oselab.config.markdown
import oselab.views
