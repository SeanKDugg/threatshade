import json
from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')


"""
Reads json file with page contents
"""
with open('text_content.json', encoding="utf-8") as json_file:
    data = json.load(json_file)

"""
Defines the route for index page and passes json data to template
"""
@app.route('/')
def index():

    schedule_assessment = data['index'][0]
    about = data['index'][1]

    return render_template(
        'index.html',
        paragraph1=schedule_assessment['paragraph1'],
        paragraph2=schedule_assessment['paragraph2'],
        paragraph3=about['paragraph1']
    )

"""
Defines the route for services page and passes json data to template
"""
@app.route('/services/')
def services():
    
    penetration_testing = data['services'][0]
    vulnerability_scanning = data['services'][1]
    threat_modelling = data['services'][2]

    return render_template(
        'services.html',
        paragraph1=penetration_testing['paragraph1'],
        paragraph2=penetration_testing['paragraph2'],
        paragraph3=vulnerability_scanning['paragraph1'],
        paragraph4=vulnerability_scanning['paragraph2'],
        paragraph5=threat_modelling['paragraph1'],
        paragraph6=threat_modelling['paragraph2']
    )

"""
Defines the route for contact page and passes json data to template
"""
@app.route('/contact-us/')
def contact():
    return render_template('contact.html', contact=data['contact'][0])

"""
Handles 404 error
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404

if __name__ == "__main__":
    app.run(debug=True)
