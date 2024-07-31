from easygui_qt import get_string
# a gui app that allows for selecting port for already compiled programs like exe , etc
from pyperclip import paste
    # a module that allows us to copy the clipboard
from flask import Flask , render_template_string , jsonify
    # importing the module that allows us to return the json output using a url
app = Flask(__name__)
@app.route("/")
def index():
        return jsonify(paste())
if __name__ == "__main__":
    portnum = int(get_string("Enter Port", default_response="8080"))
    app.run(port=portnum)
    #   Runs the program in debug mode, you can remove it if you dont want to!
