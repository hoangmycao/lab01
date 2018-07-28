strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(len(strings)):
    if (i<(len(strings))-1):
        sentence=sentence+strings[i]+" "
    else:
        sentence=sentence+strings[i]
    i=+1
print(sentence)
print(' '.join(strings))