from flask import Flask
from flask import render_template, url_for
import os
app = Flask(__name__)

def search_jsons():
	return [file[:-5] for file in os.listdir("static/json") if file.endswith(".json")]

@app.route('/')
def choose_json():
	return render_template('index.html', 
		bootstrap_path=url_for('static', filename="bootstrap/dist/css/bootstrap.min.css"), 
		jsons=','.join(['"{}"'.format(json_name) for json_name in search_jsons()]))

@app.route('/<json_name>')
def root(json_name):
    return render_template('recommendations.html', 
		bootstrap_path=url_for('static', filename="bootstrap/dist/css/bootstrap.min.css"), 
		json_path=url_for('static', filename="json/{}.json".format(json_name)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
