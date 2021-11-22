from test1 import client

teachers = client.school.teacher.find({}).skip(0).limit(10)

teachers =client.school.teacher.distinct("name")

teachers =client.school.teacher.find().sort([("name",-1)])