from test1 import  client
from gridfs import  GridFS
from  bson import ObjectId
db = client.school
gfs = GridFS(db,collection="book")
gfs.delete(ObjectId("619dfa84ffaccd534b52346f"))
