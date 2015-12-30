import abc

class AlexaBaseHandler(object):
    """
    Base class for a python Alexa Skill Set.  Concrete implementations
    are expected to implement the abstract methods.

    See the following for Alexa details:
    https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def on_launch(self, launch_request, session):
        """
        Implement the LaunchRequest
        :param launch_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_session_started(self, session_started_request, session):
        pass

    @abc.abstractmethod
    def on_intent(self, intent_request, session):
        """
        Implement the IntentRequest
        :param intent_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_session_ended(self, session_end_request, session):
        """
        Implement the SessionEndRequest
        :param session_end_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    def process_request(self, event, context):
        """
        Helper method to process the input Alexa request and
        dispatch to the appropriate on_ handler
        :param event:
        :param context:
        :return: response from the on_ handler
        """
        # if its a new session, run the new session code
        response = None
        if event['session']['new']:
            self.on_session_started({'requestId': event['request']['requestId']}, event['session'])

        # regardless of whether its new, handle the request type
        if event['request']['type'] == "LaunchRequest":
            response = self.on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            response = self.on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            response = self.on_session_ended(event['request'], event['session'])

        return response

# --------------- Helpers that build all of the responses ----------------------
    def _build_speechlet_response(self, card_title, card_output, speech_output, reprompt_text, should_end_session):
        """
        Internal helper method to build the speechlet portion of the response
        :param card_title:
        :param card_output:
        :param speech_output:
        :param reprompt_text:
        :param should_end_session:
        :return:
        """
        return {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech_output
            },
            'card': {
                'type': 'Simple',
                'title': card_title,
                'content': card_output
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                }
            },
            'shouldEndSession': should_end_session
        }

    def _build_response(self, session_attributes, speechlet_response):
        """
        Internal helper method to build the Alexa response message
        :param session_attributes:
        :param speechlet_response:
        :return:
        """
        return {
            'version': '1.0',
            'sessionAttributes': session_attributes,
            'response': speechlet_response
        }
