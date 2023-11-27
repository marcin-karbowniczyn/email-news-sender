import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

api_key = os.getenv('API_KEY')
topic = 'tesla'

url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-10-27&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get(url)  # This method creates "request object type"

# Get a dictionary with a data
content = request.json()  # This method converts the response into dict type. This will throw an error if response cannot be converted into dict from json.

# Access article titles and descriptions and construct a email content out of it
message = ''
for article in content['articles']:
    if article['title'] is not None:
        message = message + article['title'] + '\n' + article['description'] + '\n' + '\n'

    # message = message + f"""
    # {article['title']}
    # {article['description']}
    # """

message = message.encode('utf-8')
send_email(message)
