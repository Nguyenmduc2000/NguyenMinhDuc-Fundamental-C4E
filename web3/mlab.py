import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds263367.mlab.com:63367/ducad


host = "ds263367.mlab.com"
port = 63367
db_name = "ducad"
user_name = "admin"
password = "abc123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())