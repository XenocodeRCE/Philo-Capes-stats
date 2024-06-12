import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Année":    [2023,  2022,   2021,   2020,   2019,   2018,   2017,   2016,   2015,   2014,   2013,   2012,   2011,   2010,   2009,   2008,   2007,   2006,   2005,   2004,   2003],
    "Postes":   [121,   129,    129,    130,    120,    80,     100,    110,    103,    80,     80,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60],
    "Inscrits": [1380,  1412,   1866,   None,   1758,   792,    1756,   1630,   1497,   1505,   1082,   927,    918,    1130,   1096,   1375,   1440,   1594,   1603,   1783,   1929],
    "Présents": [846,   833,    1085,   1212,   1043,   1026,   1038,   1115,   1012,   1031,   606,    488,    448,    667,    672,    841,    934,    1020,   1082,   1216,   1363],
    "Admis" :   [121,   129,    129,    130,    120,    80,     104,    110,    103,    80,     79,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60]

}

df = pd.DataFrame(data)

df['Postes/Inscrits'] = df['Postes'] / df['Inscrits']

plt.figure(figsize=(10, 6))

plt.plot(df['Année'], df['Postes/Inscrits'], marker='o', color='red', label='Postes/Inscrits')

plt.xlabel('Année')
plt.ylabel('Postes par Inscrits')
plt.title('Évolution du nombre de postes par inscrits')
plt.legend()
plt.grid(True)
plt.xticks(df['Année'], rotation=45)
plt.tight_layout()
plt.show()
