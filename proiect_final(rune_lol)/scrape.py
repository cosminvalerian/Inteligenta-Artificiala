from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import urllib.request
from PIL import Image

#nautilus - 0
#udyr - 1 (p: precision)
#tristana - 2 (p: domination)
#reksai - 2 (p: precision & s: domination)

champion = 'tristana'
url = 'https://u.gg/lol/champions/' + champion + '/build'

req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")

opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')

perks = page_soup.find_all('div',{"class":"perk-style-title"})
primaryPerk = perks[0].get_text()
secondaryPerk = perks[1].get_text()
print(primaryPerk, secondaryPerk)
allShardURLs = []
shardDivs = page_soup.find_all('div',{"class":"shard"})
for shardDiv in shardDivs:
    allShardURLs.append(shardDiv.find('img')['src'])

shardsOrder = []
shards = page_soup.find_all('div',{"class":"shard"})
shards = shards[:9]

for shard in shards:
    if 'shard-active' in str(shard):
        shardsOrder.append(1)
    else:
        shardsOrder.append(0)

activeImageURLs = []
divs = page_soup.find_all('div',{"class":"perk-active"})
for div in divs:
    activeImageURLs.append(div.find('img')['src'])

allImageURLs = []
alldivs = page_soup.find_all('div',{"class":"perk"})
for div in alldivs:
    allImageURLs.append(div.find('img')['src'])

extraNeededSpaces = 0
if primaryPerk == 'Precision' and secondaryPerk != 'Domination':
    extraNeededSpaces = 1
if (primaryPerk == 'Precision' and secondaryPerk == 'Domination') or primaryPerk == 'Domination':
    extraNeededSpaces = 2
if primaryPerk != 'Precision' and secondaryPerk == 'Domination':
    extraNeededSpaces = 1

allImageURLs = allImageURLs[:21 + extraNeededSpaces]
allImageURLs.extend(allShardURLs)
allImageURLs = allImageURLs[:30 + extraNeededSpaces]

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGBA', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

imgs = []
names = []
counter = 0
blackSquarePNG = 'transparent_block.png'

if primaryPerk == 'Precision' and secondaryPerk != 'Domination':
    allImageURLs.insert(7,blackSquarePNG)
    allImageURLs.insert(11,blackSquarePNG)
    allImageURLs.insert(15,blackSquarePNG)
    allImageURLs.insert(19,blackSquarePNG)
    allImageURLs.insert(23,blackSquarePNG)
    allImageURLs.insert(27,blackSquarePNG)
    allImageURLs.insert(31,blackSquarePNG)
    allImageURLs.insert(35,blackSquarePNG)
    allImageURLs.insert(39,blackSquarePNG)

if primaryPerk == 'Domination':
    allImageURLs.insert(7,blackSquarePNG)
    allImageURLs.insert(11,blackSquarePNG)
    allImageURLs.insert(19,blackSquarePNG)
    allImageURLs.insert(23,blackSquarePNG)
    allImageURLs.insert(27,blackSquarePNG)
    allImageURLs.insert(31,blackSquarePNG)
    allImageURLs.insert(35,blackSquarePNG)
    allImageURLs.insert(39,blackSquarePNG)

if primaryPerk == 'Precision' and secondaryPerk == 'Domination':
    allImageURLs.insert(7,blackSquarePNG)
    allImageURLs.insert(11,blackSquarePNG)
    allImageURLs.insert(15,blackSquarePNG)
    allImageURLs.insert(19,blackSquarePNG)
    allImageURLs.insert(23,blackSquarePNG)
    allImageURLs.insert(31,blackSquarePNG)
    allImageURLs.insert(35,blackSquarePNG)
    allImageURLs.insert(39,blackSquarePNG)


if primaryPerk != 'Precision' and secondaryPerk == 'Domination':
    allImageURLs.insert(3,blackSquarePNG)
    allImageURLs.insert(7,blackSquarePNG)
    allImageURLs.insert(11,blackSquarePNG)
    allImageURLs.insert(15,blackSquarePNG)
    allImageURLs.insert(19,blackSquarePNG)
    allImageURLs.insert(23,blackSquarePNG)
    allImageURLs.insert(31,blackSquarePNG)
    allImageURLs.insert(35,blackSquarePNG)
    allImageURLs.insert(39,blackSquarePNG)

for activeImageURL in allImageURLs:
    imgs.append(opener.retrieve(activeImageURL, "scrapes/" + str(counter) + ".png"))
    names.append("scrapes/" + str(counter) + ".png")
    counter += 1

images = [Image.open(x).convert('RGBA') for x in names]

counter = 0
runesStop = 21
shardsStop = 30

if extraNeededSpaces > 0:
    runesStop = 28
    shardsStop = 40

for finalimg in allImageURLs:
    if finalimg not in activeImageURLs:
        images[counter] = images[counter].convert('LA')
    counter += 1
    if counter == runesStop:
        break
orderCounter = 0
for shard in allImageURLs:
    if counter == shardsStop:
        break
    if shardsOrder[orderCounter] == 0:
        images[counter] = images[counter].convert('LA')
    counter +=1
    if (counter != 31) and (counter != 35) and (counter != 39):
        orderCounter += 1

cols = 3
if extraNeededSpaces > 0:
    cols = 4
grid = image_grid(images, rows = 10, cols = cols)
grid.save('img.png')