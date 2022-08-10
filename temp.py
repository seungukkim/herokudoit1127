import json

with open('temp.json','r',encoding='utf-8') as file:
    data = json.load(file)
    data2=data['action']['params']
    school=data2['sys_constant']
    age = data2['sys_number_age']
    location = data2['sys_location']
    print(school)
    print(age)
    print(location)