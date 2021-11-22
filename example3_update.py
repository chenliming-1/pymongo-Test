from test1 import client
#修改多条数据
client.school.teacher.update_many(
    {},{"$set":{"role":["班主任"]}}

)
#修改单条数据
client.school.teacher.update_one({"name":"李璐"},{"$set":{"sex":"女"}})
client.school.teacher.update_one({"name":"李璐"},{"$push":{"role":"年级主任"}})





