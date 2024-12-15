with open("sample.txt", "r") as f:
    dump = f.readlines()

dump_list = []
for char in dump:
    x = char.strip('\n')
    dump_list.append(x)

for i in range(len(dump) - 1, 11, -1):
    print(dump_list[i - 1])

