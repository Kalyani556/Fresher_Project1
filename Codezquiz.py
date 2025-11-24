print("Hello student! Welcome to Codezquiz")
name=input("Please enter your name")
print("Great",name,"let's start the quiz!")
ans=input("Are u ready?")
score=0
if ans.lower()=="yes":
               print("3...2...1....LET'S GO!")
               # quiz starts
               print("Question 1")
               ans1=input("What is the correct extension for Python files?")
               if ans1.lower()==".py":
                   print("That's great! Correct answer!")
                   score+=1
               else:
                   print("Wrong answer")
               print("Question 2")
               ans2=input("Which of the following is a valid variable name?\nA. 2name\nB. name_2\nC. name-2\nD. name 2 \nEnter your option")
               if ans2.lower()=="b":
                   print("Correct!")
                   score+=1
               else:
                   print("Incorrect")
               print("Question 3")
               ans3=input("which operator is used for exponentiation in python")
               if ans3.lower()=="**":
                   print("Excellent! Correct Answer")
                   score+=1
               else:
                   print("Incorrect!")
               print("Question 4 ")
               ans4=input("Which keyword is used to define a function?")
               if ans4.lower()=="def":
                   print("Correct one!")
                   score+=1
               else:
                   print("Incorrect!")
               print("Question 5")
               ans5=input("What will be the output of the following?:\nprint(bool(0))\nA. True\nB. False\nC. Error\nD. 0\nSelect an option")
               if ans5.lower()=="b":
                   print("Very good! Correct answer")
                   score+=1
               else:
                   print("Incorrect!")
               a=input("Quiz Ended!Did you enjoy? yes/no")
               if a.lower()=="yes":
                   print("Nice to hear that, let's see your score!")
               else:
                   print("No worries, all the best next time")
               print("Now, let's see your score!")
               print("Your score is", score)
               if score>=4:
                   print("Excellent, did a great job!")
               elif score==3:
                   print("Good, you can do better!")
               else:
                   print("Tried well! Don't loose confidence, study well and all the best next time")
               print("Thank you", name, "Study well!")
else:
    print("TRY AGAIN.....")
                   
            
     
              
            
            
                   
           

