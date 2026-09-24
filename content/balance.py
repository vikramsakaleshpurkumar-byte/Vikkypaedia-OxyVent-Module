from gen import move_answer
# (unit, checkpoint index, new position of the correct option) — balances the key to 10/10/10/10
MOVES = [
    (1, 0, 0), (3, 0, 0), (7, 1, 0), (11, 0, 0), (13, 1, 0), (14, 0, 0), (16, 1, 0), (17, 0, 0), (20, 1, 0),
    (2, 0, 3), (3, 1, 3), (6, 1, 3), (11, 1, 3), (13, 0, 3), (16, 0, 3), (19, 1, 3),
    (10, 0, 3), (18, 0, 3),
]
for n, qi, t in MOVES:
    move_answer(n, qi, t)
