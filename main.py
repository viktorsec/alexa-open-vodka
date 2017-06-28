from __future__ import print_function

def build_speechlet_response(output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet",
            'content': "SessionSpeechlet - " + output
        },
        'shouldEndSession': should_end_session
    }

def build_response(speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': speechlet_response
    }

def get_welcome_response():
    speech_output = "<speak><audio src='https://s3.amazonaws.com/viktorsec/output.mp3'/></speak>"
    return build_response(build_speechlet_response(
        speech_output, True))

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return get_welcome_response()
