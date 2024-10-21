import json
import os
from collections import defaultdict
from concurrent import futures
from copy import deepcopy
from csv import DictWriter
from tqdm import tqdm

from selenium import webdriver

from config import url, get_default_params, generate_params_url
from players import players

_DEFAULT_STATS = {
    "tackles": {
        "success": {
            "tackleWonTotal": 0,
            "tackleTotalAttempted": 0,
        }
    },
    "interception": {"success": {"interceptionAll": 0}},
    "fouls": {
        "type": {
            "foulGiven": 0,
            "foulsCommitted": 0,
        }
    },
    "cards": {
        "type": {
            "yellowCard": 0,
            "redCard": 0,
        }
    },
    "offsides": {
        "type": {
            "offsideGiven": 0,
        }
    },
    "clearances": {
        "success": {
            "clearanceTotal": 0,
        }
    },
    "blocks": {
        "type": {
            "passCrossBlockedDefensive": 0,
            "outfielderBlockedPass": 0,
            "outfielderBlock": 0,
        }
    },
    "saves": {
        "shotzone": {
            "saveSixYardBox": 0,
            "savePenaltyArea": 0,
            "saveObox": 0,
            "saveTotal": 0,
        }
    },
    "shots": {
        "zones": {
            "shotSixYardBox": 0,
            "shotPenaltyArea": 0,
            "shotOboxTotal": 0,
            "shotsTotal": 0,
        },
        "situations": {
            "shotOpenPlay": 0,
            "shotCounter": 0,
            "shotSetPiece": 0,
            "penaltyTaken": 0,
            "shotsTotal": 0,
        },
        "accuracy": {
            "shotOnTarget": 0,
            "shotOffTarget": 0,
            "shotOnPost": 0,
            "shotBlocked": 0,
            "shotsTotal": 0,
        },
        "bodyparts": {
            "shotRightFoot": 0,
            "shotLeftFoot": 0,
            "shotHead": 0,
            "shotObp": 0,
            "shotsTotal": 0,
        },
    },
    "goals": {
        "zones": {
            "goalSixYardBox": 0,
            "goalPenaltyArea": 0,
            "goalObox": 0,
            "goalTotal": 0,
        },
        "situations": {
            "goalOpenPlay": 0,
            "goalCounter": 0,
            "goalSetPiece": 0,
            "penaltyScored": 0,
            "goalNormal": 0,
            "goalTotal": 0,
            "goalOwn": 0,
        },
        "bodyparts": {
            "goalTotal": 0,
            "goalRightFoot": 0,
            "goalLeftFoot": 0,
            "goalHead": 0,
            "goalObp": 0,
        },
    },
    "dribbles": {
        "success": {
            "dribbleLost": 0,
            "dribbleWon": 0,
            "dribbleTotal": 0,
        }
    },
    "possession-loss": {
        "type": {
            "turnover": 0,
            "dispossessed": 0,
        }
    },
    "aerial": {
        "success": {
            "duelAerialLost": 0,
            "duelAerialTotal": 0,
            "duelAerialWon": 0,
        }
    },
    "passes": {
        "length": {
            "passTotal": 0,
            "passLongBallAccurate": 0,
            "passLongBallInaccurate": 0,
            "shortPassAccurate": 0,
            "shortPassInaccurate": 0,
        },
        "type": {
            "passCornerAccurate": 0,
            "passCornerInaccurate": 0,
            "passFreekickAccurate": 0,
            "passFreekickInaccurate": 0,
            "passCrossInaccurate": 0,
            "passCrossAccurate": 0,
        },
    },
    "key-passes": {
        "length": {
            "keyPassLong": 0,
            "keyPassShort": 0,
            "keyPassesTotal": 0,
        },
        "type": {
            "keyPassCross": 0,
            "keyPassCorner": 0,
            "keyPassThroughball": 0,
            "keyPassFreekick": 0,
            "keyPassThrowin": 0,
            "keyPassOther": 0,
        },
    },
    "assists": {
        "type": {
            "assistCross": 0,
            "assistCorner": 0,
            "assistThroughball": 0,
            "assistFreekick": 0,
            "assistThrowin": 0,
            "assistOther": 0,
            "assist": 0,
        }
    },
}
_COMMONS = [
    "height",
    "weight",
    "age",
    "isManOfTheMatch",
    "isActive",
    "playedPositions",
    "playedPositionsShort",
    "teamRegionName",
    "regionCode",
    "tournamentShortName",
    "apps",
    "subOn",
    "name",
    "firstName",
    "lastName",
    "playerId",
    "positionText",
    "teamId",
    "teamName",
    "seasonId",
    "seasonName",
    "isOpta",
    "tournamentId",
    "tournamentRegionId",
    "tournamentRegionCode",
    "tournamentRegionName",
    "tournamentName",
    "rating",
    "minsPlayed",
    "ranking",
]
get_default_stats_dict = lambda: deepcopy(_DEFAULT_STATS)


def get_player_stats_params() -> dict[str, str]:
    params = get_default_params()
    params.update(
        **{
            "statsAccumulationType": "2",
            "isCurrent": "false",
            "sortBy": "seasonId",
            "appearancesComparisonType": "0",
            "ageComparisonType": "0",
            "page": "1",
            "includeZeroValues": "true",
        }
    )
    return params


def get_player_stats() -> dict:
    try:
        with open("./data/stats.json", "r") as f:
            stats_ = json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        with open("./data/stats.json", "a") as f:
            stats_ = {}
            print(str(stats_), file=f)
    return stats_


player_stats = get_player_stats()


def get_stats(from_to: tuple[int, int]):
    from_, to_ = from_to
    driver = webdriver.Chrome()
    player_stats_params = get_player_stats_params()
    player_stats = {}
    for player in tqdm(players[from_:to_], delay = 10):
        playerId = player["playerId"]
        player_stats[playerId] = defaultdict(dict)
        for category, subcategory_dict in _DEFAULT_STATS.items():
            for subcategory in subcategory_dict.keys():
                player_stats_params.update(
                    playerId=playerId,
                    category=category,
                    subcategory=subcategory,
                )
                param_url = generate_params_url(player_stats_params)
                driver.get(url + param_url)
                page_source = driver.page_source.replace(
                    "<html><head></head><body>", ""
                ).replace(" </body></html>", "")
                try:
                    data = json.loads(page_source)
                except Exception as e:
                    print(e)
                    continue
                for i, data in enumerate(data["playerTableStats"]):
                    for k, v in data.items():
                        if k in _DEFAULT_STATS[category][subcategory]:
                            player_stats[playerId][i].update(
                                {f"{category}_{subcategory}_{k}": v}
                            )
                            continue
                        player_stats[playerId][i].update({k: v})
            category_fields = _COMMONS + [
                f"{category}_{sub_name}_{k}"
                for sub_name, sub in _DEFAULT_STATS[category].items()
                for k in sub
            ]
            # print(category_fields)
            write_header = True
            if os.path.isfile(f"./test/{category}.csv"):
                write_header = False
            with open(f"./test/{category}.csv", "a",
                      encoding="utf-8") as f:
                writer = DictWriter(f, category_fields, lineterminator="\n")
                if write_header:
                    writer.writeheader()
                writer.writerows(
                    [
                        {k: v for k, v in el.items() if k in category_fields}
                        for el in player_stats[playerId].values()
                    ]
                )


if __name__ == "__main__":
    with futures.ThreadPoolExecutor() as executor:  # default/optimized number of threads
        list(executor.map(get_stats, ((el, el+100) for el in range(0, 1100, 100))))
