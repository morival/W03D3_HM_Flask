from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

from controllers import controller # ADDED