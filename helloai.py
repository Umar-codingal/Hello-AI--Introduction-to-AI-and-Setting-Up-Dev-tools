name=input("Hello User, please enter your name: ")

print("Hello,", name, "!")

mood=input("How are you feeling today? (happy/sad): ")
mood=mood.lower()

if mood=="happy":
    print("That's great to hear! Keep smiling :)")
elif mood=="sad":
    import tkinter as tk
    from tkinter import PhotoImage

    root = tk.Tk()
    root.title("GIF Example")

# Load the GIF
    gif = PhotoImage(file="crying.gif")

# Create a label to display the GIF
    label = tk.Label(root, image=gif)
    label.pack()

# Run the main event loop
    root.mainloop()

    print(f"Sorry to hear that. I hope your day gets better!")
else:

    root = tk.Tk()
    root.title("GIF Example")

# Load the GIF
    gif = PhotoImage(file="man.gif")

# Create a label to display the GIF
    label = tk.Label(root, image=gif)
    label.pack()

# Run the main event loop
    root.mainloop()
    print("I don't understand that mood. But I hope you have a great day!")

