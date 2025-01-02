name = open("newfile.txt", "a")
# names = name.write("\n")
namess = name.writelines(["This is a new file created!", "\nThis is another line to be added"])
name = namess
# name = names