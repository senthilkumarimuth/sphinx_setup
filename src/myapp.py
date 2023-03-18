
"""
Sphnix dome module.

"""

from flask import Flask
from utils import division_script

# Setting up the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Route to add two number
    :return: result or error message
    """
    try:
        c = division_script.divide(100, 100)
    except Exception as e:
        c =e

    return str(c)


if __name__ == "__main__":
    app.run(port=500, debug=True)
