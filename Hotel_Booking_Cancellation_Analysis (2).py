import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np


df=pd.read_csv("hotel_bookings 2.csv")


df.head()


df.columns


df.info()


df['reservation_status_date']= pd.to_datetime(df['reservation_status_date'],format= "mixed",dayfirst=True)


df.info()


for col in df.describe(include="object"):
    print(col)
    print(df[col].unique())
    print('--'*25)


df.isnull().sum()


df.drop(['agent','company'],axis=1,inplace=True)
df.dropna(inplace=True)


df.describe()


df=df[df['adr']<5000]


df.describe()


cancel_record=df['is_canceled'].value_counts(normalize=True)


cancel_record


plt.figure(figsize=(5,4))
plt.title('Reservation graph')
plt.bar(['not canceled','canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.5)
plt.show()


plt.figure(figsize=(7,3))
sns.countplot(x='hotel' , hue='is_canceled',data=df,palette='pink')


plt.legend(['not cancel','cancel'])
plt.show()


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


plt.figure(figsize=(20,10))

plt.plot(resort_hotel.index, resort_hotel["adr"], label='resort')
plt.plot(city_hotel.index, city_hotel["adr"], label='city')
plt.grid(True)
plt.legend(fontsize=15)


df.info()


df['month']= df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
sns.countplot(x='month',hue='is_canceled',data=df,palette='pink')
plt.legend(['not cancel','cancel'])


plt.figure(figsize=(15,6))
addre=df[df['is_canceled']==1].groupby('month')['adr'].sum().reset_index()
sns.barplot(x='month',y='adr',data=addre,palette='pink' )        


cancel=df[df['is_canceled']==1]
country=cancel['country'].value_counts(normalize=True)[:10]
plt.pie(country,labels=country.index,autopct='%.2f',shadow=True)
plt.legend(['rate_of cancelation','other'])

