
import os
import sys
import collections
import string

script_name = sys.argv[0]

res = {
    "Lines":"",
    "Characters":"",
    "Total-Words":"",
    "Unique-Words":"",
    "Repeated-Words":"",
    "Special-Characters":""
}

try:
    textfile = sys.argv[1]
    with open(textfile, "r") as f:

        line=0
        data = f.read()
        Lisst = data.split("\n") 
  
        for i in Lisst: 
            if i: 
                line += 1
        res["Lines"] = line 
        res["Characters"] = len(data.replace(" ","")) - res["Lines"]
        counter = collections.Counter(data.split())
        d = counter.most_common()
        res["Total-Words"] = sum([i[1] for i in d])
        res["Unique-Words"] = len([i[0] for i in d])
        res["Repeated-Words"] = sum([i[1] for i in d])-len([i[0] for i in d])
        special_chars = string.punctuation
        res["Special-Characters"] = sum(v for k, v in collections.Counter(data).items() if k in special_chars)

except IndexError:
    print('Usage: %s TEXTFILE' % script_name)
except IOError:
    print('"%s" cannot be opened.' % textfile)

print(res)

 
  
