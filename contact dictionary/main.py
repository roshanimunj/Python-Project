'''
#main file
fp=open("data1.txt","w")
print(fp)
print(type(fp))
d="File handling"
fp.write(d)

fp=open("data1.txt","a")
d="Hello all"
fp.write(d)

fp.close()

'''
#contact directory project
def SearchByMobile():
 smob=input("Enter the mobile number to be saerched:")
 fp=open("data.txt","r")
 data=fp.readlines()#it will return list
 #print(data)
 for x in data:
    r=x.split(':')
    if smob+'\n'==r[1]:
       print("Mobile number found",x)
       fp.close()

      # break
     #else:
        # print("Not found!!!")
         
         

def delete_record():
    emob=input("Enter the mobile number to be deleted")
    fp=open("data.txt","r")
    data =fp.readlines()
    for x in data:#accessing the data
        rec=x.split(':')#it will split the list
        if emob+'\n'==rec[1]:#it will check
            data.remove(x)#it will remove the record which the user has entered
            fp1=open("data.txt","w")#opening the file in write mode
            newdata=''.join(data)#converting the data from list to string
            fp1.write(newdata)#overriding the data
            fp1.close()
            print("Contact successfully deleted")
            break
     
    
def SearchByName():
     sname=input("Enter the name to be searched:")
     fp=open("data.txt","r")
     data=fp.readlines()#it will return list
     #print(data)
     for x in data:
         r=x.split(':')
         if sname==r[0]:
           print("Name found",x)
           fp.close()

def update_record():
    mob=input("Enter mobile number to update record:")
    fp=open("data.txt","r")
    data =fp.readlines()
    for x in data:#accessing the data
        rec=x.split(':')#it will split the list
        if mob+'\n'==rec[1]:
            print("1.update mobile no.:")
            print("2.update Name:")
            ch=input("Enter your choice:")
            if ch=='1':
                nmob=input("Enter new mobile no.:")
                rec[1]=nmob+'\n'
                data.remove(x)
                temp=':'.join(rec)
                data.append(temp)
                fdata=''.join(data)
                fp1=open("data.txt","w")
                fp1.write(fdata)
                fp1.close()
                print("Record updated successfully!!!")
                
            elif ch=='2':
                print("update name")
            else:
                print("please enter valid choice")
            break
    else:
            print("No record found")
    
while True:
    print()
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search by mobile number")
    print("6.Search by name")
    print("7.Exit")
    ch=input("Enter your choice:")

    if ch=='1':
        fp=open("data.txt","a")
        n=input("Enter your name:")
        mob=input("Enter mobile number:")
        c=n+":"+mob+"\n" 
        fp.write(c)
        fp.close()
        
    elif ch=='2':
         fp=open("data.txt","r")
         cdata=fp.read()
         print("CONTACT DIRECTORY")
         print("===========================")
         print(cdata)
         fp.close()
         
    elif ch=='3':
         update_record()
    elif ch=='4':
        delete_record()
    elif ch=='5':
         SearchByMobile()
    elif ch=='6':
         SearchByName()
    elif ch=='7':
         print("Thanks for using the application!!!")
         break
    else:
         print("Please enter a valid choice!!!")
         

