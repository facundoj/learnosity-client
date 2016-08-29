import sys
import learnosity_sdk.request
import requests
import json

def queryLearnosity(config, queryStr):
    try:
        query = json.loads(queryStr)
    except ValueError:
        print 'Malformed query.'
        return None

    # Security configuration
    consumerKey     = config['security']['consumer_key']
    consumerSecret  = config['security']['consumer_secret']

    # Query details
    learnosityEnv   = config['details']['learnosity_env']
    endpoint        = config['details']['endpoint']

    security = {
        'consumer_key':     consumerKey,
        'domain':           'localhost'
    }

    # Generating Learnosity request
    init = learnosity_sdk.request.Init('data', security, consumerSecret,
        request=query, action='get')
    learnosityRequest = init.generate()

    response = requests.post(learnosityEnv + endpoint, data=learnosityRequest)
    response.connection.close()

    if response.status_code == 200 or response.status_code == 201:
        return response
    else:
        return {
            'error': 'Your query triggered an error',
            'response': json.loads(response.text)
        }
