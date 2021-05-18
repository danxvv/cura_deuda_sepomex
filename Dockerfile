FROM python:3.9.1-slim
ADD . /python-flask
WORKDIR /python-flask
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0