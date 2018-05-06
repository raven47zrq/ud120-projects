
def Search(data,keyword,typ=None):
    for name in data.keys():
        if keyword.upper() in name:
            print name
            if typ==None:
                print data[name]
            else:
                print data[name][typ]
