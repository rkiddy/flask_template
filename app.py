
import sys

from dotenv import dotenv_values
from flask import Flask
from jinja2 import Environment, PackageLoader

cfg = dotenv_values(".env")

sys.path.append(f"{cfg['APP_HOME']}")
import data

app = Flask(__name__)
application = app 
env = Environment(loader=PackageLoader('app', 'pages'))


@app.route(f"/{cfg['WWW']}")
@app.route(f"/{cfg['WWW']}/")
def contracts_main():
    main = env.get_template('app.html')
    context = data.app_main()
    return main.render(**context)

