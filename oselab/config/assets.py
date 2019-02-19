from oselab import app
from flask_assets import Environment, Bundle

assets = Environment(app)

# Main Vendor JavaScript
vendor_javascripts = Bundle(
  'vendor/javascript/jquery-3.2.1.slim.min.js',
  'vendor/javascript/popper.min.js',
  'vendor/javascript/bootstrap.min.js',
  output='build/main-%(version)s.js'
)
assets.register('vendor_javascripts', vendor_javascripts)

# Main JavaScript asset bundle
javascripts = Bundle('javascript/home/slideshow.js', filters='rjsmin', output='build/main-%(version)s.js')
assets.register('javascripts', javascripts)

# Main CSS asset bundle
stylesheets = Bundle(
  'css/global.css',
  'css/layout.css',
  'css/pygment.css',
  'css/components/*.css',
  'css/home/*.css',
  'css/gallery/*.css',
  'css/faq/*.css',
  'css/bootcamp/*.css',
  output='build/main-%(version)s.css'
)
assets.register('stylesheets', stylesheets)
