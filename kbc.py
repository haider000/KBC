from questions import QUESTIONS
import sys


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    
    return True if question['answer']==answer else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    correctOption = ques['answer']
    optionToDelete1 = 0
    optionToDelete2 = 0
    
    if(correctOption==1):
        optionToDelete1 = "option3"
        optionToDelete2 = "option4"

    elif(correctOption==2):
        optionToDelete1 = "option3"
        optionToDelete2 = "option4"

    elif(correctOption==3):
        optionToDelete1 = "option1"
        optionToDelete2 = "option2"

    elif(correctOption==4):
        optionToDelete1 = "option1"
        optionToDelete2 = "option2"

    del ques[optionToDelete1]
    del ques[optionToDelete2]

    return ques


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

   
    prizeWon = 0
    roundNo = 0 
    lifeline = 1
    wrongAnswer = False
    print("Welcome to KBC...")
    print("Choose any Option Given Below:")
    print(" 1 : Start Game")
    print(" 2 : Quit  Game")

    userChoice = int(input().strip())

    if(userChoice==2):
        sys.exit(0)
    
    while(roundNo<=14):
        
        print("\n\t\tLifeline Remains:   {}\n".format(lifeline))
        

        print(f'\t\tQuestion {roundNo+1}: {QUESTIONS[roundNo]["name"]}' )
        print(f'\n\t\t\tOptions:')
        print(f'\t\t\t\tOption 1: {QUESTIONS[roundNo]["option1"]}')
        print(f'\t\t\t\tOption 2: {QUESTIONS[roundNo]["option2"]}')
        print(f'\t\t\t\tOption 3: {QUESTIONS[roundNo]["option3"]}')
        print(f'\t\t\t\tOption 4: {QUESTIONS[roundNo]["option4"]}')
        
        ans = input('\n\nYour choice ( 1-4 ) or Enter lifeline to use lifeline or Enter quit to Quit the game: ')
        
        if ans.lower() == "quit":
            break
        elif(ans.lower=="lifeline" and roundNo==14):
            print("You Can't Use Lifeline on Last Question")
            ans = input('\n\nYour choice ( 1-4 ) or Enter quit to Quit the game: ')
        elif(ans.lower() == "lifeline" and lifeline==0):
            print("You Did not have any Lifeline")
            ans = input('\n\nYour choice ( 1-4 ) or Enter quit to Quit the game: ')

        elif(ans.lower() == "lifeline" and lifeline==1):
            q = lifeLine(QUESTIONS[roundNo])
            print(f'\tQuestion {roundNo+1}: {q["name"]}' )
            print(f'\t\tOptions:')
            
            if(["answer"] == 1 or q["answer"] == 2):
                print(f'\t\t\tOption 1: {q["option1"]}')
                print(f'\t\t\tOption 2: {q["option2"]}')

            elif(q["answer"] == 3 or q["answer"] == 4):
                print(f'\t\t\tOption 1: {q["option3"]}')
                print(f'\t\t\tOption 2: {q["option4"]}')

            lifeline-=1

            ans = input('Your choice ( 1 or 2 ) ')
        
        elif(ans not in ["1","2","3","4"]):
            print("Please Choose a correct option")
            ans = input('Your choice ( 1-4 ) : ')

            


        if isAnswerCorrect(QUESTIONS[roundNo], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\n \t\t\tCorrect ANswer !')
            prizeWon = QUESTIONS[roundNo]["money"]
            print("\t\t\tMoney Won Till Now: {}".format(prizeWon))

        else:
            # end the game now.
            # also print the correct answer
            print('\n\nIncorrect !')
            print("THe Right Answer Was {}".format(QUESTIONS[roundNo]["answer"]))
            wrongAnswer = True;
            break;
        
        roundNo+=1
    # print the total money won in the end.
    
    
    if(not wrongAnswer):
        print("You Won Total: {} Rs".format(prizeWon))

    else:
        if(roundNo+1<5):
            print("You Won : {}".format("0 Rs"))
        elif(roundNo+1>=5 and roundNo+1<11):
            print("You Won : {}".format("10,000 Rs"))
        elif(roundNo+1>=11):
            print("You Won : {}".format("3,20,000 Rs"))





kbc()
