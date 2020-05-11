from flask import Blueprint

blueprint = Blueprint('index', __name__)

site_content = """
<html>
  <head>
    <title>Totally legitimate website</title>
  </head>
  
  <body>
    <h2>Totally legitmiate website</h2>
  </body>
</html>
"""

@blueprint.route('/')
def index():
    return site_content