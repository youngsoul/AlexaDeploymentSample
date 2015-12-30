import unittest
import inspect
from AlexaBaseHandler import AlexaBaseHandler


class TestAlexaHandler(AlexaBaseHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def on_launch(self, launch_request, session):
        print(inspect.stack()[0][3])

    def on_session_started(self, session_started_request, session):
        print(inspect.stack()[0][3])

    def on_intent(self, intent_request, session):
        print(inspect.stack()[0][3])

    def on_session_ended(self, session_end_request, session):
        print(inspect.stack()[0][3])


class AlexaParticleTests(unittest.TestCase):
    def test_session_new(self):
        print('-----------------------' + inspect.stack()[0][3])
        event = {
            'session': {
                'new': True
            },
            'request':{
                'type': 'LaunchRequest',
                'requestId': 'request_1'
            }
        }

        alexa = TestAlexaHandler()
        alexa.process_request(event, None)

    def test_session_old(self):
        print('-----------------------' + inspect.stack()[0][3])
        event = {
            'session': {
                'new': False
            },
            'request':{
                'type': 'LaunchRequest',
                'requestId': 'request_1'
            }
        }

        alexa = TestAlexaHandler()
        alexa.process_request(event, None)

    def test_session_new_intent(self):
        print('-----------------------' + inspect.stack()[0][3])
        event = {
            'session': {
                'new': True
            },
            'request':{
                'type': 'IntentRequest',
                'requestId': 'request_1'
            }
        }

        alexa = TestAlexaHandler()
        alexa.process_request(event, None)

    def test_session_new_end(self):
        print('-----------------------' + inspect.stack()[0][3])
        event = {
            'session': {
                'new': True
            },
            'request':{
                'type': 'SessionEndedRequest',
                'requestId': 'request_1'
            }
        }

        alexa = TestAlexaHandler()
        alexa.process_request(event, None)
