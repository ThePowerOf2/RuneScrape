# Imports
import bs4 as bs
import urllib.request

# Group level limits + number of pages to scrape + what skill to scrape.
group1Limit = 50
group2Limit = 80
noPages = 7
skill = 10 # This can be found in the URL of the skills hiscores page.

# Declaring an array for each group.
group1=[]
group2=[]
group3=[]

# Creating/Overwriting .txt file to save names into.
namesFile = open("GroupNames.txt","w")

# For loop from 1 to amount of (pages+1).
for memes in range(1,noPages+1):
	# Fetching and scraping out table row information that is needed.
	URL = "http://www.runeclan.com/clan/reclusion/hiscores/%s?skill=%s" % (memes,skill)
	sauce = urllib.request.urlopen(URL).read()
	soup = bs.BeautifulSoup(sauce, 'lxml')
	div = soup.find('td',class_='clan_right')
	table = div.find('table',class_='regular')
	table_rows = table.find_all('tr')

	# x is used to skip over table rows.
	x = 1

	# Place names into there relevant groups from each row on the current page we're scraping.
	for tr in table_rows:
		if x%2 == 0:
			td = tr.find_all('td')
			row = [i.text for i in td]
			if int(row[2]) <= group1Limit:
				group1.append(row[1])
			elif int(row[2]) <= group2Limit:
				group2.append(row[1])
			else:
				group3.append(row[1])
		x=x+1
	# Print out when a page has been completed.
	print('Page %d Complete.' % (memes))

# Sorting and placing all the name into the .txt file for each group.
namesFile.write("-------- GROUP 1 (1-50) -------\n" )
for name in sorted(group1):
	namesFile.write(name)
	namesFile.write("\n")

namesFile.write("\n-------- GROUP 2 (51-80) -------\n" )
for name in sorted(group2):
	namesFile.write(name)
	namesFile.write("\n")

namesFile.write("\n-------- GROUP 3 (81+) -------\n" )
for name in sorted(group3):
	namesFile.write(name)
	namesFile.write("\n")

# Memes
print('Finished!')