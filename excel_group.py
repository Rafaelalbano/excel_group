import pandas as pd
df = pd.read_excel('arq01.xlsx')
df_new = df.groupby('USER_ID')['COMPUTER_ID'].apply(list).reset_index(name='new')
print(df_new)
df_new.to_excel(r'arq01_novo.xlsx', index=False)

