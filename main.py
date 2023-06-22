# for i in range(0, 10):
#     print(i, end=', ') if i % 2 == 1 else None

# print(', '.join([str(x) if x % 2 == 1 else m for x in range(10)]))
odd = list(filter(lambda x: x % 2 == 1, range(10)))

print(','.join(map(str, odd)))


