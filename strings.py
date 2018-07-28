strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(len(strings)):
    sentence=sentence+strings[i]+" "
    i=+1
print(sentence)
print(' '.join(strings))