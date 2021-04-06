import re


def replacer(path):
    data = []
    with open(path, "r") as f:
        for line in f.readlines():
            x = re.findall("!\[\]\(/img.*\.png\)",line)
            if(len(x) > 0):
                #![]({{'/img/HBCU/Clipboard_2020-11-16-15-04-44.png' | prepend: site.baseurl}})
                fixed_img = "![]({{'"+x[0][4:-1]+"' | prepend: site.baseurl}})"

                outline = line.replace(x[0], fixed_img)
                data.append(outline)
                print("Replaced line: "+ outline)
            else:
                data.append(line)
    with open(path, "w") as f:
        for line in data:
            f.write(line)

import sys

if(len(sys.argv) != 2):
    print("enter the path to the file pls")
    exit(0)
replacer(sys.argv[1])
# replacer("/home/daroot/test-encrypted-ghpages/_pages/HBCU/HBCU-BE01.markdown")
