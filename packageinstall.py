import pandas as pd
import numpy as np

# data= np.array(['g','e','h','k'])
# ser= pd.Series(data)
# print(ser)kl'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# creating dataframe using list

lst=[1,2,3,4,5]
df=pd.DataFrame([lst,lst,lst,lst,lst,lst,lst,lst],  columns=['A',"B",'C','D','E'])
print(df)

# initialise data of lists:]
data=pd.DataFrame({"Name": ['Tom','nick','krish','jack'],'Age':[20,23,31,19]})
#create DataFrame
df=pd.DataFrame(data)
#print the output
print(df)

#deleting a dataframe
pd.DataFrame()
df=pd.read_csv(r"C:\Users\Treksha Pachadhare\Downloads\googleplaystore.csv") 
print(df.head(10))
print(df.columns)

#sum of all ratings
df_clean= df.dropna(subset=['Rating'])
average_rating= df_clean['Rating'].mean()
print("Average rating of these apps:",round(average_rating, 2))

# s=0
# for i in df['Rating']:
#     s+=i
# s=float(s)
# print(s/len(df['Rating']))
 
# how many apps have a rating between 4 and 4.5
c=0
for i in df['Rating']:
    if 4.0<=i<=4.5:
        c+=1          
print("there are",c,'apps with rating between 4-4.5')

# finding average number of reviews
# s=0
# for i in df['Reviews']:
#     s+=int(i)
# print(int(s/len(df['Reviews'])))

#printing the category
for i in df['Category'].unique():
    print(i)

# total number of catrgory
categories={} 
for name in df['Category'].unique():
    ct=0
    for i in df['Category']:
        if(i==name):
            ct +=1
    categories[name]=ct        
print(categories)

#know the number of paid applicant 
p=0
for i in df["Type"]:
    if (i=='Paid'):
        p+=1
print("there are",p," paid applicant")
print(df["Content Rating"].unique())
print(df['Type'].describe())
print('....................................')

df= pd.read_csv("data.csv")
print(df)
print('................................')

# removing rows with null values
pd=df.dropna()
print(pd) 

# filling null values using Imputation
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imputer.fit(df.iloc[:,1:3].values)
df.iloc[:,1:3] = imputer.transform(df.iloc[:,1:3].values)
df


