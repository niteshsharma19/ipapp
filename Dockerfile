FROM redhat/ubi8

RUN yum install python3 -y

RUN python3 -m pip install --upgrade pip

RUN pip3 install flask

COPY myappip.py /myappip.py

CMD ["python3" ,"./myapp.py"]
