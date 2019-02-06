def new_config_file(fout,fin):
    fout.seek(0)
    for line in fout:
        if 'ip address' in line and '.' in line:
            line=line.strip()
            line=line.split()
            iptemp=line[2]
            masktemp=line[3]
            iptemp=iptemp.split('.')
            masktemp=masktemp.split('.')
            if iptemp[0] =='192' or iptemp[0] =='172':
                iptemp[0]='10'

            if (masktemp[0]=='255' and masktemp[1]=='255') or masktemp[2]=='255':
                masktemp[1]=masktemp[2]='0'

            iptemp=' ip address '+'.'.join(iptemp)+' '+'.'.join(masktemp)+'\n'
            
            fin.write(iptemp)

        else:
            fin.write(line)
    return True
fout=open('running-config.cfg','r')
fin=open('new-running-config.cfg','a+')
if new_config_file(fout,fin):
	print('New File Created Successfully')
else:
        print('Not Able to Create New File File')

   

