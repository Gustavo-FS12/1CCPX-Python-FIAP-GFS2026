eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
}

print(eng2sp)

print('one' in eng2sp)
print('uno' in eng2sp)

print(eng2sp['two'])

vals = eng2sp.values()
print('uno' in vals)
print('one' in vals)