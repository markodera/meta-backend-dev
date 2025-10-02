try:
    with open("newfile.txt", "a") as file:
        file.writelines(["\nThis is a new file created!", "\nThis is another line to be added"])
except FileNotFoundError as e:
    print("ERROR", e)
except Exception as e:
    print("Something went wrong", e)