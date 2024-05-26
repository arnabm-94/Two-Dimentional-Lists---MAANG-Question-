#Given 2D list calculate the sum of diagonal elements.


#Define a function called diagonal_sum that takes a 2D list (matrix) as its argument.
def diagonal_sum(matrix):
    # TODO
    # Initialize the sum to 0
#Initialize a variable 'total' to store the sum of the diagonal elements. Set its initial value to 0.
    total = 0
    
    # Iterate over the matrix to sum the diagonal elements
#Start a for loop that iterates through the range of the length of the matrix (number of rows). 
#The index variable is 'i'.
    for i in range(len(matrix)):
        total += matrix[i][i]
#Add the value of the diagonal element at the current index to the 'total'. 
#The diagonal element is the one where the row and column indices are the same (i.e., matrix[i][i]).   
    return total
#After the for loop is done, return the total sum of the diagonal elements.

# Example usage
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # Output: 15

'''
#Time complexity:

O(n), where n is the number of rows (or columns) in the matrix. 
The function iterates through the rows once.

#Space complexity:

O(1), as the function only uses a single variable to store the sum (total).
'''
