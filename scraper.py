# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
# kingspan
html = scraperwiki.scrape("http://www.buildingmaterials.co.uk/kingspan-insulation-boards-tp10-2400mm-x-1200mm.html")
class Product:
    def __init__(self, name, qty, url, ID, price):
        self.name = name
        self.qty = qty
        self.url = url
        self.ID = ID
        self.price = price
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
for el in root.cssselect("tr#option_item_439"):
    kingspan50 = Product("Kingspan50",1,"buildingmaterials.co.uk",el.cssselect("td")[2].text,el.cssselect("td")[3].text)
    print kingspan50

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
