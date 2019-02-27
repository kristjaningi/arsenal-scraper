import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import Response
from flask import json
from flask import jsonify

app = Flask(__name__)

# Get all players
@app.route("/players")
def get_players():
  page = requests.get('https://www.arsenal.com/first-team/players')
  soup = BeautifulSoup(page.text, 'html.parser')

  players = soup.find_all('div', class_='player-card__info')

  results = []

  for item in players:
    number = item.select('.player-card__info__number')[0].get_text()
    firstName = item.select('.player-card__info__position-or-first-name')[0].get_text()
    lastName = item.select('.player-card__info__name')[0].get_text()
    nation = item.select('.player-card__info__nationality__label')[0].get_text()

    player = {
      "number": number.strip(),
      "firstName": firstName,
      "lastName": lastName,
      "nation": nation  
    }

    results.append(player)

  
  resp = jsonify(results)

  return resp


# Get all staff members and roles
@app.route("/staff")
def get_staff():
  page = requests.get('https://www.arsenal.com/first-team/staff')
  soup = BeautifulSoup(page.text, 'html.parser')

  players = soup.find_all('div', class_='player-card__info')

  results = []

  for item in players:
    name = item.select('.player-card__info__name')[0].get_text()
    title = item.select('.player-card__info__nationality__label')[0].get_text()

    member = {
      "name": name,
      "title": title  
    }

    results.append(member)

  resp = jsonify(results)

  return resp



if __name__ == '__main__':
  app.run(debug=True)