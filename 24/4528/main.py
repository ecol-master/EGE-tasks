filetext = open("text.txt", 'r', encoding="utf-8").read()
file_objcts = filetext.split(".")
file_objcts2 = [len(i) for i in file_objcts]
max_length = 5
for i in range(len(file_objcts2)):
    length = sum([j for j in file_objcts2[i:i+6]])
    if length > max_length:
        max_length = length

print(max_length)