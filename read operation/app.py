from flask import Flask, render_template
from models import bukutelp

application = Flask(__name__)

@application.route('/')
def index():
	model = bukutelp()
	container = []
	container = model.selectDB()
	return render_template('index.html',
		container=container)

if __name__ == '__main__':
	application.run(debug=True)
