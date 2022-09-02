from sqlite3 import connect
from flask import session, Flask, request
import secrets

server = Flask(__name__)
secret_key = secrets.token_hex(16)
server.config['SECRET_KEY'] = secret_key


@server.route("/login")
def login():
    args = request.args
    username = args.get('username', default='', type=str)
    password = args.get('password', default='', type=str)

    db = connect('mrrobot.db')
    cursor = db.cursor()

    cursor.execute(
      f"SELECT * FROM mrrobot_user WHERE username = '{username}' AND password = '{password}'"
    )

    record = cursor.fetchone()
    if record:
        session['logged_user'] = username

    db.close()

    return f'welcome to fsoc {username}'
