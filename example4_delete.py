from test1 import client
try:
    #删除单条数据
    # client.school.teacher.delete_one({"name":"晨刚"})
    #删除多条数据
    client.school.teachers.delete_many({})
except Exception as e:
    print(e)


    