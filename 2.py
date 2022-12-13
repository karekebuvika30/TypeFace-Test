from sys import stdin, stdout
string = stdin.readline().strip().lower()
similarSound = {'c' : ['s', 'k'], 'x': ['ks', 'cs', 'z'], 's' : ['z'], 'q' : ['kw'], 'u': ['oo'], 'y':['i']}
ans = []
for ch in string:
    if ch in similarSound:
        for val in similarSound[ch]:
            ans.append(string.replace(ch, val))
print(ans)