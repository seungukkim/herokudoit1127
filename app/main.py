from flask import Flask, request
import json

# 메인 로직!! 
def cals(opt_operator, number01, number02):
    if opt_operator == "addition":
        return number01 + number02
    elif opt_operator == "subtraction": 
        return number01 - number02
    elif opt_operator == "multiplication":
        return number01 * number02
    elif opt_operator == "division":
        return number01 / number02

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody


# 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody


# 카카오톡 Calculator 계산기 응답
@app.route('/api/calCulator', methods=['POST'])
def calCulator():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df)) #dict
    opt_operator = params_df['operators']
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']
    print(type(params_df['sys_number01']))
    print(type(number01)) #int 
    
    # number03=params_df['sys_number01']['amount'] #왜 값이 안나올까?
    # print(type(number03))

    print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(cals(opt_operator, number01, number02))

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }

    return responseBody

# 카카오톡 지역 이름 받아오기
@app.route('/api/whereLive', methods=['POST'])
def whereLive():
    body = request.get_json()
    print(body)
    # print(type(body))#dict
    # print(type(body['action']))#dict
    # print(type(body['action']['detailParams']))#dict
    # print(type(body['action']['detailParams']['sys_number_age']))#dict
    # print(type(body['action']['detailParams']['sys_number_age']['value'])) #str

    # print(type(body['action']['params']))# dict
    # print(type(body['action']['params']['sys_number_age'])) #str
    params_df=body['action']['params']
    # temp1=json.loads(params_df['sys_number_age'])
    temp2=json.load(params_df['sys_location'])
    # params_df = body['action']['detailParams']
    # print(type(params_df))
    
    # age = json.loads(params_df['sys_number_age'])['value']
    # location = json.loads(params_df['sys_location'])['value']
    # print(age,type(age),location,type(location))
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": temp2
                    }
                }
            ]
        }
    }

    return responseBody
    

    # # params_df = body['action']['params']
    # params_df = body['action']
    # print(params_df)
    # print(type(params_df))
    # # params_df
    # param_df=json.loads(body)
    # a1=param_df['action']
    # print(a1)
    # print(type(a1))
    
    # a2=params_df['sys_number_age']
    # print(a2) 
    # print(type(a2)) #str
    # a3=params_df['sys_location']#서울
    # a3=json.loads(params_df['sys_location']) #에러 뜸
    # a3=json.loads(params_df)['sys_location'] # 에러 뜸
    # a3 = json.loads(params_df['params'])['sys_location']# 에러 뜸
    # print(a3) # 서울
    # print(type(a3)) # str
    # print(type(str(a3)))
    # a4= json.load(a3) #에러 
    # print(type(a4))
    # a4 = int(a2)
    # print(type(a4))
    
    # responseBody = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #             {
    #                 "simpleText": {
    #                     "text": a2,
    #                     "text": a3
    #                 }
    #             }
    #         ]
    #     }
    # }

    # return responseBody

