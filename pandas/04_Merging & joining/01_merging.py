#pd.merge(df1,df2,on="column name",how="type of join")type of join are left,right,
import pandas as pd
df_customer =pd.DataFrame({
    "Customer ID": [1,2,3],
    "Name":["Amit","Ramesh","Mahesh"]
})

df_orders=pd.DataFrame({
    "Customer ID":[1,2,4],
    "OrderAmount":[255,340,260]
})
df_merged = pd.merge(df_customer,df_orders,on="Customer ID",how="inner")
print("inner merge")
print(df_merged)


df_merged = pd.merge(df_customer,df_orders,on="Customer ID",how="outer")
print("outer merge")
print(df_merged)# isme kya ha sabhi row ko combine karega aur jo value nhii hoga NaN fill kargea


df_merged = pd.merge(df_customer,df_orders,on="Customer ID",how="left")
print("left merge")
print(df_merged)#ya left wala liye haaa


df_merged = pd.merge(df_customer,df_orders,on="Customer ID",how="right")
print("right merge")
print(df_merged)#ya right wla liya haa


df_merged = pd.merge(df_customer,df_orders,how="cross")
print("cross merge")
print(df_merged)#mxn