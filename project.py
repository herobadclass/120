def read_student_data(infile):
    fileR = open(infile,"r")
    localList = []
    for line in fileR:
        row = [line[0:line.find(' ')], line[line.rfind(' ') + 1:len(line) - 1]]
        localList.append(row)
    fileR.close()
    print(len(localList))
    return localList
def read_key_pts(infile):
    fileR = open(infile,"r")
    localList = []
    for line in fileR:
        string = line[0:len(line) - 1]
        localList.append(string)
    fileR.close()
    localList[1] = localList[1].split(' ')
    return localList
def totalPts(key):
    total = 0
    for i in range(len(key[1])):
        total = total + float(key[1][i])
    return total
def markingAll(data,key,total):
    localList = []
    for student in range(len(data)):
        marks = 0
        for question in range(len(key[0])):
            if(data[student][1][question] == key[0][question]):
                marks = marks + float(key[1][question])
        string = str(data[student][0]) + "\t" + str(marks) + "\t" + str(marks / total * 100) + "%"
        localList.append(string)
    return localList
def markingSel(data,key,total):
    name = ""
    localList = []
    while(name != "end"):
        switch = False 
        name = input("Type the name of a student or 'end' to finish. ")
        for i in range(len(data)):
            if(name == data[i][0]):
                marks = 0
                for question in range(len(key[0])):
                    if(data[i][1][question] == key[0][question]):
                        marks = marks + float(key[1][question])
                string = str(data[i][0]) + "\t" + str(marks) + "\t" + str(marks / total * 100) + "%"
                localList.append(string)
                switch = True
        if(switch == False):
            print("This is not a valid input.")
    return localList
data = read_student_data('IN_data_studs.txt')
key = read_key_pts('IN_key+pts.txt')
total = totalPts(key)
print(markingSel(data,key,total))
