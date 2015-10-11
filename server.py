from flask import Flask
from flask import render_template, url_for
import os
app = Flask(__name__)

def get_paths():
	return {
		"bootstrap_css": url_for('static', filename="bootstrap/dist/css/bootstrap.min.css"),
		"bootstrap_js": url_for('static', filename="bootstrap/dist/js/bootstrap.min.js"),
		"jquery": url_for('static', filename="js/jquery-2.1.4.min.js"),
		"feed_css": url_for('static', filename="css/feed.css"),
		"generate_feed": url_for('static', filename="js/generate_feed.js"),
		"generate_home": url_for('static', filename="js/generate_home.js"),
		'moment': url_for('static', filename="js/moment.js")
	}

def search_jsons():
	return [file[:-5] for file in os.listdir("static/json") if file.endswith(".json")]

@app.route('/')
def choose_json():
	return render_template('index.html', jsons=','.join(['"{}"'.format(json_name) for json_name in search_jsons()]), **get_paths())

@app.route('/<json_name>')
def root(json_name):
    return render_template('recommendations.html', json_path = url_for('static', filename="json/{}.json".format(json_name)), **get_paths())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
