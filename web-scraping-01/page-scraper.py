from bs4 import BeautifulSoup

with open('my-website.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h2')
    print(tags)
