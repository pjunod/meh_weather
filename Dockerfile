FROM python:3.11
EXPOSE 5050
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]
