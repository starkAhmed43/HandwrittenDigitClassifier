FROM python:3.9.21-alpine3.21

WORKDIR /
COPY . /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5402
CMD ["python", "server.py"]