lst1 = [1,"|" ,2 ,"|",3]
lst2 = [4,"|" ,5 ,"|",6]
lst3 = [7,"|" ,8 ,"|",9]

def  update_Board(input,play):
    if input<4:
        lst1[input-1] = play
    elif input<7:
        lst2[input-4] = play
    else:
        lst3[input-7] = play

def input_Board(play):

    while True:
        input=int(input("Enter a number between 1-9: "))
        if input in [1,2,3,4,5,6,7,8,9]:
            update_Board(input,play)
        else:
            print("Invalid input. Please enter a number between 1-9.")

def  display_Board():
    
    
    print(" ",lst1[0], lst1[1], lst1[2], lst1[3], lst1[4])
    print("-------------")
    print(" ",lst2[0], lst2[1], lst2[2], lst2[3], lst2[4])
    print("-------------")
    print(" ",lst3[0], lst3[1], lst3[2], lst3[3], lst3[4])

 

def main():
    
    print("Welcome to tic_tak_toe game")
    while True:
        
        start = ["x", "o"]
        play = input("Which player will start? (X or O) : ").lower()

        if play not in start:
            print("Invalid input choose from X or O")
            
        else:
            display_Board()
            input_Board(play)            

if __name__ == "__main__":
    main()