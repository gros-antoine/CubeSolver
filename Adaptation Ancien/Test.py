import ast

f = open('BH.txt', 'r')

t = ""

for l in f.readlines():
    t += l.replace('\n', '')

Dict = ast.literal_eval(t)
print(Dict)
