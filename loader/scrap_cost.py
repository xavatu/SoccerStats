import json
from collections import defaultdict
from concurrent import futures

from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm

from loader.players import get_players

players = get_players()


def scrap_cost(from_to: tuple[int, int]):
    result = defaultdict(int)
    from_, to_ = from_to
    driver = webdriver.Chrome()
    url = "https://www.transfermarkt.world/schnellsuche/ergebnis/schnellsuche?query="
    for player in tqdm(players[from_:to_], delay=0):
        firstName = player.get("firstName", None)
        lastName = player.get("lastName", None)
        firstName = firstName if firstName else " "
        lastName = lastName if lastName else " "
        name = firstName + " " + lastName
        get_url = url + "+".join((firstName, lastName))
        # print(get_url)
        driver.get(get_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        odds = soup.find_all("tr", class_="odd")
        found = False
        for odd in odds:
            params = odd.find_all("td", class_="zentriert")
            if len(params) < 3:
                continue
            age = params[2].contents
            cost = odd.find_all("td", class_="rechts hauptlink")
            if len(age) == 0:
                continue
            try:
                age = int(age[0])
            except Exception:
                continue
            if age == player["age"]:
                found = True
                break
        if not found:
            continue
        cost = cost[0].text
        result[player["playerId"]] = cost
        with open("./data/player_costs2.json", "a", encoding="utf-8") as f:
            f.write(f"{get_url}, {player["playerId"]}, {cost}\n")


if __name__ == "__main__":
    with futures.ThreadPoolExecutor() as executor:  # default/optimized number of threads
        list(executor.map(scrap_cost, ((el, el + 1000) for el in range(0, 12000, 1000))))
