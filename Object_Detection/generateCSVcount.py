import sys
import time

try:
    with open(sys.argv[1], "r") as xmls:
        with open("totals.csv", "w") as totals:
            print("opened files successfully...")

            totals.write("fileName,Motorized,Non Motorized,Vehicle,Mechanical,Dog,Hybrid\n")
            counts = []
            totalCounts = []

            xmls.readline()
            data = xmls.readlines()
            for line in data:
                line = line.split(",")
                counts.append([line[0],0,0,0,0,0,0])
                if line[3] == "motorized":
                    counts[-1][1] += 1
                elif line[3] == "nonMotorized":
                    counts[-1][2] += 1
                elif line[3] == "vehicle":
                    counts[-1][3] += 1
                elif line[3] == "mechanical":
                    counts[-1][4] += 1
                elif line[3] == "dog":
                    counts[-1][5] += 1
                elif line[3] == "hybrid":
                    counts[-1][6] += 1

            #for x in counts:
            #    print(x)

            i = 0
            limiter = len(counts)

            while i < limiter:
                additional = 1
                while i+additional < limiter:
                    if counts[i][0] != counts[i+additional][0]:
                        break
                    else:
                        additional += 1

                temp = [counts[i][0],0,0,0,0,0,0]
                for k in range(additional):
                    for j in range(1,7):
                        temp[j] += counts[i+k][j]

                totalCounts.append(temp)
                
                i = i + additional

            for entry in totalCounts:
                print(entry)

            for entry in totalCounts:
                enter = entry[0]+","+str(entry[1])+","+str(entry[2])+","+str(entry[3])+","+str(entry[4])+","+str(entry[5])+","+str(entry[6])+"\n"
                totals.write(enter)
                
except:
    print("That didnt work try again or something")

