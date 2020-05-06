import pandas as pd

# data = {"Asia":[0,0,0,0,0],"Europe":[0,0,0,0,0], "America":[0,0,0,0,0]}
# df  =  pd.DataFrame(data,  columns=["A","B","C","D])
# print(df)

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }
df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print(df)
