import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#fur_colors = data["Primary Fur Color"].nunique()
fur_colors=['Gray','Cinnamon','Black']
#print(fur_colors)
#grey_squirels=data["Primary Fur Color"]=='Grey'

#print(grey_squirels.count())
data_dict ={}
for fur_color in fur_colors:
    num_squirels = 0
    my_squirels = (data[data["Primary Fur Color"]==fur_color])
    #print(my_squirels)
    num_squirels =  len(my_squirels)    #my_squirels.count()

    data_dict.update({"Fur Color" :fur_color , "Count": num_squirels})
    print(f"{fur_color} {num_squirels}")
print(data_dict)

df=pandas.DataFrame(data_dict)
df.to_csv("Squirels.csv")
