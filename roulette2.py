Roulette

import random
from collections import Counter

a = [50, 30, 15, 5]

out = []
for _ in range(100):
    o = random.choices(a, a)
    out.append(o[0])

Counter(out)
