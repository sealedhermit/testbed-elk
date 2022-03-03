import pandas as pd
import os
    
def DataStore(category,price,storage,ram,battery,display,network):
    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        df=df.append(pd.DataFrame([[category,price,storage,ram,battery,display,network]],
                        columns=["category","price","storage","ram","battery","display","network"]))
        df.to_excel("user_data.xlsx",index=False)
    else:
        df=pd.DataFrame([[category,price,storage,ram,battery,display,network]],
                        columns=["category","price","storage","ram","battery","display","network"])
        df.to_excel("user_data.xlsx",index=False)
    return []
