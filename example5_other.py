from test1 import client
#查询数据分页选取前十条
teachers = client.school.teacher.find({}).skip(0).limit(10)
for one in teachers:
    print(one["_id"],one["name"])
#查询不重复的姓名
teachers =client.school.teacher.distinct("name")
for one in teachers:
    print(one)
#查询结果按名字降序排序sort([()])
teachers =client.school.teacher.find().sort([("name",-1)])
for one in teachers:
    print(one["_id"],one["name"])