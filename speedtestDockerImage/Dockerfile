FROM python:3.8.9-alpine3.13
COPY . /app
WORKDIR /app
RUN pip install -r reqs.txt
VOLUME /app/db
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
