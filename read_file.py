try:
    with open('SampleTxt.txt') as fin:
        lines=[]
        for line in fin:
            #print(line)
            lines.append(line)
except FileNotFoundError as e:
    lines=""

print(lines)