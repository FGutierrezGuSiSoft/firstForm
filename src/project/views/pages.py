from flask import Blueprint, render_template, redirect, request


pages_blueprint = Blueprint('pages', __name__)


@pages_blueprint.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@pages_blueprint.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@pages_blueprint.route('/login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if is_empty(email) or is_empty(password):
        return redirect("/", code=302)

    return redirect("/view", code=302)


def is_empty(value):
    return value is None or value.strip() == ""


@pages_blueprint.route('/register', methods=['POST'])
def do_register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirmation = request.form.get('confirmation')

    if is_empty(name) or is_empty(email) or is_empty(password) or is_empty(confirmation):
        return redirect("/register", code=302)

    return redirect("/", code=302)


@pages_blueprint.route('/view', methods=['GET'])
def view():
    return render_template('view.html')
