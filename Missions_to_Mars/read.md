In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.
I completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Scraped the Mars News Site and collected the latest News Title and Paragraph Text. 
Visited the url for the Featured Space Image site and used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable.
Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.Use Pandas to convert the data to a HTML table string.
Visited the astrogeology site to obtain high resolution images for each of Mar's hemispheres.
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
