
guess_number = 2
i=0

while i<10:
    a=int(input("Type your Guess: "))
    i+=1
    if(a==guess_number):
        print("""
        
        You guessed it right!
        
        """)
        break;
    else:
        print("""
        
        Try Again!
        
        """)


    


