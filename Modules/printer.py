# ============== IMPORT MODULES

# NATIVE
import sys
import subprocess

# EXTERNAL
import logging
import pdfkit

# DEVELOPMENT

# ============== IMPORT CLASSES
from Classes.response import Success
from Classes.response import Error
from Classes.response import http_code

# ============== DEFINE VARIABLES AND CONSTANTS

# VARIABLES

# CONSTANST

# DEFINE LOGS
logger = logging.getLogger('root')

def pdf(params):
	logger.info('Start function')
	try:
		# Get params:
		transaction_id = params['transactionId']
		url = 'https://corebook.me:3030/cfdi?transactionId='+transaction_id;
		pdf = '/tmp/'+transaction_id+'.pdf'
		logger.info(url)
		# pdfkit.from_url(url,pdf)
		process = subprocess.Popen(['wkhtmltopdf','--page-size','Letter',url,pdf])
		retcode = process.wait()
		response = Success(transaction_id+'.pdf');
	except:
		# Extract Error
		e = str(sys.exc_info()[0]) + ' ' + str(sys.exc_info()[1])
		# Send to LOGS
		logger.critical('Internal Error ' + e)
		# Instance of ERROR
		response = Error(http_code['internal'],e)
	#Send response:
	return response