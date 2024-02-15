"""
Lista de listas e seus índices
"""
# salas = [
#     #0          1
#     ['maria', 'Helena', ], # 0
#     # 0
#     ['Elaine', ], # 1
#     # 0       1         2
#     ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
# ]

# print(salas [1][0])
# print(salas [0][1])
# print(salas [2][2])
# print(salas [2][3][3])

# for sala in salas:
#     print(sala)

salas = [
    #0          1
    ['maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1         2
    ['Luiz', 'João', 'Eduarda', ], # 2
]

# print(salas [1][0])
# print(salas [0][1])
# print(salas [2][2])
# print(salas [2][3][3])

for sala in salas:
    print(f'Na sala da {sala} os alunos são. ')
    for aluno in sala:
        print(aluno)