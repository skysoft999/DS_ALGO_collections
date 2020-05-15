"""
Title : Digit rearrangement method
to find next
greater number with same set of digits

Topic : Array problems solving techniques with examples
Description :You have given a number.
You have to find out next greater
number to given number with the
same set of digits

~~~~Asked in : Morgon Stanley,
Makemystrip, Amazon
"""


# Python program to find the smallest number which
# is greater than a given no. has same set of
# digits as given number

# Given number as int array, this function finds the
# greatest number and returns the number as integer

def findNext(number, n):
    # Start from the right most digit and find the first
    # digit that is smaller than the digit next to it
    # import pdb;pdb.set_trace()
    for i in range(n-1, 0, -1):
        if number[i] > number[i-1]:
            break

    # If no such digit found,then all numbers are in
    # descending order, no greater number is possible
    if i == 0:
        print "Next number not possible"
        return -1

    # Find the smallest digit on the right side of
    # (i-1)'th digit that is greater than number[i-1]
    x = number[i-1]
    smallest = i
    for j in range(i+1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    # Swapping the above found smallest digit with (i-1)'th
    number[smallest], number[i-1] = number[i-1], number[smallest]

    x = number[:i]
    x.extend(sorted(number[i:]))
    x = map(str, x)
    return ''.join(x)

# Driver Program to test above function
digits = "218765"

number = list(map(int, digits))
print "Next number with set of digits is %s" % (findNext(number, len(number)))
