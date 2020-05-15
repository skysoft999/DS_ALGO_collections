"""
Title : Linear time approach to solve jump game problem

Topic : Array problems solving techniques with examples

Description :Given an array of integers
where each element represents the max number
of steps that can be made forward from
that element. Write a program to find the minimum
number of jumps to reach the end of the array
(starting from the first element).
If an element is 0, then cannot move
through that element.
~~~~ Asked in: Adobe, Intuit
"""


def minJumps(arr, n):
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    maxReach = arr[0]
    step = arr[0]
    jump = 1
    import pdb;pdb.set_trace()
    for i in range(1, n):
        if i == n-1:
            return jump
        maxReach = max(maxReach, i+arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= maxReach:
                return -1
            step = maxReach - i
    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach end is %d " % minJumps(arr, size))


"""
Implementation:
Variables to be used:

1. maxReach The variable maxReach stores at all time the maximal reachable index in the array.
2. step The variable step stores the number of steps we can still take(and is initialized with value at index 0,i.e. initial number of steps)
3. jump jump stores the amount of jumps necessary to reach that maximal reachable position.

Given array arr = 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9

maxReach = arr[0]; // arr[0] = 1, so the maximum index we can reach at the moment is 1.

step = arr[0]; // arr[0] = 1, the amount of steps we can still take is also 1.

jump = 1; // we will always need to take at least one jump.

Now, starting iteration from index 1, the above values are updated as follows:


1. First we test whether we have reached the end of the array, in that case we just need to return the jump variable.
	
	if (i == arr.length - 1)
    	return jump;


2. Next we update the maxReach. This is equal to the maximum of maxReach and i+arr[i](the number of steps we can take from the current position).
	
	maxReach = Math.max(maxReach,i+arr[i]);

3. We used up a step to get to the current index, so steps has to be decreased.
	
	step--;

4. If no more steps are remaining 
(i.e. steps=0, then we must have used a jump.
Therefore increase jump. Since we know that it 
is possible somehow to reach maxReach, we again 
initialize the steps to the number of steps 
to reach maxReach from position i. 
But before re-initializing step, 
we also check whether a step is becoming zero or negative. 
In this case, It is not possible to reach further.

"""