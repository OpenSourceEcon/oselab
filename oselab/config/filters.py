import textwrap
import re
from oselab import app

@app.template_filter('dedent')
def dedent(s):
    return textwrap.dedent(s)

NOT_HANDLE_SAFE = re.compile(r'[^A-Za-z0-9\-]+')
@app.template_filter('handleize')
def handleize(s):
    handle = '-'.join(s.lower().strip().split(' '))
    clean_handle = NOT_HANDLE_SAFE.sub('', handle)
    return clean_handle


