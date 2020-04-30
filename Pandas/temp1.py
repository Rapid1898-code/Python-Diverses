import pandas as pd
df = pd.DataFrame(index=['A','B','C'], columns=['x','y'])

df._set_value("B","y",10)

print(df)
