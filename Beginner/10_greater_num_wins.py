 

def game():
    try:
        pl1 = int(input("Player1 : Enter a num between 0 and 100 (0 not included)."))
        pl2 = int(input("Player2 : Enter a num between 0 and 100 (0 not included)."))
    except ValueError:
        print("Enter a number, other data types not permitted.")
        game()
    if (pl1<1) | (pl1>100) | (pl2<1) | (pl2>100) :
        print("Number out of range.  Try again.")
        game()
    else:    
        if pl1>pl2:
            print("Player 1 wins.")
        elif pl2>pl1:
            print("Player 2 wins.")
        else:
            print("They are equal.")                

game()              