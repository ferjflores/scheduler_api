FROM python:3.9
MAINTAINER Fernando Flores "ferjflores@gmail.com"
WORKDIR /scheduler_api
ADD . /scheduler_api
RUN pip install -r requirements.txt
CMD ["python","run.py"]