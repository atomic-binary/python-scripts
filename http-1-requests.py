# Simple code to send an HTTP request to URL and read response using requests module.
# Will make changes to the code so it will ask user for the URL and take it from the input.

import requests

r = requests.get('http://ptl-e0182623-7d83ed8f.libcurl.so/pentesterlab')

print(r.text)
