from oselab import app
from flaskext.markdown import Markdown

Markdown(app,
  extensions=['tables', 'attr_list', 'smarty', 'nl2br', 'codehilite', 'fenced_code'],
  extension_configs={
    'codehilite': {
      'css_class': 'highlight'
    },
  },
)
