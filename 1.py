import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data_model/data_linear.csv")
X = data["Diện tích"]
Y = data["Giá"]
plt.xlabel('Diện tích')
plt.ylabel('Giá')
plt.plot(X,Y)
plt.show()


