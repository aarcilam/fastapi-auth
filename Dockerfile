FROM python:3.9
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add --no-cache bash
ADD requirements.txt $APP_HOME
RUN pip install -r $APP_HOME/requirements.txt
# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

COPY src/ $APP_HOME
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
