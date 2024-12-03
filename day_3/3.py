
def find_index(content, si, ei, ch):
    for i in range(si, ei):
        if content[i] == ch:
            return i
    return -1

# read the file content
file = open('input', 'r')
content = file.read()
file.close()

sum = 0
second_sum = 0
enabled = 1
for i in range(len(content) - 4):
    if content[i:i+7] == 'don\'t()':
        enabled = 0
    elif content[i:i+4] == 'do()':
        enabled = 1
    if content[i:i+4] == 'mul(':
        i += 4
        ind = find_index(content, i, i + 9, ')')
        if ind < 0: continue
        try:
            op = content[i:ind].split(',')
            print(op)
            sum += (int(op[0]) * int(op[1]))
            if enabled:
                second_sum += (int(op[0]) * int(op[1]))
        except:
            print('FALSE = ', op)
            continue

print(sum)
print(second_sum)

