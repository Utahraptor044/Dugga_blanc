
# data 
nums = [12, -1, -4, 0, 7, 7, -9, 3]

###########################################################""
### exo a.
#####################################################"""
# "create a value that will contain the sum
sum = 0

for value in nums:
    if value > 5:
        sum += value

print(sum)

##########################################################################
### exo b.

#write a function bucket(n)


def bucket(n):
    if n <= -5:
        print("LOW")

    elif n > -5 and n < 5 :
        print("MID")

    elif n >= 5:
        print("HIGH")

    else:
        # Create a statement in the case of an input that is not a numerical value
        print("Please type an interger or a float value")

bucket(-9)
bucket(7)

######################################################""
### exo c.
# Help to understand the teerminal output
print("Exo 3 beginning")
#create variables for the count
low_cnt = 0
mid_cnt = 0
high_cnt = 0

# create an empty list that will save the HIGH values
odd_high = []

for n in nums:
    bucket(n)
    if n <= -5:
        low_cnt+=1
    elif n >= 5:
        high_cnt += 1
        odd_high.append(n)
    else:
        mid_cnt +=1

print(f"There is {low_cnt} values smaller or equal to -5, {mid_cnt} values include between -5 and 5, and {high_cnt} values greater than 5.")
print(odd_high)






