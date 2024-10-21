from copy import deepcopy

url = "https://www.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?"
_DEFAULT_PARAMS = {
    "category": "",
    "subcategory": "",
    "statsAccumulationType": "",
    "isCurrent": "",
    "playerId": "",
    "teamIds": "",
    "matchId": "",
    "stageId": "",
    "sortBy": "",
    "sortAscending": "",
    "age": "",
    "ageComparisonType": "",
    "appearances": "",
    "appearancesComparisonType": "",
    "field": "",
    "nationality": "",
    "positionOptions": "",
    "timeOfTheGameEnd": "",
    "timeOfTheGameStart": "",
    "isMinApp": "",
    "page": "",
    "includeZeroValues": "",
    "numberOfPlayersToPick": "",
    "incPens": "",
}
get_default_params = lambda: deepcopy(_DEFAULT_PARAMS)
generate_params_url = lambda p: "".join(f"&{k}={v}" for k, v in p.items())[1:]
