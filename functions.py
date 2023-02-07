#1
#creating a function which finds the lowest number of any given array
def minimum(arr):
    arr.sort()
    return arr[0]

#2
#creating a function which finds the highest number of any given array
def maximum(arr):
    arr.sort()
    return arr[len(arr)-1]

#3
#Creating a function which finds the greatest possible difference
#from the highest and lowest numbers found in the array by the previous two functions
def largest_possible_dif(arr):
    highest = maximum(arr)
    lowest = minimum(arr)
    return(highest-lowest)

#4
#creating a function that will find the sum of two numbers - adds the two variables, sets them equal to a new variable, and returns them
def find_sum():
    num1 = input("Please input the first number you would like to add: ")
    num2 = input("Please input the second number you would like to add: ")
    num_sum = int(num1) + int(num2)
    return(num_sum)

#5
#creating a function to count how many letter "a"'s are in a string
def count_a():
    word = input("Please input the string that you would like to find out the number of letter 'a's: ")
    #lowercasing whatever string is input
    lowered_word = word.lower()
    #turning the inputted string into a list of individual characters
    lowered_word[::-1]
    #defining a count for the while loop and the number of a's detected
    count = 0
    num_a = 0
    while (count < len(lowered_word)):
        if (lowered_word[count] == "a"):
            num_a += 1
        count += 1
    return (num_a)

#6
#creating a function which finds the factorial of any number inputted by the user
def factorial(num):
    #defining a count for the while loop so that it goes over each number and multiplies them
    count = 0
    #setting a product where all the numbers will be multiplied and saved to
    product = 1
    while (count < num):
        count += 1
        product *= count
    return(product)

#7
def better_is_palindrome(word):
    palindrome = "".join(word[::-1])
    return (palindrome.lower() == word.lower())

#8
#creating a function which prints the sum of all numbers from zero to, and including the input
def sum_to(n):
    #where the sum will be counted
    total = 0
    #counter for the while loop
    count = 0
    while (count < int(n)):
        count += 1
        total += count
    return (total)

#9
def indexed_names (names):
    for index, vars in enumerate(names):
        #breaking each name into a list so that charcters can be added to the beginning of the strings
        namex = [*vars] 
        #recombining the lists into a string
        namex.insert(0, str(index)+": ")
        names[index] = "".join(namex)
    return (names)

#10
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)

#1
def nearest_sq(n):
    if n == 1 or n == 2:
        return 1
    if n%2==0:
        temp1 = n/2
    else:
        temp1 = (n+1)/2
    temp2 = 0
    temp3 = 0
    while 1:
        if temp1*temp1 >= n:
            temp2 = temp1
        else:
            while 1:
                temp0 = temp2 - temp1
                if temp0 == 1:
                    break
                if temp0%2==0:
                    temp3 = temp0/2 + temp1
                else:
                    temp3 = (temp0+1)/2 + temp1
                if temp3*temp3 > n:
                    if temp3 <= temp1:
                        break
                    temp2 = temp3
                elif temp3*temp3 <n:
                    if temp3 <= temp1:
                        break
                    temp1 = temp3
                else: 
                    return temp3*temp3
            
            if(n - temp1*temp1 >= temp2*temp2 - n):
                return temp2*temp2
            else: 
                return temp1*temp1
        if temp1%2==0:
            temp1 = temp1/2
        else:
            temp1 = (temp1+1)/2

#2
def sum_of_integers_in_string(s):
    result = 0
    current = ""
    for i,char in enumerate(s):
        if i != len(s) - 1:
            if char.isnumeric():
                current += char
            else:
                if len(current) >= 1:
                    result += int(current)
                    current = ""
        else:
            if char.isnumeric():
                if current:
                    current += char
                    result += int(current)
                else:
                    result += int(char)
            else:
                if current:
                    result += int(current)
               
    return result

#3
def solution(number):
    sum=0
    if number%3==0:
        nearest_three=number-3
    else:
        nearest_three=number-(number%3)
    if number%5==0:
        nearest_five=number-5
    else:
        nearest_five=number-(number%5)
    for x in range(nearest_three, 0, -3):
        sum+=x
    for y in range(nearest_five, 0, -5):
        if y%3==0:
            continue
        else:
            sum+=y
    return sum

#4
def find_it(seq):
    passes = 0
    odd_appearance_amount = 0

    answer = 0

    # takes all numbers in the range of the list
    for cardinal_num in range(min(seq), max(seq) + 2):
        passes += 1
        if passes == 2:
            passes = 1

            if not odd_appearance_amount % 2 == 0:
                return answer

            odd_appearance_amount = 0

        # checks if any numbers in the range of the list matches a number in that list
        for num in seq:
            if num == cardinal_num:
                if passes == 1:
                    odd_appearance_amount += 1
                    answer = num

#5
def count_bits(n):
    out=""
    count=0
    while(1):
        div=n//2
        mod=n%2        
        out+=str(mod)
        if(div==0):
            break
        n=div  
    for x in out:
        if x=='1':
            count+=1
        else:
            pass
    return count
