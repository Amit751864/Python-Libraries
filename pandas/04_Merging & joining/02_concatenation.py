#data frame add vertically ya horizontally
#pd.concat([df1,df2],axis=0,ignore_index=TRue)import pandas as pd
import pandas as pd
df_region1=pd.DataFrame({
    "Customer ID":[1,2],
    "Name":["Amit","Mahesh"]
})
df_region2=pd.DataFrame({
    "Customer ID":[3,4],
    "Name":["Karan","Varun"]
})
#vertically
df_concate = pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concate)
#horizontally
df_concate1 = pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concate1)
