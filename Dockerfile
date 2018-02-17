FROM python:3.6.4-alpine3.4

RUN apk add --no-cache python jpeg-dev

RUN pip install itchat pillow

COPY new_year_reply.py ./new_year_reply.py

CMD ["python", "./new_year_reply.py"]
