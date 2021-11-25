from test1 import client
from  gridfs import  GridFS
from  bson.objectid import ObjectId
db = client.school
gfs = GridFS(db,collection="book")

rs = gfs.exists(ObjectId("619dfa84ffaccd534b52346f"))
print(rs)
rs = gfs.exists(**{"filename":"GRFS的测试文件呀.pdf"})
print(rs)