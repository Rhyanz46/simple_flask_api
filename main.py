from app import app
from api.api import api

app.register_blueprint(api, url_prefix='/v1')

if __name__ == "__main__":
    app.run(debug=True)