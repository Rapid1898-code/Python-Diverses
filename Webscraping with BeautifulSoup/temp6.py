import pandas as pd
import numpy as np
from openpyxl import load_workbook


#l = [[1,2,3],[4,5,6],[7,8,9]]
#l2 = [[3,2,1],[6,5,4],[9,8,7]]
#df = pd.DataFrame(l)
#df.to_excel("test.xlsx", sheet_name="test2", header=False, index=False)

x1 = np.random.randn(100, 3)
df1 = pd.DataFrame(x1)

writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter')
df1.to_excel(writer, sheet_name = 'x1', header=False, index=False)
writer.save()
writer.close()

####################################

book = load_workbook("test.xlsx")
writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter')
writer.book = book

x3 = np.random.randn(100, 2)
df3 = pd.DataFrame(x3)
df3.to_excel(writer, sheet_name = 'x3', header=False, index=False)
writer.save()
writer.close()

