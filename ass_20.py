#1
import pandas as pd
data= {'Name':  ['akshay','ak'],'age':[19,20],'p_no':['9816005789}','9827393847'],'email_id':['habbiakshay1@gmail.com','ak@gmail.com']}
df=pd.DataFrame(data)
print (df)

#2
import pandas as pd
df = pd.read_csv("weather.csv")
df.head()
df.tail()
df.head(10)
df.tail(5)
