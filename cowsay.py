import sys

a = sys.argv[1:]
a = " ".join(a)

cow = """           \   ^__^
            \  (oo)\\_______
               (__)\\       )\\/\\
                   ||----w |
                   ||     ||
"""

print('','_'*(len(a)+2))

print('< '+a+' >')

print('','"'*(len(a)+2))

print(cow)
