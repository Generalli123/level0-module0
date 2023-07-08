from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer1 = simpledialog.askinteger(title='Question 1', prompt="What is 1+1?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 2:
    #      // 4.  if the user's answer was correct, add one to their score 
        score += 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer1 = simpledialog.askinteger(title='Question 2', prompt="What is 2+2?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 4:
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        answer1 = simpledialog.askinteger(title='Question 3', prompt="What is 4+4?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 8:
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        answer1 = simpledialog.askinteger(title='Question 4', prompt="What is 8+8?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 16:
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        answer1 = simpledialog.askinteger(title='Question 5', prompt="What is 16+16?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 32:
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        answer1 = simpledialog.askinteger(title='Question 6', prompt="What is 32+32?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == 64:
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    # After all the questions have been asked, tell the user their final score

    messagebox.showinfo(title='Final score', message="Your final score is, " + str(score) + "/6")
    # remember to convert your variable to a string using the str() function 

    # Run the window's .mainloop() method
    window.mainloop()
