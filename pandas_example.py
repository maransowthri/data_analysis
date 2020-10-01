import pandas as pd


pokemon_data = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(pokemon_data.tail(5))
# print(type(pokemon_data.columns))
# print(type(pokemon_data['Name'][:5]))
# print(pokemon_data.head(1))
# print(type(pokemon_data.iloc[1,11]))
# print(type(pokemon_data.iloc[1,3]))

# for index, row in pokemon_data.iterrows():
#     print(index, row['Name'])

# print(pokemon_data.loc[pokemon_data['Type 1'] == 'Fire'])
# print(pokemon_data.loc[pokemon_data['Legendary'] == False])

# print(pokemon_data.sort_values('Name',ascending=False))

pokemon_data['Total'] = pokemon_data.iloc[:, 4:10].sum(axis=1)
pokemon_data.to_csv('updated_pokemon_data.csv', index=False)