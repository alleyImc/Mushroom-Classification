import pandas as pd

column_names = [
    "class", "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
    "gill-attachment", "gill-spacing", "gill-size", "gill-color",
    "stalk-shape", "stalk-root", "stalk-surface-above-ring",
    "stalk-surface-below-ring", "stalk-color-above-ring",
    "stalk-color-below-ring", "veil-type", "veil-color",
    "ring-number", "ring-type", "spore-print-color",
    "population", "habitat"
]

# download dataset
file_path = "data/agaricus-lepiota.data"
data = pd.read_csv(file_path, names=column_names)
print(data.head())

df = pd.read_csv(file_path, names=column_names)
pd.set_option('display.max_columns', None)
print(df.head())

