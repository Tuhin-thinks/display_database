# Flask_CRUD_Basic
Basic Flask webapplication to implement CRUD functionality to database.

## IMPORTANT

Create a `config.json` file in the local directory as the <a href="https://github.com/Tuhin-thinks/Flask_CRUD_Basic/blob/master/app.py">app.py</a>

`config.json` should have the following contents:
```json
{
  "TESTING": "",
  "FLASK_DEBUG": true,
  "SECRET_KEY": "some_really_secret_key",
  "SQLALCHEMY_DATABASE_URI": "postgresql://postgres_username:your_passwd@localhost:5432/TestDB",
```

  Or anything appropriate from flask sqlalchemy database URI. *(according to your choice of database) [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)*


```json
  "SQLALCHEMY_TRACK_MODIFICATIONS": false
}
```
Then run, `flask migrate` to migrate the database changes.
```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```
This will create all columns and tables in the databse name provided in the `SQLALCHEMY_DATABASE_URI`.

<hr>
To run the flask app in development server in debug mode:

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```
flask run should run the flask app in your <a href="http://127.0.0.1:5000" target="blank_">http://127.0.0.1:5000</a>