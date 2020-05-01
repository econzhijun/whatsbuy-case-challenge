import pandas as pd

df1 = pd.DataFrame({'days': [1, 1, 2, 2, 1, 3, 4],
                   'values': [10, 10, 5, 3, -2, 4, 20]})
result1 = df1.groupby("days").agg(["mean", "median", "max", "min"])
result1.columns = [f"{agg}_{name}"for name, agg in result1.columns]
result1.reset_index(inplace=True)
print(result1)


df2 = pd.DataFrame({'employee': [1001, 1002, 1004, 1001,
                                 1001, 1002, 1004, 1005, 1005],
                    'pos': [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    'amount': [125, 542, 2345, 892,
                               100, 1234, 657, 34, 35]})
result2 = df2.groupby("employee").agg({"amount": ["max", "min"], "pos": "first"})
result2.columns = ["max_amount", "min_amount", "pos"]
result2["amount_diff"] = result2["max_amount"] - result2["min_amount"]
result2.sort_values(by="amount_diff", ascending=False, inplace=True)
result2 = result2.iloc[:2][["pos", "amount_diff"]].reset_index()
print(result2)