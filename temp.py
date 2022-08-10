import json

with open('temp.json','r',encoding='utf-8') as file:
    data = json.load(file)
    data2=data['action']['detailParams']
    school=data2['sys_constant']['value']
    age = data2['sys_number_age']['value']
    location = data2['sys_location']['value']
    print(school)
    print(age)
    print(location)