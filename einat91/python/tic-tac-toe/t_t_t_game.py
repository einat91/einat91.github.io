
#This code is for tic-tac-toe game!
#Here you can see an empty list for the game:
list_t_t_t = ["","","",
               "","","",
               "","",""] # fix the look of this list, maybe a table!
#list_t_t_t.insert(2, 3)
print(list_t_t_t)
#Here 2 fun for users name for the introduction:
user_1_name = input("Welcome to tic-tac-toe game! before we start what is your name?")
print("Hello " + user_1_name + ", you are X")
#intro_user_1()

def user_1_win():
    if (
        (list_t_t_t[0] == 'X' and list_t_t_t[1] == 'X' and list_t_t_t[2] == 'X') or (list_t_t_t[3] == 'X' and list_t_t_t[4] == 'X' and list_t_t_t[5] == 'X') or
        (list_t_t_t[6] == 'X' and list_t_t_t[7] == 'X' and list_t_t_t[8] == 'X') or (list_t_t_t[0] == 'X' and list_t_t_t[3] == 'X' and list_t_t_t[6] == 'X') or
        (list_t_t_t[1] == 'X' and list_t_t_t[4] == 'X' and list_t_t_t[7] == 'X') or (list_t_t_t[2] == 'X' and list_t_t_t[5] == 'X' and list_t_t_t[8] == 'X') or
        (list_t_t_t[0] == 'X' and list_t_t_t[4] == 'X' and list_t_t_t[8] == 'X') or (list_t_t_t[2] == 'X' and list_t_t_t[4] == 'X' and list_t_t_t[6] == 'X')
        ):
        return False
#User_2 options to win:
def user_2_win():
    if (
        (list_t_t_t[0] == 'O' and list_t_t_t[1] == 'O' and list_t_t_t[2] == 'O') or (list_t_t_t[3] == 'O' and list_t_t_t[4] == 'O' and list_t_t_t[5] == 'O') or
        (list_t_t_t[6] == 'O' and list_t_t_t[7] == 'O' and list_t_t_t[8] == 'O') or (list_t_t_t[0] == 'O' and list_t_t_t[3] == 'O' and list_t_t_t[6] == 'O')or
        (list_t_t_t[1] == 'O' and list_t_t_t[4] == 'O' and list_t_t_t[7] == 'O') or (list_t_t_t[2] == 'O' and list_t_t_t[5] == 'O' and list_t_t_t[8] == 'O') or
        (list_t_t_t[0] == 'O' and list_t_t_t[4] == 'O' and list_t_t_t[8] == 'O') or(list_t_t_t[2] == 'O' and list_t_t_t[4] == 'O' and list_t_t_t[6] == 'O')
        ):
        print(user_2_name + " you won!")
        return False
def user_1_turn():
    n1 = int(input(user_1_name + " choose an index"))
    return n1

user_2_name = input("Welcome to tic-tac-toe game! before we start what is your name?")
print("Hello " + user_2_name + ", you are O")
#intro_user_2()
def user_2_turn():
    n2 = int(input(user_2_name + " choose an index"))
    return n2

def user_1_choice(c):
    if list_t_t_t[c] == 'X' or list_t_t_t[c] == 'O':
        print("Try again")
        return user_1_turn()
def user_2_choice(c):
    if list_t_t_t[c] == 'X' or list_t_t_t[c] == 'O':
        print("Try again")
        return user_2_turn()

#User_1 options to win:
def t_t_t_game():
    n = 1
    while True:
        if n % 2 == 1:
            n1 = int(input(user_1_name + " choose an index"))
            if list_t_t_t[n1] == 'X' or list_t_t_t[n1] == 'O':
                print("Try again")
                n+=0
            else:
                list_t_t_t[n1] = 'X'
                print(list_t_t_t)
                n+=1
            user_1_win()
            
        if n % 2 == 0:
            n2 = int(input(user_2_name + " choose an index"))
            if list_t_t_t[n2] == 'X' or list_t_t_t[n2] == 'O':
                print("Try again")
                n+=0
            else:
                list_t_t_t[n2] = 'O'
                print(list_t_t_t)
                n+=1
            user_2_win()
           
        
t_t_t_game()

