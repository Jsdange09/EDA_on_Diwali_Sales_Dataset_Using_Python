import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\jayes\\OneDrive\\Desktop\\projects\\project_1\\C1.csv', encoding= 'unicode_escape')
# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.tail())
df.drop(['Status','unnamed1'], axis=1, inplace=True)
print(df.info())
print(pd.isnull(df).sum())
print(df.shape)
df.dropna(inplace=True)
print(df.shape)
df['Amount']=df['Amount'].astype('int')
print(df['Amount'].dtypes)
df.rename(columns={'Marital_Status':'shaadi'}, inplace=True)
print(df.info())
print(df.describe())
print(df[['Amount','Age']].describe())
ax= sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
ay= sns.barplot(x='Gender', y='Amount', data=sales)
for bars in ay.containers:
    ay.bar_label(bars)
plt.show()

az= sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in az.containers:
    az.bar_label(bars)
plt.show()

sales2=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
ax1=sns.barplot(x='Age Group', y='Amount', data=sales2)
for bars in ax1.containers:
    ax1.bar_label(bars)
plt.show()

sales3=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders' , ascending=False).head(10)
sns.set(rc={'figure.figsize':(18,5)})
ax2=sns.barplot(x='State',y='Orders' , data=sales3)
for bars in ax2.containers:
    ax2.bar_label(bars)
plt.show()

sales3=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False).head(10)
sns.set(rc={'figure.figsize':(18,5)})
ax2=sns.barplot(x='State',y='Amount' , data=sales3)
for bars in ax2.containers:
    ax2.bar_label(bars)
plt.show()

sns.set(rc={'figure.figsize':(4,5)})
ax3=sns.countplot(x='shaadi', data=df)

for bars in ax3.containers:
    ax3.bar_label(bars)
plt.show()

sales=df.groupby(['shaadi','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(4,5)})
ax3=sns.barplot(x='shaadi',y='Amount', hue='Gender', data=sales)
for bars in ax3.containers:
    ax3.bar_label(bars)
plt.show()

sns.set(rc={'figure.figsize':(20,5)})
ax3=sns.countplot(x='Occupation', data=df)

for bars in ax3.containers:
    ax3.bar_label(bars)
plt.show()

sales=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
ax3=sns.barplot(x='Occupation',y='Amount', data=sales)
for bars in ax3.containers:
    ax3.bar_label(bars)
plt.show()


sns.set(rc={'figure.figsize':(20,5)})
ax3=sns.countplot(x='Product_Category', data=df)

for bars in ax3.containers:
    ax3.bar_label(bars)
plt.show()

sales=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
ax3=sns.barplot(x='Product_Category',y='Amount', data=sales)
plt.show()

sales=df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
ax3=sns.barplot(x='Product_ID',y='Orders', data=sales)
plt.show()

