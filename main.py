from bs4 import BeautifulSoup

with open('my_website.html', 'r') as html_file:
    content = html_file.read()
    print(content)
