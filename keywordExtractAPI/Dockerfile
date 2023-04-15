FROM python:3.8 

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim # docker 안에서 vi 설치 안해도됨

RUN mkdir /srv/docker-server # docker안에 srv/docker-server 폴더 생성
ADD . /srv/docker-server 

WORKDIR /srv/docker-server 

RUN pip install --upgrade pip # pip 업글

Run apt install default-jdk -y # java 설치

RUN pip --no-cache-dir install -r requirements.txt # 필수 패키지 설치
Run pip --no-cache-dir install tensorflow

#Run pip install mysqlclient #mysql

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
