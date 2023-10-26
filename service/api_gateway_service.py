import os
import boto3

from config.get_logger import Logger
from config.get_properties import EnvironmentRead

log = Logger.get_log()
env = os.environ.get('ENV')
env_reader = EnvironmentRead(env)
ENV, _config = env_reader.get_all()


class ApiGatewayService:

    def __init__(self):
        log.info('{}{}{}'.format('ApiGatewayService:: Enter:: ', 'create_api:: ', ENV))
        if ENV.casefold() == "DEV".casefold():
            self._api_gateway = boto3.client('apigateway', region_name=_config[ENV]['region'],
                                             endpoint_url=_config[ENV]['aws_endpoint_url'],
                                             aws_access_key_id='test',
                                             aws_secret_access_key='test')
        else:
            self._api_gateway = boto3.resource('apigateway', region_name=_config[ENV]['region'])

    def create_api(self):
        log.info('{}{}'.format('APP:: Enter:: ', 'create_api:: '))
        response = self._api_gateway.create_rest_api(
            name='test_1',
            description='localstack api_gateway',
            version='v.0.0.1'
        )
        log.info('{}{}{}{}'.format('Enter:: ', 'create_api:: ', 'response: ', response))
        return response
