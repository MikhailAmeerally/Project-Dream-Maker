
file = open("MyLibs/LoveLetter3.txt", "r")

line = file.readline()
title = None
content = None
prompts = []


while(line):
    #print(line)

    if(line.strip() == "{Title}"):
        title = file.readline()
    elif(line.strip() == "{Content}"):
        content = ""
        while(line.strip() != ""):
            line = file.readline()
            content = content + line.strip() + "\n"
    elif(line.strip() == "{Prompts}"):
        line = file.readline().strip()
        while(line):
            prompts.append(line)
            line = file.readline().strip()
        break


    line = file.readline()

for i in range(0, len(prompts)):
    prompts[i] = input(prompts[i])

print(content.format(*prompts))

file.close()