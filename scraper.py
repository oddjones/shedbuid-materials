import string
import scraperwiki
import mechanize

from BeautifulSoup import BeautifulSoup


starting_url = 'http://www.buildingmaterials.co.uk/kingspan-insulation-boards-tp10-2400mm-x-1200mm.html' 


br = mechanize.Browser()
br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open(starting_url)
soup = BeautifulSoup(br.read())
