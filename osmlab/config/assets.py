from osmlab import app
from flask_assets import Environment, Bundle

assets = Environment(app)

# JavaScript asset bundle
javascripts = Bundle('javascript/home/slideshow.js', filters='rjsmin', output='build/main-%(version)s.js')
assets.register('javascripts', javascripts)

# CSS asset bundle
stylesheets = Bundle(
  'css/global.css',
  'css/layout.css',
  'css/components/*.css',
  'css/home/*.css',
  'css/gallery/*.css',
  output='build/main-%(version)s.css'
)
assets.register('stylesheets', stylesheets)
