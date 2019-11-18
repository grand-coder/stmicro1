from urllib.request import urlopen, urlretrieve
import json
import os
for m in range(3):
    url = "https://www.google.com/doodles/json/2019/" + str(m+1) + "?hl=zh_TW"
    response = urlopen(url)
    pics = json.load(response)
    for p in pics:
        purl = "https:" + p["url"]
        print(p["title"])
        print(purl)

        dn = "pic/" + str(m+1)
        if not os.path.exists(dn):
            os.makedirs(dn)
        fn = dn + "/" + purl.split("/")[-1]
        urlretrieve(purl, fn)