# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;

	for i in range(0,number):
		x = (i+1)
		total+=(x*x)

	return total
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1 to number):
		total=total*(i+1)
	return total
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* ex. Samuel Vimes
	* ...

### Timing Data

grab a screenshot of your excel graphs and put it here


### Summary 
|function| runtime based on analysis | Most similar curve | 
|---|---|---|
|partb_one()|  |  |
|partb_two()|   |   |
|partb_three()|   |   |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.


## Reflection:

1. for each function what growth rate best match your results?
2. Does your analysis match your analysis?  If not, where do you suppose the error occurred?
3. What sort of conclusions can you draw based on your observations?


