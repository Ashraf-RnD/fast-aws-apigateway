from fastapi import FastAPI

from config.get_logger import Logger
from service.api_gateway_service import ApiGatewayService

app = FastAPI()

log = Logger.get_log()

api_gateway_service = ApiGatewayService()


@app.get("/fast/api/ping")
def read_root():
    return {"ping": "pong"}


@app.post("/fast/api/create-api")
def create_api():
    log.info('{}{}'.format('APP:: Enter:: ', 'create_api:: '))
    return api_gateway_service.create_api()
