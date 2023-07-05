from mongoengine import connect

def db_connection():
    data = connect('medical', host='127.0.0.1', port=27017)
    if data:
        return "success"
    else:
        return "failure"