import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

api_key = os.getenv('API_KEY')
topic = 'tesla'
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make a request
response = requests.get(url)  # This method creates "request object type"

# Get a dictionary with a data
content = response.json()  # This method converts the response into dict type. This will throw an error if response cannot be converted into dict from json.

# Access article titles and descriptions and construct a email content out of it. Limit e-mails to 20.
message = 'Subject: Daily News Digest' + '\n'
for index, article in enumerate(content['articles'][:20]):
    if article['title'] is not None and article['title'] != '[Removed]':
        # message = message + article['title'] + '\n' + article['description'] + 2*'\n'
        message = message + f"""
        {index + 1}. {article['title']}
        {article['description']}
        {article['url']}
        """

message = message.encode('utf-8')
send_email(message)
