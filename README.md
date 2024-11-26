# Mahdix

Mahdix is a versatile Python library that offers various utilities for printing, generating logos, fetching HTML content, making HTTP requests, and more. This library is designed to simplify common tasks and enhance productivity in Python programming.

## Features

- Print text to the console
- Get the current time
- Generate text-based logos
- Generate random numbers
- Fetch HTML content from URLs
- Perform regex-based text searches
- Execute system commands
- Make HTTP GET and POST requests
- Randomly select items from a list
- Encode and decode Base64 strings
- Colorful console output
- Retrieve Facebook ID creation dates

## Installation

To use Mahdix, you can install it via pip:

```bash
pip install mahdix
```
# Project Description

## Print Something
```python
from mahdix import p

p('YOUR TXT')
```
# Get Current Time

```python
from mahdix import time

print(time())
```
# Generate Text Logo


```python
from mahdix import makelogo

logo = makelogo(text='Mahdi')
print(logo)
```
# Random Numbers
python
Copy code
from mahdix import random7, random8, random9, random1_2, random1_3, random1_4, random10

print(random7())
print(random8())
print(random9())
print(random1_2())
print(random1_3())
print(random1_4())
print(random10())

# html_req Function
The html_req function fetches HTML content from the specified URL, using optional headers and data for the request.
```python

from mahdix import html_req

url = 'https://example.com'
headers = {
    'User-Agent': 'Your User Agent',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
cookie = {'key': 'value'}  ## Optional Cookies for POST requests
data = {'key': 'value'}  ## Optional data for POST requests
params = {
    'q': 'params_valu',
}
# You can add json data: json_data={"json" : "value"}
parsed_html = html_req(url, Headers=headers, Data=data, Cookie=cookie, Params=params)  ## Data for POST requests
parsed_html = html_req(url, Headers=headers, Cookie=cookie, Params=params)  ## For GET requests
print(parsed_html)
```
# html_txt Function
The html_txt function fetches HTML content from any request response.
```python

from mahdix import html_txt
response = requests.get('https://example.com').text
text_html = html_txt(response)
print(text_html)  # Get response as HTML text
```
# search_as_re Function
This function searches for a specific text from any text using the re module.

```python
from mahdix import search_as_re

full_text = "This is some example text. Starting:apple, Finding:banana, Finding:orange, Ending:grape, Finding:pear,"  # Default value None
starting_text = "Starting:"  # Default value None
finding_text = "Finding:"  # Default value None
ending_text = ","  # Default value ','

# Using search_as_re
result_search = search_as_re(full_text, starting_text, ending_text)
print("Result from search_as_re:", result_search)

# Output: apple

```
# findall_as_re Function
This function finds a list of specific texts from any text and returns them.

```python
from mahdix import findall_as_re

full_text = "This is some example text. Starting:apple, Finding:banana, Finding:orange, Ending:grape, Finding:pear,"  # Default value None
starting_text = "Starting:"  # Default value None
finding_text = "Finding:"  # Default value None
ending_text = ","  # Default value ','

result_findall = findall_as_re(full_text, finding_text, ending_text)
print("Result from findall_as_re:", result_findall)

# Output: {'banana', 'pear', 'orange'}

```
#  System Commands
```python
from mahdix import sysT

sysT('YOUR COMMAND')
```
# HTTP Requests

```python
from mahdix import rqg, rqp

response_get = rqg('https://example.com')
response_post = rqp('https://example.com', data={'key': 'value'})
```
# Random Choices
```python
from mahdix import rc

print(rc([1, 2, 3, 4]))
Base64 Encoding/Decoding
```
```python
from mahdix import bsec, bsdc

encoded_data = bsec('Hello, World!')
decoded_data = bsdc(encoded_data)
```
# Colors

```python
# ---[coloure]------

RED = mahdix.RED
GREEN = mahdix.GREEN
YELLOW = mahdix.YELLOW
BLUE = mahdix.BLUE
ORANGE = mahdix.ORANGE
LI_BLUE = Light_BLUE
LI_MAGENTA = Light_MAGENTA
LI_CYAN = Light_CYAN
LI_WHITE = Light_WHITE
```
# Background Colors
```python
BG_BLACK = Background_BLACK
BG_RED = Background_RED
BG_GREEN = Background_GREEN
```
# Get Any Facebook ID Created Date

```python
from mahdix import getyearid

# Example: cid = '100000000023456'
print(getyearid(cid))
```
This should give you a comprehensive guide to all available functions in your project.
