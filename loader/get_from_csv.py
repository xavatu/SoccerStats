import glob
import pathlib
from copy import deepcopy
from collections import defaultdict


_DEFAULT_STATISTIC = {
    "tackles": {
        "success_tackleWonTotal": 0,
        "success_tackleTotalAttempted": 0,
    },
    "interception": {"success_interceptionAll": 0},
    "fouls": {"type_foulGiven": 0, "type_foulsCommitted": 0},
    "cards": {"type_yellowCard": 0, "type_redCard": 0},
    "offsides": {"type_offsideGiven": 0},
    "clearances": {"success_clearanceTotal": 0},
    "blocks": {
        "type_passCrossBlockedDefensive": 0,
        "type_outfielderBlockedPass": 0,
        "type_outfielderBlock": 0,
    },
    "saves": {
        "shotzone_saveSixYardBox": 0,
        "shotzone_savePenaltyArea": 0,
        "shotzone_saveObox": 0,
        "shotzone_saveTotal": 0,
    },
    "shots": {
        "zones_shotSixYardBox": 0,
        "zones_shotPenaltyArea": 0,
        "zones_shotOboxTotal": 0,
        "zones_shotsTotal": 0,
        "situations_shotOpenPlay": 0,
        "situations_shotCounter": 0,
        "situations_shotSetPiece": 0,
        "situations_penaltyTaken": 0,
        "situations_shotsTotal": 0,
        "accuracy_shotOnTarget": 0,
        "accuracy_shotOffTarget": 0,
        "accuracy_shotOnPost": 0,
        "accuracy_shotBlocked": 0,
        "accuracy_shotsTotal": 0,
        "bodyparts_shotRightFoot": 0,
        "bodyparts_shotLeftFoot": 0,
        "bodyparts_shotHead": 0,
        "bodyparts_shotObp": 0,
        "bodyparts_shotsTotal": 0,
    },
    "goals": {
        "zones_goalSixYardBox": 0,
        "zones_goalPenaltyArea": 0,
        "zones_goalObox": 0,
        "zones_goalTotal": 0,
        "situations_goalOpenPlay": 0,
        "situations_goalCounter": 0,
        "situations_goalSetPiece": 0,
        "situations_penaltyScored": 0,
        "situations_goalNormal": 0,
        "situations_goalTotal": 0,
        "situations_goalOwn": 0,
        "bodyparts_goalTotal": 0,
        "bodyparts_goalRightFoot": 0,
        "bodyparts_goalLeftFoot": 0,
        "bodyparts_goalHead": 0,
        "bodyparts_goalObp": 0,
    },
    "dribbles": {
        "success_dribbleLost": 0,
        "success_dribbleWon": 0,
        "success_dribbleTotal": 0,
    },
    "possession-loss": {
        "type_turnover": 0,
        "type_dispossessed": 0,
    },
    "aerial": {
        "success_duelAerialLost": 0,
        "success_duelAerialTotal": 0,
        "success_duelAerialWon": 0,
    },
    "passes": {
        "length_passTotal": 0,
        "length_passLongBallAccurate": 0,
        "length_passLongBallInaccurate": 0,
        "length_shortPassAccurate": 0,
        "length_shortPassInaccurate": 0,
        "type_passCornerAccurate": 0,
        "type_passCornerInaccurate": 0,
        "type_passFreekickAccurate": 0,
        "type_passFreekickInaccurate": 0,
        "type_passCrossInaccurate": 0,
        "type_passCrossAccurate": 0,
    },
    "key-passses": {
        "length_keyPassLong": 0,
        "length_keyPassShort": 0,
        "length_keyPassesTotal": 0,
        "type_keyPassCross": 0,
        "type_keyPassCorner": 0,
        "type_keyPassThroughball": 0,
        "type_keyPassFreekick": 0,
        "type_keyPassThrowin": 0,
        "type_keyPassOther": 0,
    },
    "assists": {
        "type_assistCross": 0,
        "type_assistCorner": 0,
        "type_assistThroughball": 0,
        "type_assistFreekick": 0,
        "type_assistThrowin": 0,
        "type_assistOther": 0,
        "type_assist": 0,
    },
}
_DEFAULT_SEASON_INFO = {
    "seasonId": 0,
    "seasonName": "",
    "apps": 0,
    "minsPlayed": 0,
    "rating": 0,
    "ranking": 0,
    "playedPositions": "",
    "regionCode": "",
    "tournamentId": 0,
    "tournamentRegionId": "",
    "tournamentRegionCode": "",
    "tournamentRegionName": "",
    "tournamentName": "",
    "tournamentShortName": "",
    "teamId": 0,
    "teamRegionName": "",
    "teamName": "",
    "statistic": _DEFAULT_STATISTIC,
}
_DEFAULT_PLAYER_INFO = {
    "playerId": 0,
    "name": "",
    "firstName": "",
    "lastName": "",
    "age": 0,
    "height": 0,
    "weight": 0,
}
_DEFAULT_PLAYER_STATISTIC = {
    **_DEFAULT_PLAYER_INFO,
    "seasons": [],
}
get_default_statistic = lambda: deepcopy(_DEFAULT_STATISTIC)
get_default_season_info = lambda: deepcopy(_DEFAULT_SEASON_INFO)
get_default_player_info = lambda: deepcopy(_DEFAULT_PLAYER_INFO)
get_default_player_statistic = lambda: deepcopy(_DEFAULT_PLAYER_STATISTIC)


if __name__ == "__main__":
    path = pathlib.Path().resolve().parent
    player_statistics = defaultdict(get_default_player_statistic)

    for filename in glob.glob1(f"{path}/test/", "*.csv"):
        name = filename.replace(".csv", "")
        print(f"{name} = pd.read_csv('./test/{name}.csv')")
        print(f"{name}_total = {name}.groupby(['playerId']).agg(")
        print({"apps": "sum", "minsPlayed": "sum", **{k: "sum" for k in _DEFAULT_STATISTIC[name]}})
        print(")")
        print(f"{name}_avg = {name}.groupby(['playerId']).agg(")
        print({"apps": "sum", "minsPlayed": "sum", **{k: "mean" for k in _DEFAULT_STATISTIC[name]}})
        print(")")

    #     with open(f"{path}/test/{filename}", "r", encoding="utf-8") as f:
    #         reader = DictReader(f)
    #         for row in reader:
    #             stat = player_statistics[row["playerId"]]
    #             stat.update(
    #                 {
    #                     k: v
    #                     for k, v in row.items()
    #                     if k in _DEFAULT_PLAYER_INFO.keys()
    #                 }
    #             )
    #             season_info = get_default_season_info()
    #             season_info.update(
    #                 {
    #                     k: v
    #                     for k, v in row.items()
    #                     if k in _DEFAULT_SEASON_INFO.keys()
    #                 }
    #             )
    #             statname = filename.replace(".csv", "")
    #             season_info["statistic"][statname].update(
    #                 {
    #                     k: v
    #                     for k, v in row.items()
    #                     if k in _DEFAULT_STATISTIC[statname].keys()
    #                 }
    #             )
    #             stat["seasons"].append(season_info)
    # print(player_statistics)
