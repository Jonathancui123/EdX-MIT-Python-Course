data = []
filename = input("Enter a file name")

try:
    fh = open(filename, 'r')
except IOError:
    print('cannot open', filename)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
    print(data)
    fh.close()

if data != []:
    OrganizedData = []
    for student in data:
        try:
            name = student[:-1]
            grade = int(student[-1])
            OrganizedData.append([name, [grade]])
        except ValueError:
            OrganizedData.append([student[:], []])

    print(OrganizedData)
