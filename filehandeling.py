import os
print("####################################################")
print("#               FILE HANDELING                     #")
print("####################################################")
def ins():
    print("1. create new file")
    print("2. write text in file")
    print("3. list the files")
    print("4. delet the file")
    print("5. rename the file")
    print("6. stop the program")
ins()
c=int(input('enter ur choice: '))
def create_file():
    name=input('enter the file name: ')
    with open(name+".txt","w")as file:
        file.write("welcome")
    print(name+",.txt", "created successfully..")
def create_file():
    name=input('enter the file name to write: ')
    text=input('type the content: ')
    with open(name+".txt","w")as file:
        file.write("text")
    print(name,"reated successfully..")
while(True):
  ins()
  match c:
    case 1:
        print("creating file")
        create_file()
    case 2:
        print("edit")
        write_file()
    case 3:
        print("list file")
        files_list=os.listdir(".")
        print(files_list)
    case 4:
        print("delet file")
        n=input("type the file name to delet: ")
        os.remove(n)
        print("deleted successfully")
    case 5:
        print("rename")
    case 6:
        print("stop the program")
def create_file():
    name=input('enter the file name: ')
    with open(name+".txt","w")as file:
        file.write("welcome")
    print(name+",.txt", "created successfully..")