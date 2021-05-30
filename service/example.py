import sqlite3
from flask import Flask, Config, jsonify
from flask.views import View
from flask_injector import FlaskInjector, request
from injector import inject

app = Flask(__name__)

# Configure your application by attaching views, handlers, context processors etc.:

@app.route("/bar")
def bar():
    return jsonify("bar.html")


# Route with injection
@app.route("/foo")
def foo(db: sqlite3.Connection):
    users = db.execute('SELECT * FROM users').all()
    return jsonify("foo.html")


# Class-based view with injected constructor
class Waz(View):
    @inject
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def dispatch_request(self, key):
        users = self.db.execute('SELECT * FROM users WHERE name=?', (key,)).all()
        return 'waz'

app.add_url_rule('/waz/<key>', view_func=Waz.as_view('waz'))


# In the Injector world, all dependency configuration and initialization is
# performed in modules (https://injector.readthedocs.io/en/latest/terminology.html#module).
# The same is true with Flask-Injector. You can see some examples of configuring
# Flask extensions through modules below.

# Accordingly, the next step is to create modules for any objects we want made
# available to the application. Note that in this example we also use the
# Injector to gain access to the `flask.Config`:

def configure(binder):
    binder.bind(
        sqlite3.Connection,
        to=sqlite3.Connection(':memory:'),
        scope=request,
    )

# Initialize Flask-Injector. This needs to be run *after* you attached all
# views, handlers, context processors and template globals.

FlaskInjector(app=app, modules=[configure])

# All that remains is to run the application

app.run()