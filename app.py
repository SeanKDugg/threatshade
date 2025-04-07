from flask import Flask, render_template
import json


app = Flask(__name__, static_url_path='/static', static_folder='static')


"""
Reads json file with page contents
"""
with open('text_content.json', encoding="utf-8") as json_file:
    data = json.load(json_file)


""" 
Defines the route for index page
"""
@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
