fname=input('Enter File Name:')
file=open(fname)
for line in file:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    print(line)
    space=line.find(':')
    print(space)
