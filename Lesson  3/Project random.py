import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
# Fill missing values
df["Age"]      = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop unneeded columns
df.drop(columns=["Name", "PassengerId"], inplace=True)

# Encode / derive new columns
df["Survived_Label"] = df["Survived"].map({0: "Did not survive", 1: "Survived"})

df["Age_Band"] = pd.cut(df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child (≤12)", "Teen (13–18)", "Young Adult (19–35)",
            "Middle-Aged (36–60)", "Senior (61+)"])

df["Pclass_Label"] = df["Pclass"].map({1: "1st Class", 2: "2nd Class", 3: "3rd Class"})
df["Port"]         = df["Embarked"].map({"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"})
# Chart 1 — Count plot: who survived?
sns.countplot(data=df, x="Survived_Label", hue="Survived_Label",
              palette=["#E07B72", "#6AAE8D"], legend=False)

# Chart 2 — Bar plot: survival rate by passenger class
sns.barplot(data=df, x="Pclass_Label", y="Survived", hue="Pclass_Label",
            palette="Blues_d", estimator=np.mean, legend=False)

# Chart 3 — Histogram + KDE: age by survival outcome
sns.histplot(data=df, x="Age", hue="Survived_Label",
             multiple="stack", kde=True, palette=["#E07B72", "#6AAE8D"])

# Chart 4 — Bar plot: survival rate by sex
sns.barplot(data=df, x="Sex", y="Survived", hue="Sex",
            palette=["#5B8DB8", "#E8A0A0"], estimator=np.mean, legend=False)

# Chart 5 — Violin plot: fare spread by class
sns.violinplot(data=df, x="Pclass_Label", y="Fare", hue="Pclass_Label",
               palette="Set2", inner="quartile", legend=False)

# Chart 6 — Bar plot: survival rate by age band
sns.barplot(data=age_band_data, x="Age_Band", y="Survival Rate",
            hue="Age_Band", palette="viridis", legend=False)

# Chart 7 — Count plot: passengers per port, split by survival
sns.countplot(data=df, x="Port", hue="Survived_Label",
              palette=["#E07B72", "#6AAE8D"])

# Chart 8 — Heatmap: feature correlations
corr = df[["Survived","Pclass","Age","SibSp","Parch","Fare"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)

# Chart 9 — Pair plot: age, fare, class coloured by outcome
sns.pairplot(pair_df, hue="Outcome",
             palette={"Did not survive": "#E07B72", "Survived": "#6AAE8D"},
             diag_kind="kde", plot_kws={"alpha": 0.6})

# Chart 10 — Box plot: age by class and sex
sns.boxplot(data=df, x="Pclass_Label", y="Age", hue="Sex",
            palette=["#5B8DB8", "#E8A0A0"])