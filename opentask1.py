import math
def list_ifname_ip():
    myfile = open('running-config.cfg')
    newdict=dict()

    for line in myfile:
        if "nameif" in line:
            mytemplist = line.split()

            next(myfile)
            templine = next(myfile)
            mylist= templine.split()

            if mytemplist[0]=='nameif':
                if mylist[0] == 'ip':
                    mytuple=(mylist[2:])
                    newdict[mytemplist[1]]=mytuple

    return (newdict)

ipconfigs = list_ifname_ip()
print(ipconfigs)
