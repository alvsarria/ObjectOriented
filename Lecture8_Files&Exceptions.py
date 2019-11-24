file_path = "C://Users//alvar//Documents//DT265C - Fundamentals of Computing//Object Oriented SW - GitHub//" \
            "Lecture8_Files&Exceptions//"

file_obj = open(file_path+"twinkle.txt", "r+")

for line in file_obj:
    print(line.strip())

file_obj.close()

output_file = open("numbers.txt","w")

for i in range(0,11):
    output_file.write(str(i))
    output_file.write("\n")

output_file.close()