import pandas as Pandas
import re
import matplotlib.pyplot as plt

f=Pandas.read_csv("data.csv")
print("QUESTION 1\n")
print(f)

print("\n--------------------------------------------------------------")


print("\n QUESTION 2 \n")
print("Basic statistical description about the data.\n")
print(f.describe())

print("\n-------------------------------------------------------------\n")


print("\n QUESTION 3 \n")

print("Calories  sum = "+"",f['Calories'].isna().sum())

print("Calories mean = "+"",f['Calories'].mean())
print(f)
f=f.fillna(f.mean())
print(f)
print("\n------------------------------------------------------------\n")


print("\n QUESTION 4 \n")
print(f.groupby('Duration').agg({'Maxpulse': ['mean', 'min', 'count', 'max']}))
print("\n------------------------------------------------------------\n")


print("\n QUESTION 5 \n")
print(f[(f['Calories']>500) & (f['Calories']<1000)])
print("\n------------------------------------------------------------\n")


print("\n QUESTION 6 \n")
print(f[(f['Calories']>500) & (f['Pulse']<100)])
print("\n-----------------------------------------------------------\n")



print("\n QUESTION 7 \n")
f_modified=f.drop("Maxpulse",axis=1)
print(f_modified)
print("\n-----------------------------------------------------------\n")


print("\n QUESTION 8 \n")
print(f.drop("Maxpulse",axis=1))
print("\n----------------------------------------------------------\n")


print("\n QUESTION 9 \n")
f["Calories"] = f["Calories"].astype(float).astype(int)
print(f)
print("\n----------------------------------------------------------\n")


print("\n QUESTION 10 \n")
f.plot.scatter(x='Duration',y='Calories')
plt.show()
print("\n----------------------------------------------------------\n")
