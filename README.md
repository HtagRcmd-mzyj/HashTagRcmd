### 실행방법

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
---  
### 디렉토리 기능
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
### 디렉토리 구조
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


