FROM python:3

ADD . .

RUN pip3 install -r requirements.txt
RUN pip3 install sklearn

RUN adduser -D myuser
USER myuser 

CMD ["python3","-u","api.py"]