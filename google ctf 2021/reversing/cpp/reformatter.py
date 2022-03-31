import re

inputfile = open("cpp.c")
ifcount = 0
out = open("output.text", 'w')
for line in inputfile.readlines():
    if re.match(".*endif.*", line):
        ifcount -= 1
        out.write("\t"*ifcount + line)
    elif re.match(".*if.*", line):
        out.write("\t"*ifcount + line)
        ifcount += 1
    elif re.match(".*else.*", line):
        out.write("\t"*(ifcount-1) + line)
    else:
        out.write("\t"*ifcount + line)
