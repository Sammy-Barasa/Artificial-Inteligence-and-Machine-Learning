#retrieving the data
import requests
url="https://raw.githubusercontent.com/priyanka-kasture/ML-Algorithms/master/Regression/SimpleLinearRegression/Salary_Data.csv"
response=requests.get(url,allow_redirects=True)

with open("Salary_Data.csv","wb") as f:
    f.write(response.content)
