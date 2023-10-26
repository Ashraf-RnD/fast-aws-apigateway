FROM python:3.9
COPY ../requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /code
COPY .. .
RUN mkdir -p 'logs'
RUN touch 'logs/fast-aws-apigateway.log'
RUN touch 'logs/fast-aws-apigateway-ERROR.log'

ARG ENV=DEV
#CMD ["sh" ,"dev.sh"]
CMD ["uvicorn" ,"app:app" ,"--reload" ,"--host" ,"localhost" ,"--port", "9501"]