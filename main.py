import requests
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv('API_KEY')

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-10-27&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get('https://acmilan.com.pl')  # This method creates "request object type"

# Get a dictionary with a data
content = request.json()  # This method converts the response into dict type. This will throw an error if response cannot be converted into dict from json.

# Access article titles and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])
