from test1 import client
from  gridfs import  GridFS
db = client.school
gfs = GridFS(db,collection="book")

file = open("D:/GRFS的测试文件呀.pdf","rb")
args = {"type":"PDF","keyword":"linux"}
gfs.put(file,filename="GRFS的测试文件呀.pdf",**args)
file.close()

