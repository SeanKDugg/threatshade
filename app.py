import json
from flask import Flask, render_template


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

"""
Defines the route for services page
"""
@app.route('/services/')
def services():
    return render_template('services.html', data=data)

"""
Defines the route for contact page
"""
@app.route('/contact-us/')
def contact():
    return render_template('contact.html', data=data)

"""
Handles 404 error
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404

if __name__ == "__main__":
    app.run(debug=True)
