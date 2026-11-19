import argparse

p = argparse.ArgumentParser()
p.add_argument('n', type=int)
a = p.parse_args()
if a.n < 0:
    p.error('N must be nonnegative')
for n in range(a.n, 0, -1):
    print(n)
