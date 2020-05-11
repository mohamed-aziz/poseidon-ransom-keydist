from app.ws import create_app 
from app.secrets import Config

app = create_app(Config)