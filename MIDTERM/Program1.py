def palin(a):
    a_st = str(a)
    rev = " " 

    for char in a_st:
        rev = char + rev  

    return a_st == rev  

# Open the file and read lines
with open("C:/Users/JAN RODRIGO MARTINEZ/Documents/GitHub/Martinez_IT0011/MIDTERM/numbers.txt", "r") as file:
    lines = file.readlines()

# Process each line
for i, lin in enumerate(lines):
    nums = lin.strip().split(",")  
    sum = 0  

    for num in nums:
        num = num.strip() #remove space
        if num.isdigit():  
            sum += int(num) 
        else:
            print(f"Skipping invalid value: {num}")  

    # Check if sum is a palindrome
    if palin(sum):
        print(f"Line {i+1}: {lin.strip()} (sum {sum}) - Palindrome")
    else:
        print(f"Line {i+1}: {lin.strip()} (sum {sum}) - Not a palindrome")
