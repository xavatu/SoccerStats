import json

from bs4 import BeautifulSoup


def get_teams() -> list:
    try:
        with open("./data/teams2.json", "r") as f:
            teams_ = json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        with open("./data/teams2.json", "w") as f:
            teams_ = []
            print(str(teams_), file=f)
    return teams_


teams = get_teams()

if __name__ == "__main__":

    def extract_team_data(html_file):
        with open(html_file, "r") as file:
            content = file.read()

        soup = BeautifulSoup(content, "html.parser")
        team_links = soup.find_all("a", class_="team-link")
        teams = []

        for team_link in team_links:
            team_name = " ".join(team_link.text.split())
            team_url = team_link["href"]
            team_id = team_url.split("/")[2]

            teams.append(
                {
                    "teamIds": team_id,
                    "teamLink": "https://www.whoscored.com/Teams/" + team_id,
                    "teamName": team_name,
                }
            )

        return teams

    def print_team_data(teams):
        for team in teams:
            print(f"{team['teamLink']:<50} {team['teamName']}")

    html_file = "./data/teams2.html"

    extracted = extract_team_data(html_file)
    print_team_data(extracted)
    teams = extracted

    with open("./data/teams2.json", "w") as f:
        print(json.dumps(teams, indent=4), file=f)
