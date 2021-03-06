import string
import scraperwiki
import mechanize

from BeautifulSoup import BeautifulSoup

# The job of this scraper is to go away and find the prices of all the components for the SHED 
# garden office from those suppliers I know supply them

starting_url = 'http://www.buildingmaterials.co.uk/kingspan-insulation-boards-tp10-2400mm-x-1200mm.html' 
#start using mechanize to simulate a browser ('br')
br = mechanize.Browser()
br.set_debug_responses(True)
# Set the user-agent as Mozilla - if the page knows we're Mechanize, it won't return all fields
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#open the URL previously defined as 'starting_url'
br.open(starting_url)
soup = BeautifulSoup(br.response().read())
table_div = soup.find("div",{"id" : "property_table_109"})
if table_div:
	ks_table = table_div.find("table")
	if ks_table:
		rows = ks_table.findAll("tr")
		for row in rows:
			record={}
			table_cells = row.findAll("td")
			if table_cells:
				record['id'] = table_cells[1].string
				record['name'] = table_cells[0].string
				record['price'] = table_cells[2].find("span").string
				print record
