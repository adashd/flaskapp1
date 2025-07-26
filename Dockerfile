FROM redhat/ubi8

RUN yum install python36 -y

RUN pip3 install flask

COPY app.py .

ENTRYPOINT [ "python3", "app.py"]
