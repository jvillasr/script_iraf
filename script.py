filename='ejsalidairaf.dat'
c1='('
c2=')'
c3=''
filer=open(filename, 'r')
filew=open(filename+'.mod', 'w')
old=filer.read()
new=old.replace(c1, c3)
new2=new.replace(c2,c3)
filew.write(new2)
filer.close()
filew.close()

