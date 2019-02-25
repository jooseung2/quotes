from datetime import datetime

def get_timestamp():
	return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
QUOTES = {
	"Ezreal": {
		"speaker" : "Ezreal",
		"quote" : "Time for a true display of skills!",
		"timestamp": get_timestamp()
	},
	"Vayne": {
		"speaker" : "Vayne",
		"quote" : "Let us hunt those who have fallen in darkness.",
		"timestamp": get_timestamp()
	}
}

# Create a handler for our read (GET) quotes
def read():
	"""
	This fn responds to a request for /api/quotes
	wit the complete lists of quotes
	
	:return:	sorted list of quotes
	"""
	return [QUOTES[key] for key in sorted(QUOTES.keys())]





