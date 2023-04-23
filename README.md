---
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
### 디렉토리 구조
