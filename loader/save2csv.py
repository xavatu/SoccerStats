from collections import defaultdict
from csv import DictWriter, DictReader

from stats import player_stats, get_default_stats_dict


def _get_values_dict():
    values_dict = {}
    for filename, _ in get_default_stats_dict().items():
        values = defaultdict(list)
        for type_, data in _.items():
            for column_name, column_value in data.items():
                column_name = f"{type_}_{column_name}"
                values[column_name]  # noqa
        values_dict.update(**{filename: values})
    return values_dict


def _init_statistics_csv():
    values = _get_values_dict()
    for filename, _ in get_default_stats_dict().items():
        with open(f"../statistics/{filename}.csv", "w") as f:
            writer = DictWriter(f, ["playerId", *values.keys()])
            writer.writeheader()


def _fill_statistics():
    values = _get_values_dict()
    print(values)
    return
    costs = _get_costs()
    _player_ids = set()
    for filename, _ in get_default_stats_dict().items():
        with open(f"./test/{filename}.csv", "w", encoding="utf-8") as f:
            fieldnames = list(values[filename].keys())
            fieldnames.append("playerCost")
            for playerId, player_data in player_stats.items():
                all_fields = []
                for type_, data in player_data[filename].items():
                    data = data["playerTableStats"]
                    if not data:
                        break
                    data = data[0]
                    all_fields = data.keys()
                    for field in all_fields:
                        if f"{type_}_{field}" not in fieldnames:
                            fieldnames.append(field)
                    break
                if all_fields:
                    break
            writer = DictWriter(f, fieldnames, lineterminator="\n")
            writer.writeheader()
            for playerId, player_data in player_stats.items():
                periods = 0
                for type_, data in player_data[filename].items():
                    data = data["playerTableStats"]
                    if not data:
                        break
                    periods = len(data)
                    break
                periods_data = [
                    {k: None for k in fieldnames} for _ in range(periods)
                ]
                for type_, data in player_data[filename].items():
                    data = data["playerTableStats"]
                    if not data:
                        break
                    _player_ids.add(playerId)
                    data = [
                        {
                            (k if k in fieldnames else f"{type_}_{k}"): v
                            for k, v in row.items()
                        }
                        for row in data
                    ]
                    for i, el in enumerate(data):
                        periods_data[i].update(**el)
                        periods_data[i].update(
                            playerCost=costs[int(playerId)].get(
                                "playerCost", None
                            )
                        )
                    # print(filename, data[0].keys())
                writer.writerows(periods_data)
    print(len(_player_ids))


def _get_costs():
    results = defaultdict(dict)
    player_ids = set()
    with open("./data/player_costs2.json", "r", encoding="utf-8") as f:
        reader = DictReader(
            f, fieldnames=("url", "playerId", "cost1", "cost2")
        )
        i = 0
        for row in reader:
            i += 1
            cost1 = row["cost1"]
            cost2 = row["cost2"]
            player_id = int(row["playerId"].replace(" ", ""))
            player_ids.add(player_id)
            if not cost2:
                playerCost = cost1
            else:
                playerCost = cost1 + "." + cost2
            if "млн €" in playerCost:
                playerCost = playerCost.replace("млн €", "").replace(" ", "")
                playerCost = int(float(playerCost) * 1000000)
            elif "тыс €" in playerCost:
                playerCost = playerCost.replace("тыс €", "").replace(" ", "")
                playerCost = int(float(playerCost) * 1000)
            else:
                playerCost = None
            result = {
                "url": row["url"],
                "playerId": player_id,
                "playerCost": playerCost,
            }
            results[player_id] = result
    # print(results)
    return results


if __name__ == "__main__":
    # _init_statistics_csv()
    # _fill_statistics()
    player_costs = _get_costs()
    with open(f"./data/costs.csv", "w", encoding="utf-8") as f:
        writer = DictWriter(
            f, ["url", "playerId", "playerCost"], lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows([player_costs[el] for el in player_costs])
