import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Année":    [2023,  2022,   2021,   2020,   2019,   2018,   2017,   2016,   2015,   2014,   2013,   2012,   2011,   2010,   2009,   2008,   2007,   2006,   2005,   2004,   2003],
    "Postes_cafep":   [20,    20,     20,     22,     20,     20,     25,     25,     20,     20,     10,     20,     20,     20,     5,      9,      10,     15,     20,     20,     40],
    "Postes_capes":   [121,   129,    129,    130,    120,    80,     100,    110,    103,    80,     80,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60],
    "Inscrits_cafep": [275,   276,    317,    None,   318,    326,    299,    273,    218,    208,    208,    218,    210,    229,    22,     239,    244,    287,    299,    213,    171],
    "Inscrits_capes": [1380,  1412,   1866,   None,   1758,   792,    1756,   1630,   1497,   1505,   1082,   927,    918,    1130,   1096,   1375,   1440,   1594,   1603,   1783,   1929],
    "Présents_cafep": [164,   150,    159,    None,   188,    184,    171,    157,    122,    118,    106,    101,    115,    144,    143,    170,    152,    179,    197,    149,    115],
    "Présents_capes": [846,   833,    1085,   1212,   1043,   1026,   1038,   1115,   1012,   1031,   606,    488,    448,    667,    672,    841,    934,    1020,   1082,   1216,   1363],
    "Admis_cafep" :   [20,    20,     20,     22,     20,     20,     25,     25,     19,     19,     9,      9,      10,     8,      5,      7,      5,      4,      7,      10,     5],
    "Admis_capes" :   [121,   129,    129,    130,    120,    80,     104,    110,    103,    80,     79,     50,     32,     32,     26,     26,     30,     30,     48,     38,     60]
}



df = pd.DataFrame(data)



# Replace 'None' with NaN
df['Inscrits_cafep'] = df['Inscrits_cafep'].astype('float')
df['Inscrits_capes'] = df['Inscrits_capes'].astype('float')
df['Présents_cafep'] = df['Présents_cafep'].astype('float')


plt.plot(df['Année'], df['Postes_capes'], marker='o', color='red', label='Postes CAPES')
plt.plot(df['Année'], df['Postes_cafep'], marker='o', color='blue', label='Postes CAFEP')

plt.plot(df['Année'], df['Inscrits_capes'], marker='o', color='brown', label='Inscrits CAPES')
plt.plot(df['Année'], df['Inscrits_cafep'], marker='o', color='dodgerblue', label='Inscrits CAFEP')

plt.xlabel('Année')
plt.ylabel('Nombre')
plt.title('Évolution du nombre de postes, inscrits et présents au CAPES')
plt.legend()
plt.grid(True)
plt.xticks(df['Année'], rotation=45)
plt.tight_layout()

plt.show()
