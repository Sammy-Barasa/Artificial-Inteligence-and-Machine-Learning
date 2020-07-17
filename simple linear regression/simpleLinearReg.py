#imports
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#Loading the data from a csv
dataset=pd.read_csv("Salary_Data.csv")

#Data pre processing for salary vs experience 

x=dataset.iloc[:,:-1].values

print(x)

y=dataset.iloc[:,1].values

print(y)

#spliting the data into Training set and Test set

linear_regressor=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=1/3)

#Generating the model on training dataset

linear_regressor.fit(x_train,y_train)

#Evaluating model on testing dataset
y_predicted=linear_regressor.predict(x_test)

#Visualising the results
    #for training

plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,linear_regressor.predict(x_train),color="blue")
plt.title("Salary vs Experience(training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

    #for test

plt.scatter(x_test,y_test,color="red")
plt.plot(x_train,linear_regressor.predict(x_train),color="blue")
plt.title("Salary vs Experience(Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()