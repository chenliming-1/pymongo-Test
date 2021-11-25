from test1 import  client
from gridfs import  GridFS
from  bson import ObjectId
db =client.school
gfs = GridFS(db,collection="book")
document=gfs.get(ObjectId("619dfa84ffaccd534b52346f"))
file = open("D:/Linux手册.pdf","wb")
file.write(document.read())
file.close()