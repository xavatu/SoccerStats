import json
import time
from random import randint

from selenium import webdriver

from config import get_default_params, generate_params_url, url
from teams import teams


def get_team_squad_params() -> dict[str, str]:
    params = get_default_params()
    params.update(
        **{
            "category": "summary",
            "subcategory": "all",
            "statsAccumulationType": "0",
            "isCurrent": "true",
            "sortBy": "Rating",
            "field": "Overall",
            "isMinApp": "false",
            "page": "1",
            "includeZeroValues": "true",
        }
    )
    return params


def get_players() -> list:
    try:
        with open("./data/players.json", "r") as f:
            players_ = json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        with open("./data/players.json", "w") as f:
            players_ = []
            print(str(players_), file=f)
    return players_


players = get_players()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    print(driver.__dict__)
    team_squad_params = get_team_squad_params()
    players = []

    for team_dict in teams:
        teamIds = team_dict["teamIds"]
        team_squad_params.update(teamIds=teamIds)
        param_url = generate_params_url(team_squad_params)
        driver.get(url + param_url)
        page_source = driver.page_source.replace(
            "<html><head></head><body>", ""
        ).replace(" </body></html>", "")
        squad = json.loads(page_source)
        print(squad)
        players.extend(squad["playerTableStats"])
        time.sleep(randint(10, 30) / 1000)

    with open("./data/players2.json", "w", encoding="utf-8") as f:
        print(json.dumps(players, indent=4), file=f)
