# Module for Constants

FIRMWARE_URL = 'http://25.138.146.114/firmware'

DOWNLOAD_PATH = '/tmp/Forest/'

VALID_STATUS = 'valid'
CANCELED_STATUS = 'canceled'
SYNCHRONIZING_FROM_THE_BEGINING = 'from_begining'
KEEPING_SYNCHRONIZING = 'keeping_syncrhonizing'

FISCAL_STATUS = {
	'Vigente' : VALID_STATUS,
	'Cancelado' : CANCELED_STATUS
}

# BILLS
RECEIVED_BILL = 1
ISSUED_BILL = 2
BILL_TYPE = {
	'issued' : ISSUED_BILL,
	'received' : RECEIVED_BILL
}

# RESPONSE
ERROR = 0
SUCCESS = 1
RESPONSE_TYPE = {
	'Success' : SUCCESS,
	'Error' : ERROR
}

# SEARCH_BILL_BY
DATE = 1
UUID = 2
SERACH_BILLS_BY = {
	'date' : DATE,
	'uuid' : UUID
} 

AUTHORIZED = 'Authorized'
UNAUTHORIZED = 'Unauthorized'

ONE_MONTHS_PERIOD = 1;
TWO_MONTHS_PERIOD = 2;

