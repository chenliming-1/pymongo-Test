from test1 import client
# 插入单条数据
client.school.teachers.insert_one({"name":"李璐2","role":"兼职老师"})
#插入多条数据
client.school.teacher.insert_many([{"name":"晨刚"},{"name":"郭丽丽"}])
