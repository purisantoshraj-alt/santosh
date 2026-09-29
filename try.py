
import pandas as pd
date ={
    "name" : ["ram","shyam","hari"],
    "score": [50,60,70,]
}
df= pd.DataFrame(data)
df["passed"]= df["score"]>=50
print (df)
print(df["score"].max())