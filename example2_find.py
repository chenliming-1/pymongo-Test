from test1 import client
try:
    teachers = client.school.teacher.find({})
    for one in teachers:
        print("查找多条数据：",one["_id"],one["name"])
    teacher = client.school.teacher.find_one({"name":"李璐"})
    print("查找单条数据：",teacher["_id"],teacher["name"])
except Exception as e:
    print(e)