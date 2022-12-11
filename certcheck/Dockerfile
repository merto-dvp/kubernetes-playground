FROM python:alpine3.17

RUN mkdir -p /var/www/certchecker

COPY main.py /var/www/certchecker

RUN pip3 install flask
RUN pip3 install pyopenssl

ENTRYPOINT ["python3","/var/www/certchecker/main.py"]