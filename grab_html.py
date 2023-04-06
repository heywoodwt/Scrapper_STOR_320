import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = "https://247sports.com/Season/2019-Basketball/CompositeTeamRankings/"
response = requests.get(url)

# Check if the response was successful
if response.status_code != 200:
    raise ValueError("Failed to load page")

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table element with the team rankings
table = soup.find("table", {"class": "rankings-table"})

# Check if the table was found
if table is None:
    raise ValueError("Failed to find table")

# Create a CSV file to write the data to
with open("team_rankings.csv", mode="w") as file:
    writer = csv.writer(file)

    # Write the headers of the table as the first row in the CSV file
    headers = [header.text.strip() for header in table.find_all("th")]
    writer.writerow(headers)

    # Write the data of each row in the table to the CSV file
    for row in table.find_all("tr")[1:]:
        data = [cell.text.strip() for cell in row.find_all("td")]
        writer.writerow(data)
