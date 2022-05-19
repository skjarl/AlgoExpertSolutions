# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

#if next number is an array
#then next number = productSum(array,depth)
#else next number != array
#so we add it to the running sum

def productSum(array,depth=1):
	sum = 0

	for element in array:
		if type(element) == int or type(element) == float:
			sum += element
		else:
			sum += productSum(element,depth + 1)
	
	return (sum * depth)

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))