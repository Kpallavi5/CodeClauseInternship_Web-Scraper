import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
print(htmlContent)		# printing the code

# Step 2 : Parse the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())	# to print html in tree structure

# Step 3: HTML Tree Traversal
# Commonly used Types of object
#print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup) # 3. BeautifulSoup
# 4.comment
markup = "<p><!--this is comment--></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
exit()

#Get the title of the HTML page
title = soup.title

#Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)


# print(anchors)


#Get first element in the HTML page
print(soup.find('p'))

#Get the classes of any element in the HTML page
print(soup.find('p') ['class'])

#find all the elements withclass lead
print(soup.find_all("p",class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
# print(soup.get_text())

#Get all the anchor tag  from the page
anchors = soup.find_all('a')

all_links = set()
#Get all the links on the page:
for link in anchors:
    if(link != '#'):
        # all_links.add(link.get('href'))
        link = "https://timesofindia.indiatimes.com/city/delhi" +link.get('href')
        all_links.add(link)
        print(link)







