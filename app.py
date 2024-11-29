from api import *
from flask_session import Session
from flask import Flask

sess = Session()


if __name__=='__main__':
    app.secret_key='secret'
    app.run()


