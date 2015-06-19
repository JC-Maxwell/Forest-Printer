# ============== IMPORT MODULES

# NATIVE
import sys
import subprocess
import os

# EXTERNAL
import logging
import pdfkit

# DEVELOPMENT
from Modules import helper
from Modules import constants as K

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

		# url = 'https://wallstreetmx.cloudapp.net:3030/cfdi?transactionId='+transaction_id;

		url = 'https://corebook.me/cfdi?transactionId='+transaction_id;
		
		pdf = K.PDF_STORAGE +transaction_id+'.pdf'
		
		logger.info(pdf)	
		logger.info(url)

		if helper.transaction_is_stored_in_path(K.PDF_STORAGE,transaction_id) == True:
			logger.info("Deleted File")
			helper.remove_file(K.PDF_STORAGE+transaction_id+'.pdf')
		
		# pdfkit.from_url(url,pdf)
		# process = subprocess.Popen(['wkhtmltopdf','--page-size','Letter',url,pdf])
		process = subprocess.Popen(['wkhtmltopdf','--page-size','Letter',url,pdf])
		
		retcode = process.wait()
		
		if(retcode == 1):
			if helper.transaction_is_stored_in_path(K.PDF_STORAGE,"E" + transaction_id) != True:
				os.rename(pdf, K.PDF_STORAGE + "E" + transaction_id+'.pdf')
			pdf = K.PDF_STORAGE + "E" + transaction_id+'.pdf'

		response = Success(pdf);
	except:
		# Extract Error
		e = str(sys.exc_info()[0]) + ' ' + str(sys.exc_info()[1])
		# Send to LOGS
		logger.critical('Internal Error ' + e)
		# Instance of ERROR
		response = Error(http_code['internal'],e)
	#Send response:
	return response