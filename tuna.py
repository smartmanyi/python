import yangfile

def trankt(asd):

    a = yangfile.getfileeverylinetolist(asd)
    urllist = []
    for i in a:
        loc = i .find('ftp')
        ftp = i[loc:]
        print(ftp)
        urllist.append(ftp)
    return urllist


def createfile(asd):
    uu = trankt(asd)
    newfile = open('cleanFTP.txt', 'w')

    for item in uu:
        newfile.write("%s\n" % item)


createfile('./data1.txt')
