from pyparsing import line
import pyttsx3, random, linecache, time

pyobj = pyttsx3.init()
with open('quotes.txt','r', encoding= 'UTF-8') as file:
    for line_number, line in enumerate(file):
        pass
    line_chosen = random.randint(1, line_number + 1)
line = linecache.getline(r"quotes.txt", line_chosen)
line = "\"" + line + "\"" + " - Andrew Tate"
print(line)


pyobj.say(line, "slow")
pyobj.runAndWait()
