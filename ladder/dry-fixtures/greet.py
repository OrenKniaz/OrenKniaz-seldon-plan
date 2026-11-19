import argparse

p = argparse.ArgumentParser()
p.add_argument('name')
a = p.parse_args()
if not a.name:
    p.error('NAME must be nonempty')
print(f'Hello, {a.name}!')
