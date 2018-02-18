FROM python:3.6.4-alpine3.4

RUN apk upgrade --no-cache

RUN pip install itchat pillow

COPY new_year_reply.py ./new_year_reply.py

ENV LOGLEVEL=info

CMD python ./new_year_reply.py -v ${LOGLEVEL}
