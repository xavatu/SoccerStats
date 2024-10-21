import pandas as pd


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
cards_total = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_yellowCard": "sum",
        "type_redCard": "sum",
    }
)
cards_avg = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "type_yellowCard": "mean",
        "type_redCard": "mean",
    }
)

clearances = pd.read_csv("./test/clearances.csv")
clearances_total = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_clearanceTotal": "sum"
    }
)
clearances_avg = blocks.groupby(["playerId"]).agg(
    {
        "apps": "sum",
        "minsPlayed": "sum",
        "success_clearanceTotal": ""
    }
)

dribbles = pd.read_csv("./test/dribbles.csv")

fouls = pd.read_csv("./test/fouls.csv")

goals = pd.read_csv("./test/goals.csv")

interception = pd.read_csv("./test/interception.csv")

key_passses = pd.read_csv("./test/key-passses.csv")

offsides = pd.read_csv("./test/offsides.csv")

passes = pd.read_csv("./test/passes.csv")

possession_loss = pd.read_csv("./test/possession-loss.csv")

saves = pd.read_csv("./test/saves.csv")

shots = pd.read_csv("./test/shots.csv")

tackles = pd.read_csv("./test/tackles.csv")
