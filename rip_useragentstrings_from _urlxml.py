# normal pycode to rip url from url from xml format file and to store it in external file
# $python rip_useragentstrings_from _urlxml.py > useragentstring.py

with open('url.xml') as f:
    for line in f:
        if line.startswith("#"):
            continue
        print "'" + line.split('"')[3] + "',"
