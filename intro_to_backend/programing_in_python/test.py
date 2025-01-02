import random
f_name = input("Type your file name: ")
f_content = open(f_name)
f_content = f_content.read()
f_content_list = f_content.split("\n")
# f_content.close()
print(random.choice(f_content_list))