FROM python:3.7-alpine
ADD . /ui
WORKDIR /ui
ENV FLASK_APP ui.py
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5001
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
