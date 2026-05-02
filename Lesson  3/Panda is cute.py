import pandas as pd

data = {
    "calories": [420, 380, 390, 450, 500, 480],
    "duration": [50, 40, 45, 60, 55, 50]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)