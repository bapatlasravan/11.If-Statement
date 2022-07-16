print("Exam Results")
marks=65
if marks>=35:
    print("You Passed! \n",'marks:',marks)
    if marks>=75 and marks<85:
        print("You promotted! \n",)
    elif marks>=85 and marks <95:
        print("You are good! \n",)
    elif marks>=95:
         print("You are excellent! \n",)
    else:
        print("you just passed! \n",)
else:
    print("YOU Failed!")
