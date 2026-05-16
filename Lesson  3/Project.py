import seaborn as sns
import matplotlib.pyplot as plt

# Example: scatter plot with histograms on the axes
sns.jointplot(data=df, x="column1", y="column2", kind="reg") 
plt.show()
