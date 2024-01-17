FROM python:3.12.1
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD python3 FlaskMorkAPI.py

