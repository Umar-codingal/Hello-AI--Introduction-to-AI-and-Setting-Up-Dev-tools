import tkinter as tk
from tkinter import PhotoImage

def chatbot():
    print("Hello, User! Let's chat!")

    while True:
        name = input("Please enter your name: ")
        print("Hello,", name, "!")

        mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

        if mood == "happy":
            print("That's great to hear! Keep smiling :)")
            
        elif mood == "sad":
            print(f"Sorry to hear that. I hope your day gets better!")
            display_gif("crying.gif")
        elif mood == "neutral":
            print("That's okay! I hope something exciting happens today!")
           
        else:
            print("I don't quite understand that mood, but I hope you have a great day!")
            display_gif("man.gif")

        repeat = input("Do you want to chat more? (yes/no): ").lower()
        if repeat == "no":
            print("Goodbye! Take care!")
            break
        elif repeat != "yes":
            print("I didn't quite get that. Let's chat again.")
            continue

def display_gif(gif_name):
    root = tk.Tk()
    root.title("Emotion GIF")

    # Load the GIF
    gif = PhotoImage(file=gif_name)

    # Create a label to display the GIF
    label = tk.Label(root, image=gif)
    label.pack()

    # Run the main event loop
    root.mainloop()

# Run the chatbot function
chatbot()
