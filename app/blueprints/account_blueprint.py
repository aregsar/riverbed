from flask import Blueprint

account = Blueprint('account', __name__)


@account.route("/account/signup/")
def signup():
    return "signup"

@account.route("/account/signin/")
def signin():
    return "signin"

@account.route("/account/signout/")
def signout():
    return "signout"


