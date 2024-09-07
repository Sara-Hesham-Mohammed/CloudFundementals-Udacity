FROM python:3.12.4
LABEL maintainer = "Sara Hesham"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]