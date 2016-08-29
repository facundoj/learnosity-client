import os
import sys
import yaml

from bottle import app, route, run, request, abort, response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))

from learnosity_client import queryLearnosity

# Usage:
#   python app/learnosity-client.py <config-file.yml>

configFilePath = sys.argv[1]

with open(configFilePath, 'r') as configFile:
    config = yaml.load(configFile)

@route('/learnosity-proxy', method='POST')
def queryLearnosityService():
    data = request.body.read().decode("utf-8")

    if not data:
        abort(400, 'Please, specify your query')

    response.content_type = 'application/json'

    return queryLearnosity(config, data)

if __name__ == "__main__":
    # Start our bottle web server
    run(host='0.0.0.0', port=3000)
