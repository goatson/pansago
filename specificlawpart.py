import pandas as pd

df = pd.read_csv('./law_list_detail.csv')
# print(df)

subset = df.loc[:, ['law_court_name'], ['law_event_type']]


# subset = df.iloc[:, [2, 4, -1]]
# print(subset.head())

# small_range = list(range(5))
# print(small_range)


# small_range = list(range(0, 6, 2))
# print(range(0, 6, 2))
# subset = df.iloc[:, small_range]
# print(subset.head())