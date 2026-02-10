import pandas
data=pandas.read_csv("weather_data.csv")
#print(data.temp)
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
temp_list= data["temp"].to_list()
temp_average = sum(temp_list)/len(temp_list)
print(temp_average)

#print max temp
print(data["temp"].max())

#print row containing max temp
print(data[data["temp"]==data["temp"].max()])
#same like
print(data[data.temp==data.temp.max()])

monday = data[data.day=="Monday"]
print(monday.condition)
