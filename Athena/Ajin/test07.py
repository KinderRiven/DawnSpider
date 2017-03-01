from bs4 import BeautifulSoup

fr = open("setting.txt", "r")
content = fr.read()
fr.close()


soup = BeautifulSoup(content, "html.parser")
data = soup.find("data")
data.string = ""

#print soup

for i in range(1, 5):
    item = BeautifulSoup("<item><url></url><title></title></item>\n", "html.parser")
    item.find("url").string = str(i)
    item.find("title").string = "233"
    soup.data.append(item)
#print soup

fw = open("setting.txt", "wb")
fw.write(str(soup))
fw.close()