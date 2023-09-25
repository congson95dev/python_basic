import numpy as np
import pandas as pd

# create numpy as normal, nothing new so far
my_list = [1402, 548, 1122]
my_arr = np.array(my_list)
print(my_arr[1])  # result: 548

"""
Series
"""
# transfer from numpy array to pandas series
my_series = pd.Series(my_arr)
print(my_series)
# result:
# 0    1402
# 1     548
# 2    1122
print(my_series[1])  # result: 548

# transfer from numpy array to pandas series with name
# with this name, now we can access to it by name, Ex: my_series["Tom"]
name = ["Ellie", "Tom", "Mike"]
my_series = pd.Series(my_arr, name)
print(my_series)
# result:
# 0     Ellie    1402
# 1     Tom       548
# 2     Mike     1122
print(my_series[1])  # result: 548
print(my_series["Tom"])  # result: 548

# we could use dictionary for THE SAME RESULT
my_dict = {"Ellie": 1402, "Tom": 548, "Mike": 1122}
my_series = pd.Series(my_dict)
print(my_series)
# result:
# 0     Ellie    1402
# 1     Tom       548
# 2     Mike     1122
print(my_series[1])  # result: 548
print(my_series["Tom"])  # result: 548

"""
Series operator
"""
my_dict = {"Ellie": 1402, "Tom": 548, "Mike": 1122}
my_other_dict = {"Ellie": 1202, "Tom": 221, "Ted": 200}
my_series = pd.Series(my_dict)
my_other_series = pd.Series(my_other_dict)

print(my_series + my_other_series)
# result:
# Ellie    2604.0
# Mike        NaN
# Ted         NaN
# Tom       769.0
# it got NaN because "Mike" doesn't exists on the 2nd serires, vice versa for "Ted"

# but with the add() function,
# we can use fill_value to treat the unavailable data with 0 or whatever number we want
print(my_series.add(my_other_series, fill_value=0))
# result:
# Ellie    2604.0
# Mike     1122.0
# Ted       200.0
# Tom       769.0

"""
DataFrame
"""
a = np.random.randint(1, 2000, (4, 3))
name = ["Ellie", "Tom", "Mike", "Ted"]
months = ["April", "May", "June"]

my_df = pd.DataFrame(a, index=name, columns=months)
print(my_df)
# result:
#        April  May  June
# Ellie      0    0     2
# Tom        3    1     2
# Mike       7    0     8
# Ted        7    7     3

# create DataFrame from csv file
my_df = pd.read_csv("./pandas_test_data/cars.csv")
print(my_df)  # result: show all data of csv file
print(my_df.head())  # result: show header + first 5 column of csv file

# condition
print(my_df["year"])  # result: show all data of year as Series
print(my_df["year"] > 2015)  # result: show all data of year as Series as True or False
condition = my_df["year"] > 2015
print(my_df[condition])  # result: show all data of csv file matched to the condition

# multiple condition
condition = (my_df["year"] > 2015) & (my_df["finance"] == "yes")
print(my_df[condition])  # result: show all data of csv file matched to the condition
condition = (my_df["year"] > 2015) | (my_df["finance"] == "yes")
print(my_df[condition])  # result: show all data of csv file matched to the condition
condition = my_df["day"].isin(["Mon", "Sun", "Thur"])
print(my_df[condition])  # result: show all data of csv file matched to the condition


"""
methods
"""


def calculate_total_price(price):
    return price * 1.13


# apply()
# create new column "total_price" and calculate it based on "price"
my_df["total_price"] = my_df["price"].apply(calculate_total_price)
print(my_df)


def calculate_profit(price, finance):
    if finance == "yes":
        if price > 20000:
            return "HIGH"
        else:
            return "LOW"
    else:
        if price > 5000:
            return "HIGH"
        else:
            return "LOW"


# vectorize() (this come from numpy, not pandas)
# it allow us to transfer multiple params to the function
my_df["profit"] = np.vectorize(calculate_profit)(my_df["price"], my_df["finance"])
print(my_df)

# describe()
print(my_df.describe())  # describe on the vertical
print(my_df.describe().transpose())  # describe on the horizon, easier to watch

# sort()
print(my_df.sort_values("price"))  # it will sort from lowest to highest
print(my_df.sort_values(["price", "year"]))  # it will sort from lowest to highest

# max, min(),
print(my_df["price"].max())  # result: 232000
print(my_df["price"].min())  # result: 2235

# idxmax()
# get index of record which have max price
print(my_df["price"].idxmax())  # result: 44

# iloc()
# get record data of index
print(my_df.iloc[44])  # result: data of record with index = 44
print(my_df.iloc[my_df["price"].idxmax()])  # result: same as above

# between()
print(my_df[my_df["price"].between(10000, 20000)])

# value_counts()
# count how many value the data have,
# Ex: the column "sex" have 26 records with value "M", and 19 records with value "F"
print(my_df["sex"].value_counts())  # result: M 26 F 19

# replace()
# replace value of column "sex" with another value
my_df["sex"] = my_df["sex"].replace(to_replace="M", value="male")
my_df["sex"] = my_df["sex"].replace(to_replace="F", value="female")
print(my_df)

# duplicated()
# find duplicated records and return true or false for every records
# "duplicated" here mean every columns in the record is the same as the other record
print(my_df.duplicated())
print(my_df[my_df.duplicated()])  # result: data of records 35 and 38

# unique(), nunique()
print(my_df["car"].unique())  # result: list of "car" which unique
print(my_df["car"].nunique())  # result: 19, number of "car" which unique

# groupby()
# group by "dealer" and select column "price"
print(my_df.groupby("dealer").sum()["price"])
# result:
# dealer       price
# Brittany     248086
# Maddy        363855
# Mike        1099353
# Sam          442831
# Turner       292677

# we could do group by for multiple column
print(my_df.groupby(["dealer", "year"]).sum()["price"])
# result:
# dealer    year     price
# Brittany  2000      2333
#           2002      3553
#           2015     85312
#           2020     78444
#           2021     78444
# Maddy     2011      7434
#           2014     17434
#           2017     40434
#           2020    140553
#           2021    158000
# Mike      2015     42953
#           2016     23998
#           2017    119027
#           2018     22333
#           2019     39000
#           2020    548492
#           2021    249550
#           2022     54000
# Sam       2012      9855
#           2014     25356
#           2018     27433
#           2020    126844
#           2021    253343
# Turner    2000      3500
#           2004      2235
#           2010     10983
#           2013     45633
#           2015     52000
#           2018     76550
#           2019     57744
#           2021     44032

# get data of 2 rows where "dealer" is "Mike" and "Sam"
dealer_year = my_df.groupby(["dealer", "year"])["price"].sum()
print(dealer_year.loc[["Mike", "Sam"]])

# get data of row "dealer" is "Mike" and "year" = 2015
print(dealer_year.loc[("Mike", 2015)])
