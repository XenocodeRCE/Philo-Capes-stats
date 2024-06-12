import pandas as pd
import matplotlib.pyplot as plt

data_capes = {
    "Année":    [2023,  2022,   2021,   2020,   2019,   2018,   2017,   2016,   2015,   2014,   2013,   2012,   2011,   2010,   2009,   2008,   2007,   2006,   2005,   2004,   2003],
    "Postes":   [121,   129,    129,    130,    120,    80,     100,    110,    103,    80,     80,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60],
    "Inscrits": [1380,  1412,   1866,   None,   1758,   792,    1756,   1630,   1497,   1505,   1082,   927,    918,    1130,   1096,   1375,   1440,   1594,   1603,   1783,   1929],
    "Présents": [846,   833,    1085,   1212,   1043,   1026,   1038,   1115,   1012,   1031,   606,    488,    448,    667,    672,    841,    934,    1020,   1082,   1216,   1363],
    "Admis" :   [121,   129,    129,    130,    120,    80,     104,    110,    103,    80,     79,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60]
}

data_cafep = {
    "Année":    [2023,  2022,   2021,   2020,   2019,   2018,   2017,   2016,   2015,   2014,   2013,   2012,   2011,   2010,   2009,   2008,   2007,   2006,   2005,   2004,   2003],
    "Postes":   [20,    20,     20,     22,     20,     20,     25,     25,     20,     20,     10,     20,     20,     20,     5,      9,      10,     15,     20,     20,     40],
    "Inscrits": [275,   276,    317,    None,   318,    326,    299,    273,    218,    208,    208,    218,    210,    229,    22,     239,    244,    287,    299,    213,    171],
    "Présents": [164,   150,    159,    None,   188,    184,    171,    157,    122,    118,    106,    101,    115,    144,    143,    170,    152,    179,    197,    149,    115],
    "Admis" :   [20,    20,     20,     22,     20,     20,     25,     25,     19,     19,     9,      9,      10,     8,      5,      7,      5,      4,      7,      10,     5]
}




df = pd.DataFrame(data_cafep)
# Calculate the number of postes par admis
df['Postes/Admis'] = df['Postes'] / df['Admis']

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(df['Année'], df['Postes/Admis'], marker='o', color='orange', label='Postes/Admis')

plt.xlabel('Année')
plt.ylabel('Postes par Admis')
plt.title('Évolution du nombre de postes par admis')
plt.legend()
plt.grid(True)
plt.xticks(df['Année'], rotation=45)
plt.tight_layout()

plt.show()
