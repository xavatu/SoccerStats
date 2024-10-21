import pandas as pd

aerial = pd.read_csv("./test/aerial.csv")
aerial_total = aerial.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_duelAerialLost": "sum",
        "success_duelAerialTotal": "sum",
        "success_duelAerialWon": "sum",
    }
)
aerial_avg = aerial.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_duelAerialLost": "mean",
        "success_duelAerialTotal": "mean",
        "success_duelAerialWon": "mean",
    }
)
assists = pd.read_csv("./test/assists.csv")
assists_total = assists.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_assistCross": "sum",
        "type_assistCorner": "sum",
        "type_assistThroughball": "sum",
        "type_assistFreekick": "sum",
        "type_assistThrowin": "sum",
        "type_assistOther": "sum",
        "type_assist": "sum",
    }
)
assists_avg = assists.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_assistCross": "mean",
        "type_assistCorner": "mean",
        "type_assistThroughball": "mean",
        "type_assistFreekick": "mean",
        "type_assistThrowin": "mean",
        "type_assistOther": "mean",
        "type_assist": "mean",
    }
)
blocks = pd.read_csv("./test/blocks.csv")
blocks_total = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_passCrossBlockedDefensive": "sum",
        "type_outfielderBlockedPass": "sum",
        "type_outfielderBlock": "sum",
    }
)
blocks_avg = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_passCrossBlockedDefensive": "mean",
        "type_outfielderBlockedPass": "mean",
        "type_outfielderBlock": "mean",
    }
)
cards = pd.read_csv("./test/cards.csv")
cards_total = cards.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_yellowCard": "sum",
        "type_redCard": "sum",
    }
)
cards_avg = cards.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_yellowCard": "mean",
        "type_redCard": "mean",
    }
)
clearances = pd.read_csv("./test/clearances.csv")
clearances_total = clearances.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "success_clearanceTotal": "sum"}
)
clearances_avg = clearances.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "success_clearanceTotal": "mean"}
)
dribbles = pd.read_csv("./test/dribbles.csv")
dribbles_total = dribbles.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_dribbleLost": "sum",
        "success_dribbleWon": "sum",
        "success_dribbleTotal": "sum",
    }
)
dribbles_avg = dribbles.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_dribbleLost": "mean",
        "success_dribbleWon": "mean",
        "success_dribbleTotal": "mean",
    }
)
fouls = pd.read_csv("./test/fouls.csv")
fouls_total = fouls.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_foulGiven": "sum",
        "type_foulsCommitted": "sum",
    }
)
fouls_avg = fouls.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_foulGiven": "mean",
        "type_foulsCommitted": "mean",
    }
)
goals = pd.read_csv("./test/goals.csv")
goals_total = goals.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "zones_goalSixYardBox": "sum",
        "zones_goalPenaltyArea": "sum",
        "zones_goalObox": "sum",
        "zones_goalTotal": "sum",
        "situations_goalOpenPlay": "sum",
        "situations_goalCounter": "sum",
        "situations_goalSetPiece": "sum",
        "situations_penaltyScored": "sum",
        "situations_goalNormal": "sum",
        "situations_goalTotal": "sum",
        "situations_goalOwn": "sum",
        "bodyparts_goalTotal": "sum",
        "bodyparts_goalRightFoot": "sum",
        "bodyparts_goalLeftFoot": "sum",
        "bodyparts_goalHead": "sum",
        "bodyparts_goalObp": "sum",
    }
)
goals_avg = goals.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "zones_goalSixYardBox": "mean",
        "zones_goalPenaltyArea": "mean",
        "zones_goalObox": "mean",
        "zones_goalTotal": "mean",
        "situations_goalOpenPlay": "mean",
        "situations_goalCounter": "mean",
        "situations_goalSetPiece": "mean",
        "situations_penaltyScored": "mean",
        "situations_goalNormal": "mean",
        "situations_goalTotal": "mean",
        "situations_goalOwn": "mean",
        "bodyparts_goalTotal": "mean",
        "bodyparts_goalRightFoot": "mean",
        "bodyparts_goalLeftFoot": "mean",
        "bodyparts_goalHead": "mean",
        "bodyparts_goalObp": "mean",
    }
)
interception = pd.read_csv("./test/interception.csv")
interception_total = interception.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "success_interceptionAll": "sum"}
)
interception_avg = interception.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "success_interceptionAll": "mean"}
)
# key_passses = pd.read_csv("./test/key-passses.csv")
# key_passses_total = key_passses.groupby(["playerId"]).agg(
#     {
#         "apps": "sum",
#         "minsPlayed": "sum",
#         "length_keyPassLong": "sum",
#         "length_keyPassShort": "sum",
#         "length_keyPassesTotal": "sum",
#         "type_keyPassCross": "sum",
#         "type_keyPassCorner": "sum",
#         "type_keyPassThroughball": "sum",
#         "type_keyPassFreekick": "sum",
#         "type_keyPassThrowin": "sum",
#         "type_keyPassOther": "sum",
#     }
# )
# key_passses_avg = key_passses.groupby(["playerId"]).agg(
#     {
#         "apps": "sum",
#         "minsPlayed": "sum",
#         "length_keyPassLong": "mean",
#         "length_keyPassShort": "mean",
#         "length_keyPassesTotal": "mean",
#         "type_keyPassCross": "mean",
#         "type_keyPassCorner": "mean",
#         "type_keyPassThroughball": "mean",
#         "type_keyPassFreekick": "mean",
#         "type_keyPassThrowin": "mean",
#         "type_keyPassOther": "mean",
#     }
# )
offsides = pd.read_csv("./test/offsides.csv")
offsides_total = offsides.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "type_offsideGiven": "sum"}
)
offsides_avg = offsides.groupby(["playerId"]).agg(
    {"apps": "sum", "minsPlayed": "sum", "type_offsideGiven": "mean"}
)
passes = pd.read_csv("./test/passes.csv")
passes_total = passes.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "length_passTotal": "sum",
        "length_passLongBallAccurate": "sum",
        "length_passLongBallInaccurate": "sum",
        "length_shortPassAccurate": "sum",
        "length_shortPassInaccurate": "sum",
        "type_passCornerAccurate": "sum",
        "type_passCornerInaccurate": "sum",
        "type_passFreekickAccurate": "sum",
        "type_passFreekickInaccurate": "sum",
        "type_passCrossInaccurate": "sum",
        "type_passCrossAccurate": "sum",
    }
)
passes_avg = passes.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "length_passTotal": "mean",
        "length_passLongBallAccurate": "mean",
        "length_passLongBallInaccurate": "mean",
        "length_shortPassAccurate": "mean",
        "length_shortPassInaccurate": "mean",
        "type_passCornerAccurate": "mean",
        "type_passCornerInaccurate": "mean",
        "type_passFreekickAccurate": "mean",
        "type_passFreekickInaccurate": "mean",
        "type_passCrossInaccurate": "mean",
        "type_passCrossAccurate": "mean",
    }
)
