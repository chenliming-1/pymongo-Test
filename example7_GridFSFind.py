from test1 import client
from  gridfs import  GridFS
import  math
import datetime
db = client.school
gfs = GridFS(db,collection="book")
book = gfs.find_one({"filename":"GRFS的测试文件呀.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM"%math.ceil(book.length/1024/1024))
# 查询：find函数

books = gfs.find({"type":"PDF"})
for one in  books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    # uploadDate = uploadDate.strftime("%Y-%m%-%d %H:%M:%S")
    # print(one._id,one.filename,uploadDate)
    print(uploadDate)




