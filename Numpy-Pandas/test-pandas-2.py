import pandas

# no_value=[' ']
# df=pandas.read_csv('douban.csv',dtype=str,na_values=no_value)
# print(df[['影片外国名']].to_string())

no_value=[' ']
df=pandas.read_csv('douban.csv',na_values=no_value)
new_df=df.dropna(axis=0)
# print(df[['影片外国名']].isnull())
# new_df.to_csv('dropna_douban.csv')
print(new_df['影片外国名'].to_string())