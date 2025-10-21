from random import choice

n = 100
np = 100
n_wins = 0
n_lose = 0
goods = 0
amount = 0
check = 0
for _ in range(10000):
    airplane = {}

    passes = list(range(100))
    sits = list(range(100))
    fp = choice(passes)
    fs = choice(sits)

    airplane[fp] = fs
    passes.remove(fp)
    sits.remove(fs)

    np = len(passes)
    for i in range(np):
        rp = choice(passes)
        if rp in sits:
            rs = rp
            airplane[rp] = rs
            goods += 1
        else:
            rs = choice(sits)
            airplane[rp] = rs
        passes.remove(rp)
        sits.remove(rs)
        if i == np - 1:
            if airplane[rp] == rp:
                n_wins += 1
            else:
                n_lose += 1
    print(goods)
    amount += goods
    check += 1
    goods = 0
print(n_wins / 10000)
print(n_lose / 10000)
print(amount / check)