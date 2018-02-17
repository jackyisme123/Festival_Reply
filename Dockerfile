FROM python:3.6.4-alpine3.4

RUN apk upgrade --no-cache

RUN apk add --no-cache jpeg-dev zlib-dev python3-dev gcc musl-dev

RUN pip install itchat pillow

COPY new_year_reply.py ./new_year_reply.py

CMD ["python", "./new_year_reply.py"]
