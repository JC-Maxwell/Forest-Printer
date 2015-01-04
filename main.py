# ============== IMPORT MODULES

# NATIVE
import sys
import json

# EXTERNAL
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import send_file
from flask import send_from_directory

# DEVELOPMENT
from Modules import log
from Modules import constants as K
from api import instructions as API

# ============== IMPORT CLASSES
from Classes.response import Success
from Classes.response import Error
from Classes.response import http_code

# ============== DEFINE VARIABLES, CONSTANTS AND INITIALIZERS

# VARIABLES

# CONSTANST

# DEFINE API CONSTRUCTOR
app = Flask(__name__)

# ======================================================== CODE MODULE

@app.route('/Forest/printer', methods=['POST'])
def api_post():
	try:
		# Send request to LOGS
		logger.info('Listen request')

		# DESERIALIZE REQUEST 
		request_data = json.loads(request.data)
		
		# VALIDATE REQUEST
		if (('instruction' in request_data) and ('params' in request_data)):
			# GET PARAMS
			instruction = request_data['instruction']
			params = request_data['params']
			# Send to LOGS
			logger.info('Call ' + instruction + ' function')
			# Execute INSTRUCTION
			result = API[instruction](params)
			# Define RESPONSE
			response = result.get_response()
		else:
			# Send to LOGS
			logger.info('Bad request')
			# Instance of ERROR s
			error = Error(http_code['bad_request'],'Instruction an Params are required')
			# Define RESPONSE
			response = error.get_response()
	except:
		# Extract Error
		e = str(sys.exc_info()[1])
		# Send to LOGS
		logger.critical('Internal Error ' + e)
		# Instance of ERROR
		error = Error(http_code['internal'],'Internal Server Error')
		# Define RESPONSE
		response = error.get_response()
	
	# SEND RESPONSE
	logger.info('End of request')
	return response

# @app.route('/printer/<instruction>/<transaction_id>')
# def api_get(instruction,transaction_id):

@app.route('/service/Forest/<instruction>')
def api_get(instruction):
	try:
		# Send request to LOGS
		logger.info('Listen request')

		# DESERIALIZE REQUEST 
		# request_data = json.loads(request.args)
		request_data = request.args

		# VALIDATE REQUEST
		if (request_data):
		# if(transaction_id):
			# GET PARAMS
			instruction = instruction
			params = request_data
			# Send to LOGS
			logger.info('Call ' + instruction + ' function')
			# Execute INSTRUCTION
			result = API[instruction](params)
			# Define RESPONSE
			# response = result.get_response()
			response = result.content
			logger.info(response)
			response = send_file(response, as_attachment=True)
		else:
			# Send to LOGS
			logger.info('Bad request')
			# Instance of ERROR s
			error = Error(http_code['bad_request'],'Instruction an Params are required')
			# Define RESPONSE
			response = error.get_response()
	except:
		# Extract Error
		e = str(sys.exc_info()[1])
		# Send to LOGS
		logger.critical('Internal Error ' + e)
		# Instance of ERROR
		error = Error(http_code['internal'],'Internal Server Error')
		# Define RESPONSE
		response = error.get_response()
	
	# SEND RESPONSE
	logger.info('End of request')
	return response
	

# MAIN
if __name__ == '__main__':

	# Define LOGGER
	logger = log.setup_custom_logger('root')
	logger.info('Start Forest API Server')

	# Intialize API	
	app.debug = True
	app.run(host='0.0.0.0',threaded=True, port=5010)