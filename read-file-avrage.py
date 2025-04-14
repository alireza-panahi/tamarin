numbers = []
file_path = "numbers.txt" 
#مسیر فایل اعداد 
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  
        print(line)  
        if line != "":  #با این دستور اگر خطی خالی باشد حذف میشود
            number = float(line)  
            numbers.append(number)
average = sum(numbers) / len(numbers)
print("avrage= ", average)
