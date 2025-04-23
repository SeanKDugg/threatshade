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
@app.route('/contact-us/', methods=['GET','POST'])
def contact():
    contact_data=data['contact'][0]
    return render_template('contact.html', paragraph1=contact_data['paragraph1'])


"""
Defines the route for services page and passes json data to template
"""
@app.route('/privacy-policy/')
def privacy_policy():

    intro = data['policy'][0]
    info_we_collect = data['policy'][1]
    how_we_use_info = data['policy'][2]
    sharing_info = data['policy'][3]
    data_security = data['policy'][4]
    your_rights = data['policy'][5]
    policy_changes = data['policy'][6]
    contact_us = data['policy'][7]

    return render_template(
        'privacy-policy.html',
        intro_title=intro['title'],
        intro_paragraph=intro['paragraph1'],

        collect_title=info_we_collect['title'],
        collect_intro=info_we_collect['paragraph1'],
        collect_bullets=[
            info_we_collect['paragraph2'],
            info_we_collect['paragraph3'],
            info_we_collect['paragraph4'],
        ],

        use_title=how_we_use_info['title'],
        use_intro=how_we_use_info['paragraph1'],
        use_bullets=[
            how_we_use_info['paragraph2'],
            how_we_use_info['paragraph3'],
            how_we_use_info['paragraph4'],
            how_we_use_info['paragraph5'],
            how_we_use_info['paragraph6'],
            how_we_use_info['paragraph7'],
            how_we_use_info['paragraph8'],
            how_we_use_info['paragraph9'],
        ],

        share_title=sharing_info['title'],
        share_intro=sharing_info['paragraph1'],
        share_bullets=[
            sharing_info['paragraph2'],
            sharing_info['paragraph3'],
            sharing_info['paragraph4'],
            sharing_info['paragraph5'],
            sharing_info['paragraph6'],
        ],

        security_title=data_security['title'],
        security_paragraph=data_security['paragraph1'],

        rights_title=your_rights['title'],
        rights_intro=your_rights['paragraph1'],
        rights_bullets=[
            your_rights['paragraph2'],
            your_rights['paragraph3'],
            your_rights['paragraph4'],
            your_rights['paragraph5'],
            your_rights['paragraph6'],
            your_rights['paragraph7'],
        ],

        changes_title=policy_changes['title'],
        changes_paragraph=policy_changes['paragraph1'],

        contact_title=contact_us['title'],
        contact_intro=contact_us['paragraph1'],
        contact_methods=[
            contact_us['paragraph2'],
            contact_us['paragraph3'],
            contact_us['paragraph4'],
        ]
    )

"""
Handles 404 error
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404

if __name__ == "__main__":
    app.run(debug=True)
