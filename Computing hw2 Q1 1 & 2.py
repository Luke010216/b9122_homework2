#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

seed_url = 'https://press.un.org/en'
keyword = 'crisis'
part_number = 1

urls = [seed_url]
seen = [seed_url]
opened = []
url_found_1=[]

n = 0
maxNum = 10
print("Starting with url=" + str(urls))

while len(urls) > 0 and n < maxNum:
    try:
        curr_url = urls.pop(0)
        req = urllib.request.Request(curr_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)
    except Exception as ex:
        print("Unable to access= " + curr_url)
        print(ex)
        continue

    soup = BeautifulSoup(webpage, "html.parser")
            
    if keyword.lower() in soup.get_text().lower() and soup.find('a', href='/en/press-release', string='Press Release') and soup.find('h1', class_='page-header'):
        print(f"Found the keyword '{keyword}' in: {curr_url}")
        url_found_1.append(curr_url)
        n = n + 1
        webpage_text = webpage.decode('utf-8')
        filename = f"{part_number}_{n}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(webpage_text)

    for tag in soup.find_all('a', href=True):
        childUrl = tag['href']
        fullUrl = urllib.parse.urljoin(seed_url, childUrl)
        if "//press.un.org/en" in fullUrl and seed_url in fullUrl and fullUrl not in seen:
            urls.append(fullUrl)
            seen.append(fullUrl)


# In[2]:


from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

keyword = 'crisis'
part_number = 2
page = 0
n = 0
maxNum = 10
url_found_2=[]

while n < maxNum:
    seed_url = f'https://www.europarl.europa.eu/news/en/press-room/page/{page}'
    urls = [seed_url]
    print("Starting with url=" + str(urls))
    seen = [seed_url]
    opened = []
    page = page + 1

    while len(urls) > 0 and n < maxNum:
        curr_url = urls.pop(0)
        try:
            req = urllib.request.Request(curr_url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urllib.request.urlopen(req).read()
            opened.append(curr_url)
        except Exception as ex:
            print("Unable to access= " + curr_url)
            print(ex)
            continue

        soup = BeautifulSoup(webpage, "html.parser")

        if keyword.lower() in soup.get_text().lower() and soup.find('span', class_='ep_name', string='Plenary session') and soup.find('h1', class_='ep_title'):
            print(f"Found the keyword '{keyword}' in: {curr_url}")
            url_found_2.append(curr_url)
            n = n + 1
            webpage_text = webpage.decode('utf-8')
            filename = f"{part_number}_{n}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(webpage_text)

        for tag in soup.find_all('a', href=True):
            childUrl = tag['href']
            fullUrl = urllib.parse.urljoin(seed_url, childUrl)
            if "/news/en/press-room/" in fullUrl and fullUrl not in seen and fullUrl not in urls:
                urls.append(fullUrl)
                seen.append(fullUrl)


# In[ ]:




