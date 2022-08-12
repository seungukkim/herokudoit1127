from cgi import parse_multipart
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
         "carousel": {
           "type": "listCard",
           "items": [
             {
               "header": {
                 "title": "샌드위치"
               },
               "items": [
                 {
                   "title": "햄치즈",
                   "description": "4,500원",
                   "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_01.jpg"
                 },
                 {
                   "title": "베이컨 아보카도",
                   "description": "5,500원",
                   "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_02.jpg"
                 },
                 {
                   "title": "에그 포테이토",
                   "description": "5,300원",
                   "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_03.jpg"
                 },
                 {
                   "title": "갈릭 베이컨 토마토",
                   "description": "5,800원",
                   "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_04.jpg"
                 }
               ],
               "buttons": [
                 {
                   "label": "더보기",
                   "action": "message",
                   "messageText" : "샌드위치 더보기"
                 }
               ]
             }           
           ]
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




    
    

