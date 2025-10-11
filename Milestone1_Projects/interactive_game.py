mylist : list = ['0','1','2']
def display_list()->None:

    print(f"The Current list is : {mylist}")


def input_list():
    state = True
    index = " "
    Value=None
    while state:
       
        index = input("Update value of list at which index (0-2) : ")
        if index.isdigit() == False:
            print("Enter a Valid number")
        elif  index.isdigit() and int(index) not in range(0,3):
            print("Enter within range of (0-2) ")  
        else:
            Value = input("Enter value to enter : ")
            state=False
    return index,Value
    

def update_list(Value,index):
    mylist[int(index)] = Value

    

if __name__ =="__main__":

    print("Simple interactive list update")
    flag = True
    while flag:
        display_list()
        index,val = input_list()
        update_list(val,index)
        display_list()
        conti = input("Do u wish to continue ? (Y/N)")

        if conti.lower() == 'n':
            break
    




        
        

