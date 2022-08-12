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
        "listCard": {
          "header": {
            "title": "챗봇 관리자센터를 소개합니다."
          },
          "items": [
            {
              "title": "챗봇 관리자센터",
              "description": "새로운 AI의 내일과 일상의 변화",
              "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
              "link": {
                "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
              }
            },
            {
              "title": "챗봇 관리자센터",
              "description": "카카오톡 채널 챗봇 만들기",
              "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
              "action": "block",
              "blockId": "62654c249ac8ed78441532de",
              "extra": {
                "key1": "value1",
                "key2": "value2"
              }
            },
            {
              "title": "Kakao i Voice Service",
              "description": "보이스봇 / KVS 제휴 신청하기",
              "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
              "action": "message",
              "messageText": "Kakao i Voice Service",
              "extra": {
                "key1": "value1",
                "key2": "value2"
              }
            }
          ],
          "buttons": [
            {
              "label": "구경가기",
              "action": "block",
              "blockId": "62654c249ac8ed78441532de",
              "extra": {
                "key1": "value1",
                "key2": "value2"
              }
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

# 카카오톡 지역 이름 받아오기
@app.route('/api/whereLive', methods=['POST'])
def whereLive():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job']
    print(job)

    location=params_df['location']
    print(location)

    position=params_df['position']
    [print(position)]

    advantage=params_df['advantage']
    print(advantage)

    age=json.loads(params_df['sys_number'])['amount']
    print(age)
   


    
    

