from pymongo import MongoClient 

uri = "mongodb://admin:duc123@ds143971.mlab.com:43971/c4e23"
client = MongoClient(uri)
db = client.get_default_database()
blog = db["blog"]

post = {
'title':"Yeah"
}
blog.insert_one (post)