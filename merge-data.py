import sys
def clean_data(inputfile):
    f1 = open(inputfile, "r")
    content = f1.readlines()
    f1.close()

    outputfile = inputfile.split(".")[0] + ".csv"

    first_line = True
    f1 = open(outputfile, "w")
    for line in content:
        if first_line == True:
            line = line.split(";")
            cleanLine = ";".join(line[0:8])
            cleanLine = cleanLine + "\n"
            f1.write(cleanLine)
            first_line = False

        if ";" and not "Dag" in line:
            line = line.split(";")
            cleanLine = ";".join(line[0:8])
            cleanLine = cleanLine + "\n"
            f1.write(cleanLine)
    f1.close()

def create_big_csv():
    blindernData = open("blindern.csv", "r").readlines()
    blindernData.pop(0)
    hemsedalData = open("hemsedal.csv", "r").readlines()
    hemsedalData.pop(0)

    mergedData = open("diggedata.csv", "w")
    mergedData.write("Dag-blindern;TA-blindern-01;TA-blindern-07;TA-blindern-13;TA-blindern-19;TAM-blindern;TAX-blindern;TAN-blindern;Dag-hemsedal;TA-hemsedal-01;TA-hemsedal-07;TA-hemsedal-13;TA-hemsedal-19;TAM-hemsedal;TAX-hemsedal;TAN-hemsedal\n")

    counter = 0
    for line in blindernData:
        line = line.rstrip()
        mergedData.write(line + ";" + hemsedalData[counter])
        counter += 1

    mergedData.close()


if __name__ == "__main__":
    clean_data(sys.argv[1])
    try:
        if sys.argv[2] == "--merge":
            #create_big_csv()
            pass
    except:
        pass
    create_big_csv()
