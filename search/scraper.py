import requests
from bs4 import BeautifulSoup
from search.models import Professor

def scrape_professors():
    url = "https://www.cse.iitk.ac.in/pages/Faculty.html"  # Example dept
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for prof in soup.find_all("div", class_="faculty-profile"):
        name = prof.find("h3").text.strip()
        webpage = prof.find("a")["href"]
        domain = prof.find("p", class_="research-interest").text.strip()

        Professor.objects.create(name=name, webpage=webpage, domain=domain)

# Run this inside Django shell
# python manage.py shell
# >>> from search.scraper import scrape_professors
# >>> scrape_professors()
