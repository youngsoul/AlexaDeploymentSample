import logging
from AlexaDeploymentHandler import AlexaDeploymentHandler

"""
Main entry point for the Lambda function.
In the AWS Lamba console, under the 'Configuration' tab there is an
input field called, 'Handler'.  That should be:  main.lambda_handler

Handler: main.lambda_handler
Role: lambda_basic_execution

"""

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info("Executing main lambda_handler for AlexaDeploymentHandler class")

    alexa = AlexaDeploymentHandler()
    alexa_response = alexa.process_request(event, context)

    return alexa_response



