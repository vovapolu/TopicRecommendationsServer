from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('recommendations.html', 
		bootstrap_path=url_for('static', filename="bootstrap/dist/css/bootstrap.min.css"), 
		json_path=url_for('static', filename="recommendation_samat.json"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
