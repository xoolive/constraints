Nv = 19
# Gatwick, Heathrow, Bruxelles, Berlin, Roissy, Orly, Munich, Toulouse, Rome, Madrid
Na = 10
# Londres, Bruxelles, Berlin, Paris, Munich, Toulouse, Rome, Madrid
Ni = 8  
# ville des aéroports
Va = [0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8]  
# origine des vols
Ov = [0, 1, 1, 10, 2, 2, 5, 7, 3, 5, 4, 4, 7, 8, 6, 9, 9, 8, 9, 10]
# destination des vols
Dv = [0, 6, 8, 1, 3, 4, 2, 2, 4, 3, 5, 7, 5, 6, 9, 7, 8, 10, 10, 6]

Td = [
    0,
    8,
    9,
    22,
    6,
    7,
    21,
    22,
    12,
    8,
    16,
    17,
    21,
    23,
    11,
    18,
    19,
    16,
    16,
    21,
]  # heure de décollage
Ta = [
    0,
    9,
    11,
    24,
    7,
    9,
    22,
    24,
    13,
    9,
    18,
    18,
    22,
    24,
    13,
    19,
    21,
    18,
    18,
    23,
]  # heure d'atterrissage

# temps de transfert d'un aéroport à l'autre
Dt = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 4, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 4, 2, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 25, 25, 2, 25, 25, 25, 25, 25, 25, 25],
    [0, 25, 25, 25, 2, 25, 25, 25, 25, 25, 25],
    [0, 25, 25, 25, 25, 2, 4, 25, 25, 25, 25],
    [0, 25, 25, 25, 25, 4, 2, 25, 25, 25, 25],
    [0, 25, 25, 25, 25, 25, 25, 2, 25, 25, 25],
    [0, 25, 25, 25, 25, 25, 25, 25, 2, 25, 25],
    [0, 25, 25, 25, 25, 25, 25, 25, 25, 2, 25],
    [0, 25, 25, 25, 25, 25, 25, 25, 25, 25, 2],
]

# temps infini
Dtinf = 25

# capacité de l'avion
Np = [
    0,
    100,
    100,
    100,
    100,
    100,
    200,
    100,
    50,
    100,
    100,
    50,
    100,
    100,
    100,
    50,
    50,
    50,
    50,
    100,
]

# personnel requis
Nec = [0, 3, 3, 3, 3, 3, 4, 3, 2, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 2]

# prix de vente d'une place
Pr = [
    0,
    100,
    200,
    200,
    100,
    200,
    100,
    200,
    100,
    100,
    200,
    100,
    100,
    100,
    200,
    100,
    200,
    200,
    200,
    200,
]

# nombre d'employés
Ne = 42

# pilote (1) ou cabine (0)
Ty = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

# domicile de l'employé
Vh = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
]

# nombre maximal de vols par employé par jour
Nvmax = 4

# durée maximale d'absence
Dmax = 24

# durée de transfert domicile-aéroport
Dda = 2
