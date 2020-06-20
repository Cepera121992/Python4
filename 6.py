from itertools import count, cycle

for i in count(3, 1):
    if i == 11:
        break

    print(i)

my_list = ['Hi', 'How are you doing?', ';)']
c = 0
for i in cycle(my_list):
    c += 1
    if c > 9:
        break
    print(i)
