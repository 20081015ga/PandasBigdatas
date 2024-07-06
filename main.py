import pandas as pd 

data = {
        'Nome' : ['Grylo', 'Bob', 'Wanderson', 'Jõ Soares'],
        'Idade' : [55, 10, 70, 10],
        'Cidade': ['Brazilandia', 'Valinhos', 'Barão Geraldo', 'São Paulo']
  
  
}

df = pd.DataFrame(data)
print(df)