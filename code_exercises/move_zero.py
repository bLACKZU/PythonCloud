old_list = [0,2,6,6,0,2,9]
i = 0
j = len(old_list) - 1

while i < j:
    if old_list[j] == 0:
        j -= 1
        continue
    if old_list[i] == 0:
        old_list[i], old_list[j] = old_list[j], old_list[i]
        i += 1
        j -= 1
    else:
        i += 1 

print(old_list)


# limit = 7
# offset = 6
# old_list[0] = 9
# old_list[6] = 0
# i = 0
# limit = 7
# offset = 6
# old_list[0] = old_list[0 + 6]
# old_list[7 - 1] = old_list[0]

# [9,2,6,6,0,2,0]