from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola calabaza, prueba heroku exitosa:)"

if __name__ == "__main__":
    app.run()