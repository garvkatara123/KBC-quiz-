def kbc_quiz():
    name=input("please enter your name:- ")
    st=input("Are you ready for the KBC quiz.\npress(y) for yes and(n) for no:- ")
    questions=[
      #1
      ["who develop python programming language.","1:- wick van rossum","2:- ramkali",
      "3:- guido van rossum","4:-none",3],
      #2
      ["which extenshion is used in python.","1:- .py","2:-.c++","3:-.pyhton","4:-.htm",1],
      #3
      ["which of the following is a valid python comment?","1:- $","2:- #","3:- &","4:-!",2],
      #4
      ["which of these data types does python not natively support.","1:- List","2:- Tuples","3:- Dictionary","4:- Arrays",4],
      #5
      ["which of the following is the mutable data type in pyhton?","1:- String","2:- List",      "3:- Tuples","4:- Integer",2],
      #6
      ["which datatype would you use to store whole number in python.",
      "1:- float","2:- int","3:- str","4:- bool",2],
      #7
      ["variable\nx='python'\ncheck if x is string\nif yes\nprint'string'\notherwise\nprint'not a string'.","1:- String","2:- Not a string",
      "3:- Error","4:- none",1],
      #8
      ["x=(1,2,3)\nx[1]=4\nprint(x).",
      "1:- Tuples are immutable","2:- x[1] should be x[2]","3:- syntax error","4:- no error",1],
      #9
      ["what is the purpose of the end parameter in the print() function.","1:- To add a space at the end","2:- To end the script","3:- To specify the string appended after the last value","4:- To break the line",3 ],
      #10
      ["which is the valid identifier","1:- name-123","2:- 123name","3:- name 123","4:- _name123",4],
      #11
      ["what is the output of the following code.\nprint(2**3+(5+6)**(1+1)).","1:- 127","2:- 129","3:- 128","4:- 221",2],
      #12
      ["how is a code block indicated in python.","1:- brackets","2:- indentation","3:- curly brackets and semi colon","4:- none of the above",2],
      #13
      ["what will be the output of the following code.\na=[5, 4, 9]\na=tuple(a)\na[0]=2\nprint(a).","1:- [2, 4, 9]","2:- (2, 4, 9)","3:- [5, 4, 9]","4:- error",4 ],
      #14
      ["what will be the output of the following code.\na=3\nb=1\nprint(a,b)\na, b = b, a\nprint(a,b).","1:- 3 1  1 3 ","2:- 3 1  3 1","3:- 1 3  1 3","4:- 1 3  3 1",1],
      #15
      ["which of the following types of loops are not supported in python?.","1:- for ","2:- while","3:- do-while","4:- none of the above",3],
      #16
      ["which of the following is the proper syntax to check if a particular element is present in a list?.","1:- if ele in list","2:- if not ele not in list","3:- none of the above","4:- both a and b",4],
      #17
      ["What will be the output of the following code snippet?\n def thrive(n):\n\t if n % 15 == 0:\n\t print(""thrive"", end = “ ”)\n\b elif (n % 3 != 0 and n % 5 != 0):\n\t print(""neither"", end = “ ”)\n\b elif n % 3 == 0:\n\t print(""three"", end = “ ”)\n\b elif n % 5 == 0:\n\t print(""five"", end = “ ”)\n\bthrive(35)\n\bthrive(56)\n\bthrive(15)\n\bthrive(39)","1:- five neither thrive three","2:- thrive five neither three","3:- five thrive neither three","4:- five thrive three neither",1],
      ]
    levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,"1 crore","7 crore"]
    money=0
    if(st=="y" or st=="Y"):
        print("Hello!",name)
        print("Welcome to the quiz.\nNow")
        for i in range(0,len(questions)):
            question=questions[i]
            print(f"Question for Rs.{levels[i]}")
            print(f"{i+1}. question is:- \n\n{question[0]}")
            print(f"{questions[i][1]}     {questions[i][2]}")
            print(f"{questions[i][3]}     {questions[i][4]}")
            reply=int(input("enter your answer(1-4) "))
            if (reply==question[-1]):
                print(f"correct answer,you have won Rs.{levels[i]}\n")
                if (i==4):
                    money=10000
                elif(i==9):
                    money=320000
                elif (i>9 and i<18):
                    money=levels[i]
                    if money=="1 crore":
                        print("Wow Nice",'"',name,'"',"You played well")
                        print("you won 1 crore rupees")
                        print("Just give one more right answer and get 7 crore rupees in your account")
                    elif(money=="7 crore"):
                        print("Wow Nice",'"',name,'"',"You played well")
                        print("you won 7 crore rupees") 
            else:
                print("wrong answer!")
                if(money==0):
                    print("Sorry !",'"',name,'"',"\nyou won Rs.",money)
                else:
                    print("Congratulations!",'"',name,'"',"\nyou won Rs.",money)
                break
    elif(st=="n" or st=="N"):
        print("Thankyou ",name,"!")
        print("Now you are exit from the KBC quiz.")
    else:
        print('"',name,'"',"you entered invalid choice.")
kbc_quiz()





























































































































































    

