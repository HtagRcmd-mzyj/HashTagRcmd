# HashTag Recommand Web Project

이미지 파일을 업로드하거나 텍스트를 입력했을 때, `키워드`를 추출한 후 해당 키워드와 관련된 `해시태그`들을 인스타그램의 크롤링을 통하여 추천해주는 웹 프로젝트입니다.

### 📍 개요
- 프로젝트명: 이미지와 텍스트 기반의 연관된 해시태그 추천 시스템 
- 프로젝트 기간 : 2022.07 ~ 2022.10
- 프로젝트 참여인원 
    | [권용준](https://github.com/dydwns99) | [류민지](https://github.com/mxnzx) |
- 데모 영상(이미지) : https://youtu.be/8OCdgybDq0M
- 데모 영상(텍스트) : https://youtu.be/mVVpacQGOwE 

### 📍 사용 기술
|  |  |
| --- | --- |
| 언어 | Python3, HTML/CSS, Javascript |
| 프레임워크 | Django, React |
| 서버 | Amazon EC2, Docker |
| DB | MySQL |
| API 및 라이브러리 | Restful API, axois |

### 📍 웹 프로젝트 이용 방법

- 메인 화면(이미지 등록)
   1. 사용자가 이미지를 업로드합니다. (.jpg, .jpeg, .git 가능)
   2. `해시태그생성하기` 버튼을 클릭합니다.

        <img  alt="1_upload_image" src="https://user-images.githubusercontent.com/77240765/234433942-4ba81fb7-34dd-41b2-9fc6-36bebb3924f0.png">

   3. 추천 해시태그가 체크박스와 함께 표시되면 사용자는 원하는 해시태그를 선택합니다.
    (지역명이 추출되었다면, 지역명과 키워드를 함께 붙인 해시태그도 함께 출력됩니다.)
         
        <img alt="3_pickHashtag_fullshot" src="https://user-images.githubusercontent.com/77240765/234433568-7d27da3f-7d83-4318-906f-12818269367f.png">
        
   4. 복사버튼 및 드래그를 통해 해당 해시태그를 복사하여 원하는 곳에 붙일 수 있습니다.
        
        <img width="60%" alt="4_pickHashTag" src="https://user-images.githubusercontent.com/77240765/234430572-dcb05e0b-14f6-44a9-b6a5-07069d199cc6.png">

    
- 텍스트 등록
    1. 사용자가 글을 입력합니다.
    2. `해시태그생성하기` 버튼을 클릭합니다.
        <img alt="2_1_write_text" src="https://user-images.githubusercontent.com/77240765/234434118-a6572c00-e432-4618-a56f-a0c934e8efe3.png">
    3. 추천 해시태그가 체크박스와 함께 표시되면 사용자는 원하는 해시태그를 선택합니다.  
    4. 복사버튼 및 드래그를 통해 해당 해시태그를 복사하여 원하는 곳에 붙일 수 있습니다.  

        <img  alt="2_2_pick_hashtag" src="https://user-images.githubusercontent.com/77240765/234433763-cf5734c4-ed74-47b3-a01f-fa69920f1c84.png">


### 📍 실행방법

- frontend 실행  
```
docker build -t 이미지이름
docker run -p 3000:3000 이미지이름
```
- keywordExtractAPI 와 nginx 실행
```
docker-compose up -d --build
```
- crawlingAPI 실행
```
docker build -t 이미지이름
docker run -p 8080:8080 이미지이름
```

### 📍 디렉토리 기능
- frontend/

>화면을 보여주는 기능을 한다.
> 
> keywordExtractAPI 와 crawlingAPI 에 데이터를 전송하고 받아 원하는 값을 화면에 보여준다.
- keywordExtractAPI/
>키워드를 출력하는 기능을 한다.
> 
>이미지 데이터의 경우 이미지에 맞는 키워드를 추출하여 crawlingAPI로 전송 한다.
텍스트 데이터의 경우 keyBERT 모델을 사용하여 추천 키워드들을 바로 추출 한다.
- crawlingAPI/
>이미지 키워드로 크롤링하고 위치정보 추출하는 기능을 한다. 
> 
> 크롤링을 통한 빈도수 기반 상위 n개의 해시태그를 반환하고 이미지의 위치 정보를 추출하여 해시태그로 반환한다.
- nginx/
>웹서버로써 정적인 리소스를 처리하는 기능을 한다.
- log/
>웹서버로 보낸 http 요청, 반응, 에러에 대한 정보들을 기록하여 저장하는 저장소 역할을 한다.
---
### 📍 디렉토리 구조
```
├── README.md
├── crawlingAPI/
│   ├── Dockerfile
│   ├── crawling/
│   ├── crawling_server/
│   ├── db.sqlite3
│   ├── google-chrome-stable_current_amd64.deb
│   ├── manage.py
│   ├── requirements.txt
│   ├── templates/
│   └── test.jpg
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── README.md
│   ├── media/
│   ├── node_modules/
│   ├── package-lock.json
│   ├── package.json
│   ├── public/
│   ├── src/
│   └── yarn.lock
├── keywordExtractAPI/
│   ├── Dockerfile
│   ├── README.md
│   ├── __pycache__/
│   ├── apps.sock=
│   ├── db.sqlite3
│   ├── djangoProject/
│   ├── docker-compose.yml
│   ├── eff_model/
│   ├── keyBERT_model/
│   ├── manage.py
│   ├── media/
│   ├── requirements.txt
│   ├── sqlite3.exe
│   └── uwsgi.ini
├── log/
│   ├── access.log
│   ├── error.log
│   └── uwsgi.log
└── nginx/
    ├── Dockerfile
    ├── nginx-app.conf
    └── nginx.conf
```

