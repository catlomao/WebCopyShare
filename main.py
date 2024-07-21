from pyperclip import paste
    # a module that allows us to copy the clipboard
from time import sleep
    # to slow down high usage (making the loop not use the maximum CPU usage)
from flask import Flask , render_template_string , jsonify
    # importing the module that allows us to return the json output using a url
app = Flask(__name__)
@app.route("/")
def index():
    while True:
            # <---- THE START OF THE LOOP ---->
        sleep(0.2)
        return jsonify(paste())
            # <---- THE END OF THE LOOP ---->
if __name__ == "__main__":
    app.run(debug=True)
    #   Runs the program in debug mode, you can remove it if you dont want to!