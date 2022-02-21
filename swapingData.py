def swapData():
    File1=input ("Enter the File Name.")
    File2=input ("Enter the File Name.")

    f1=open(File1,'r')
    data_a=f1.read()

    f2=open(File2,'r')
    data_b=f2.read()


    f1=open(File1,'w')
    f1.write(data_b)

    f2=open(File2,'w')
    f2.write(data_a)

swapData()
