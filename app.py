import json
from flask import Flask,render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
import models
from models import db


app = Flask(__name__)
app.debug = True
app.config.from_json('config.json')
app.secret_key = bytes(app.config['SECRET_KEY'], 'UTF-8')
db.init_app(app)
migrate = Migrate(app, db)

def create_app():
    """Construct the core application."""
    with app.app_context():
        # Create tables for our models
        db.create_all()
        return app
create_app()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/view", methods=['GET'])
def view_db():
    data = models.MainDB.query.all()
    table_name = models.MainDB.__tablename__
    columns = models.MainDB.metadata.tables[table_name].columns.keys()
    return render_template('view.html', table_data=data, columns=columns, table_name=models.MainDB.__tablename__)

@app.route("/update", methods=['POST'])
def update_db():
    data = request.form
    resp_dict = dict(data)  # retrieve data from front-end
    return json.dumps({'status':'OK'});

@app.route("/add",methods=['GET', 'POST'])
def add_data():
    if request.method == "POST":
        form_data = request.form
        with open('form-data.json', 'w') as file:
            json.dump(dict(form_data), file, indent=2)

            main_db = models.MainDB(**dict(form_data))
            db.session.add(main_db)
            db.session.commit()
            flash("Data Updated successfully!")
            print("redirect url:", request.url)
        return redirect(url_for('add_data'))
    return render_template('add_data.html', columns = models.MainDB.fields)


if __name__ == '__main__':
    app.run(host="localhost")
