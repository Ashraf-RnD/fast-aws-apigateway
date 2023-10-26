import boto3
import os

from config.get_logger import Logger
from config.get_properties import EnvironmentRead

log = Logger.get_log()
env = os.environ.get('ENV')
env_reader = EnvironmentRead(env)
ENV, _config = env_reader.get_all()


class ApiGatewayConfig:

    def __int__(self):
        if ENV.casefold() == "DEV".casefold():
            self._api_gateway = boto3.resource('apigateway', region_name=_config[ENV]['region'],
                                               endpoint_url=_config[ENV]['aws_endpoint_url'])
        else:
            self._api_gateway = boto3.resource('apigateway', region_name=_config[ENV]['region'])

    def get_api_gateway(self):
        return self._api_gateway
