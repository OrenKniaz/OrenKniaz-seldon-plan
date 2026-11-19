import argparse

p = argparse.ArgumentParser()
p.add_argument('a', type=int)
p.add_argument('b', type=int)
a = p.parse_args()
print(a.a + a.b)
