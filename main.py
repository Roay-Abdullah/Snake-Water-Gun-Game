import random
import tkinter as tk

choices = {"Snake": 1, "Water": -1, "Gun": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

userScore = 0
compScore = 0

def play(userChoice):
    global userScore, compScore

    compChoice = random.choice([1, -1, 0])

    result = ""
    if (userChoice == compChoice):
        result = "It's a Tie!"
    elif (compChoice == -1 and userChoice == 1) or (compChoice == 1 and userChoice == 0) or (compChoice == 0 and userChoice == -1):
        result = "You Win!"
        userScore += 1
    else:
        result = "Computer Wins!"
        compScore += 1

    resultLabel.config(text=f"You: {reverse[userChoice]} | Computer: {reverse[compChoice]}\n{result}")
    scoreLabel.config(text=f"Score → You: {userScore} | Computer: {compScore}")


# GUI window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("800x400")

tk.Label(root, text="Snake Water Gun", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Snake", width=10, command=lambda: play(1)).pack(pady=5)
tk.Button(root, text="Water", width=10, command=lambda: play(-1)).pack(pady=5)
tk.Button(root, text="Gun", width=10, command=lambda: play(0)).pack(pady=5)

resultLabel = tk.Label(root, text="", font=("Arial", 12))
resultLabel.pack(pady=10)

scoreLabel = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
scoreLabel.pack()

root.mainloop()
