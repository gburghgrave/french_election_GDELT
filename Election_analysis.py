import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import axis, pie, show
from pymongo import MongoClient

# CHOSE DB AND COLLECTION
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")

db = client.GDELT
coll = db.June2017

# FIND EVENTS
events = coll.aggregate([{'$match': {'ActionGeo_CountryCode': {'$in': ['FR']}}}], allowDiskUse=True)
data = list(events)
events.close()
df = pd.DataFrame(data)

"""# Remove rows with NaN values
df = df.replace('null', np.nan, regex=True)
df = df[df['Actor1Geo_CountryCode'].notna()]
df = df[df['Actor2Geo_CountryCode'].notna()]

# 01. GET ALL EVENTS BY FILTERING ONE FIELD
filt = coll.find({"Actor1CountryCode": "FRA"})
for filt_all in filt:
   print(filt_all)
   
print(len(filt_all))

# 02. GET TOTAL NUMBER OF DOCUMENTS
number_of_events = coll.count_documents({})
print(number_of_events)

# 03. NUMBER OF EVENTS PER MONTH
df.groupby('MonthYear')['_id'].nunique().plot(kind='bar')
plt.title('NUMBER OF EVENTS PER MONTH')
plt.xlabel('Month')
plt.ylabel('Number of events')
show()

# 04. NUMBER EVENTS BY THEIR KIND PER MONTH
df.groupby(['MonthYear', 'EventRootCode'])[
    '_id'].nunique().unstack('MonthYear').plot(kind='bar')
plt.title('KIND OF EVENTS PER MONTH')
plt.xlabel('Event code')
plt.ylabel('Number of occurrences')
show()"""

# 05. TOP 5 KIND OF EVENTS WITH MOST FREQUENCY
sums = df.groupby('Actor1Type1Code')['_id'].nunique().nlargest(5)
pie(sums, labels=sums.index, autopct='%1.1f%%')
axis('equal')
plt.title('TOP KIND OF ACTOR1 IN FRANCE')
plt.xlabel('Actor code')
plt.ylabel('Number of occurrences')
show()

sums = df.groupby('Actor2Type1Code')['_id'].nunique().nlargest(5)
pie(sums, labels=sums.index, autopct='%1.1f%%')
axis('equal')
plt.title('TOP KIND OF ACTOR2 IN FRANCE')
plt.xlabel('Actor code')
plt.ylabel('Number of occurrences')
show()

"""# 06. TOP FREQUENT COUNTRIES PER MONTH (ACTOR 1)
df.groupby(['MonthYear', 'Actor1Geo_CountryCode'])['_id'].nunique().nlargest(
    20).unstack('Actor1Geo_CountryCode').plot.bar()
plt.title('TOP COUNTRIES PER MONTH FOR ACTOR 1')

# 07. TOP FREQUENT COUNTRIES PER MONTH (ACTOR 2)
df.groupby(['MonthYear', 'Actor2Geo_CountryCode'])['_id'].nunique().nlargest(
    20).unstack('Actor2Geo_CountryCode').plot.bar()
plt.title('TOP COUNTRIES PER MONTH FOR ACTOR 2')

 #Axis names
plt.ylabel('Number of occurrences')
plt.xlabel('Month')
show()"""

