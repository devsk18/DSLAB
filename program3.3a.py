import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
plt.plot(iris["id"],iris["sepal.length"], "r--")
plt.show()
