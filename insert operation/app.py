from flask import Flask, render_template, request, redirect, url_for
from models import bukutelp

application = Flask(__name__)

@application.route('/')
def index():
	model = bukutelp()
	container = []
	container = model.selectDB()
	return render_template('index.html',
container=container)

@application.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        nama = request.form['nama']
        no_telp = request.form['no_telp']
        data = (nama, no_telp)
        model = bukutelp()
        model.insertDB(data)
        return redirect(url_for('index'))
    else:
        return render_template('insert_form.html')

if __name__ == '__main__':
	application.run(debug=True)
