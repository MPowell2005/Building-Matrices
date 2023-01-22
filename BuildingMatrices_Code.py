'''
Author: Michael Powell
Narrative: This program allows the user to execute various methods on a class called "Matrix".

Features:
    (1) void_print
    (2) plus
    (3) times
    (4) scalarTimesRow
    (5) switchRows
    (6) linearCombRows
    (7) rowreduce
    (8) invert

@author: mpowell23@gcds.net
'''

import random

class Matrix:
    def __init__(self, dimensions, matrix_option):
        '''
        Summary:
            This function constructs a matrix according to
            the values of its dimensions and its elements provided by the user.
        
        Arguments:
            self (Matrix)
            dimensions (List): This argument encodes the dimensions of the matrix as follows: [ROW X COLUMN].
                ROW: A natural number from 1 through 10 for randomization or of any size for customization.
                COLUMN: A natural number from 1 through 10 for randomization or of any size for customization.
            matrix_option (str): This argument gives whether the user wants to randomize or customize the dimensions and elements of the matrix.    
        '''
        self.r = dimensions[0]
        self.c = dimensions[1]
        self.M = []
        
        # Construction of matrix with customized elements
        if matrix_option == '1' or matrix_option == 'customized dimensions and customized elements' or matrix_option == '4' or matrix_option == 'randomized dimensions and customized elements':
            for i in range(self.r):
                row = []
                for j in range(self.c):
                    while True:
                        element = input('What is the value of the element of the matrix at (' + str(i) + ',' + str(j) + ')?\n')
                        try:
                            element = float(element)
                            break
                        except:
                            print('Please ensure that the value of the element is a float.')
                    row.append(element)
                self.M.append(row)
        
        # Construction of matrix with randomized elements
        elif matrix_option == '2' or matrix_option == 'customized dimensions and randomized elements' or matrix_option == '3' or matrix_option == 'randomized dimensions and randomized elements':
            for i in range(self.r):
                row = []
                for j in range(self.c):
                    row.append(random.randint(0, 9))
                self.M.append(row)
        
        # Construction of matrix with all elements containing the value of 0
        elif matrix_option == 'zero matrix':
            for i in range(self.r):
                row = []
                for j in range(self.c):
                    row.append(0)
                self.M.append(row)
        
        # Construction of identity matrix
        elif matrix_option == 'identity matrix':
            for i in range(self.r):
                row = []
                for j in range(self.c):
                    row.append(0)
                self.M.append(row)
            for i in range(self.r):
                for j in range(self.c):
                    self.M[i].pop(i)
                    self.M[i].insert(i, 1)
    
    
    def copy_elements(self, other):
        '''
        Summary:
            This function copies the elements and dimensions of one matrix to another.

        Arguments:
            self (Matrix)
            other (Matrix): This argument encodes a matrix that 'self' copies.
        
        Returns:
            self (Matrix)
        '''
        for i in range(self.r):
            row = []
            for j in range(self.c):
                row.append(other.M[i][j])
            self.M.pop(i)
            self.M.insert(i, row)        
        return self
    
    
    def round(self):
        '''
        Summary:
            This function rounds all of the elements of a matrix to five decimal places.
        
        Arguments:
            self (Matrix)
        
        Returns:
            self (Matrix)
        '''
        for i in range(self.r):
            for j in range(self.c):
                self.M[i][j] = round(self.M[i][j], 5)
                # If the last digit in the value of one of the elements is zero (ex. 1.0), convert it to an integer
                if int(list(str(self.M[i][j]))[len(list(str(self.M[i][j]))) - 1]) == 0:
                    self.M[i][j] = int(self.M[i][j])
        
        return self   
    
    
    # Method (1)
    def void_print(self):
        '''
        Summary:
            This function prints the elements of matrix 'self'.
        
        Arguments:
            self (Matrix)
        '''
        for row in self.M:
            print(row)
    
    
    # Method (2)
    def plus(self, other):
        '''
        Summary:
            This function adds two matrices.
        
        Arguments:
            self (Matrix)
            other (Matrix)
        
        Returns:
            sum_self_and_other (Matrix): This output is the sum of matrix 'self' and matrix 'other'.
        '''
        sum_self_and_other = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        
        for i in range(self.r):
            for j in range(self.c):
                sum_self_and_other.M[i][j] = self.M[i][j] + other.M[i][j]
                
        return sum_self_and_other
    
    
    # Method (3)
    def times(self, other):
        '''
        Summary:
            This function multiplies two matrices.
        
        Arguments:
            self (Matrix)
            other (Matrix)
        
        Returns:
            product_self_and_other (Matrix): This output is the product of matrix 'self' and matrix 'other'.
        '''
        product_self_and_other = Matrix(dimensions = [self.r, other.c], matrix_option = 'zero matrix')
        
        for i in range(self.r):
            for j in range(other.c):
                element_value = 0
                for k in range(self.c):
                    element_value = element_value + (self.M[i][k] * other.M[k][j])
                product_self_and_other.M[i][j] = element_value
        
        return product_self_and_other
    
    
    # Method (4)
    def scalarTimesRow(self, scalar, row_number):
        '''
        Summary:
            This function multiplies a scalar to the elements of a given row for a given matrix.
        
        Arguments:
            self (Matrix)
            scalar (float)
            row_number (int)
        
        Returns:
            scaled_self (Matrix): This output is the scaled matrix of 'self'.
        '''
        scaled_self = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        scaled_self = scaled_self.copy_elements(self)
        
        for j in range(self.c):
            scaled_self.M[row_number][j] = scalar * self.M[row_number][j]
        
        return scaled_self
    
    
    # Method (5)
    def switchRows(self, row_1, row_2):
        '''
        Summary:
            This function switches the elements from one row with those of another row for a given matrix.
        
        Arguments:
            self (Matrix)
            row_1 (int)
            row_2 (int)
        
        Returns:
            switched_self (Matrix): This output is the switched matrix of 'self'.
        '''
        switched_self = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        switched_self = switched_self.copy_elements(self)
        
        # Switches row_1 and row_2 if row_1 is greater than row_2
        if row_1 > row_2:
            switched_self.M.pop(row_1)
            switched_self.M.pop(row_2)
            switched_self.M.insert(row_2, self.M[row_1])
            switched_self.M.insert(row_1, self.M[row_2])
        
        # Switches row_1 and row_2 if row_1 is less than row_2
        elif row_1 < row_2:
            switched_self.M.pop(row_2)
            switched_self.M.pop(row_1)
            switched_self.M.insert(row_1, self.M[row_2])
            switched_self.M.insert(row_2, self.M[row_1])
        
        # Does not switch any rows if row_1 is equal to row_2
        else:
            pass
        
        return switched_self
    
    
    # Method (6)
    def linearCombRows(self, scalar, row_1, row_2):
        '''
        Summary:
            This function adds a scalar multiple of the elements in row_1 to those of row_2 for a given matrix.
        
        Arguments:
            self (Matrix)
            scalar (float)
            row_1 (int)
            row_2 (int)
        
        Returns:
            linear_combinations_self: This output contains the linear combinations applied to matrix 'self'.
        '''
        linear_combinations_self = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        linear_combinations_self = linear_combinations_self.copy_elements(self)
        
        linear_combinations_self = linear_combinations_self.scalarTimesRow(scalar, row_1)
        
        for j in range(self.c):
            linear_combinations_self.M[row_2][j] = linear_combinations_self.M[row_2][j] + linear_combinations_self.M[row_1][j]
        
        linear_combinations_self = linear_combinations_self.scalarTimesRow(scalar**-1, row_1)
        
        return linear_combinations_self
    
    
    # Method (7)
    def rowreduce(self):
        '''
        Summary:
            This function row reduces matrix 'self'.
        
        Arguments:
            self (Matrix)
        
        Returns:
            rowreduce_self (Matrix): This output is the row reduced matrix 'self'.
        '''
        rowreduce_self = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        rowreduce_self = rowreduce_self.copy_elements(self)
        
        for j in range(self.c):
            # Row-reduce the matrix 'self' if the current column is less than the number of rows of matrix 'self' minus 1
            if j <= self.r - 1:
                counter = 1
                while True:
                    # Switch the current row of matrix 'self' if one of the elements of its diagonal is equal to 0
                    if rowreduce_self.M[j][j] == 0:
                        # Stop switching if the counter reaches the value of the number of rows of the matrix, meaning the column contains all 0s
                        if counter == self.r:
                            break
                        # Do not switch if the counter is less than or equal to the current row; only switch rows geometrically below the current one
                        elif counter <= j:
                            counter = counter + 1
                        # Otherwise, switch the current row with a row separated by the value of counter
                        else:
                            rowreduce_self = rowreduce_self.switchRows(j, counter)
                            counter = counter + 1
                    # Otherwise, multiply the current row by a scalar equal to the reciprocal of the value of element on the diagonal
                    else:
                        rowreduce_self = rowreduce_self.scalarTimesRow(rowreduce_self.M[j][j]**-1, j)
                        break     
                # Move down the column to convert each element to the value of 0
                for i in range(self.r):
                    if rowreduce_self.M[i][j] == 0:
                        pass
                    else:
                        if i == j:
                            pass
                        else:
                            rowreduce_self = rowreduce_self.linearCombRows(-(rowreduce_self.M[i][j]), j, i)
            # Do not row-reduce the matrix 'self'
            else:
                break

        return rowreduce_self
    
    
    # Method (8)
    def invert(self):
        # Create a matrix with the same elements as matrix 'self'
        invert_self = Matrix(dimensions = [self.r, self.c], matrix_option = 'zero matrix')
        invert_self = invert_self.copy_elements(self)
        
        # Extend the new matrix with its identity matrix and row-reduce
        identity_matrix = Matrix(dimensions = [self.r, self.c], matrix_option = 'identity matrix')
        for i in range(self.r):
            invert_self.M[i].extend(identity_matrix.M[i])
        invert_self.c = 2 * invert_self.c
        invert_self = invert_self.rowreduce()
        invert_self.c = int(invert_self.c/2)
        
        # Remove half of the row-reduced matrix on the left
        for i in range(invert_self.r):
            counter = 1
            while counter <= invert_self.c:
                invert_self.M[i].pop(0)
                counter = counter + 1
       
        return invert_self


def get_MatrixOption():
    '''
    Summary:
        This function asks the user for the matrix option to initially create a matrix class.
    
    Arguments:
        None
    
    Return:
        matrix_option (str): This argument gives whether the user wants to randomize or customize the dimensions and elements of the matrix.
    '''
    while True:
        matrix_option = input('Do you want a matrix that has:\n(1) Customized dimensions and customized elements,\n(2) Customized dimensions and randomized elements,\n(3) Randomized dimensions and randomized elements,\nor\n(4) Randomized dimensions and customized elements?\n')
        matrix_option = matrix_option.lower()
        
        if matrix_option == '1' or matrix_option == 'customized dimensions and customized elements' or matrix_option == '2' or matrix_option == 'customized dimensions and randomized elements' or matrix_option == '3' or matrix_option == 'randomized dimensions and randomized elements' or matrix_option == '4' or matrix_option == 'randomized dimensions and customized elements':
            break
        
        else:
            print('Please insert a matrix option consistent with the provided options or their corresponding numbers.')
    
    return matrix_option


def get_Dimensions(matrix_option):
    '''
    Summary:
        This function obtains the dimensions of the matrix through randomization or customization according to matrix_option.
        
    Arguments:
        matrix_option (str): This argument gives whether the user wants to randomize or customize the dimensions and elements of the matrix.
    
    Returns:
        dimensions (List): This argument encodes the dimensions of the matrix as follows: [ROW X COLUMN].
            ROW: A natural number from 1 through 10 for randomization or of any size for customization.
            COLUMN: A natural number from 1 through 10 for randomization or of any size for customization.
    '''
    # Determines the dimensions of a matrix through customization
    if matrix_option == '1' or matrix_option == 'customized dimensions and customized elements' or matrix_option == '2' or matrix_option == 'customized dimensions and randomized elements':
        # Asks for the number of rows from the user
        while True:
            number_rows = input('Insert the number of rows of your matrix as a natural number.\n')
            try:
                number_rows = int(number_rows)
                if number_rows > 0 :
                    break
                else :
                    print('Please ensure that the number of rows is a natural number for your matrix.')
            except:
                print('Please ensure that the number of rows is a natural number for your matrix.')
        # Asks for the number of columns from the user
        while True:
            number_columns = input('Insert the number of columns of your matrix as a natural number.\n')
            try:
                number_columns = int(number_columns)
                if number_columns > 0 :
                    break
                else :
                    print('Please ensure that the number of columns is a natural number for your matrix.')
                    continue
            except:
                print('Please ensure that the number of columns is a natural number for your matrix.')
                continue
        
        dimensions = [number_rows, number_columns]
    
    # Determines the dimensions of a matrix through randomization
    elif matrix_option == '3' or matrix_option == 'randomized dimensions and randomized elements' or matrix_option == '4' or matrix_option == 'randomized dimensions and customized elements':
        dimensions = [random.randint(1, 10), random.randint(1, 10)]
    
    return dimensions


def main():
    matrix_option = get_MatrixOption()
    dimensions = get_Dimensions(matrix_option)
    trixie = Matrix(dimensions, matrix_option)
    
    restart = 'yes'
    while restart == 'yes':
        # Showing the user the matrix that they constructed
        print('The matrix you constructed is as follows:')
        trixie.void_print()
        
        # Asks for the executable method from the user
        while True:
            method = input('What method do you want to execute on your matrix:\n(1) void_print\n(2) plus\n(3) times\n(4) scalarTimesRow\n(5) switchRows\n(6) linearCombRows\n(7) rowreduce\n(8) invert\n')
            if method == '1' or method == 'void_print' or method == '2' or method == 'plus' or method == '3' or method == 'times' or method == '4' or method == 'scalarTimesRow' or method == '5' or method == 'switchRows' or method == '6' or method == 'linearCombRows' or method == '7' or method == 'rowreduce' or method == '8' or method == 'invert':
                break
            else:
                print('Please insert a method consistent with the provided options or their corresponding numbers.')
        
        # Method (1)
        if method == '1' or method == 'void_print':
            print('The matrix that you have constructed will be printed on the screen as follows:')
            trixie.void_print()
        
        # Method (2)
        elif method == '2' or method == 'plus':
            while True:
                matrix_option_allice = get_MatrixOption()
                dimensions_allice = get_Dimensions(matrix_option_allice)
                if trixie.r == dimensions_allice[0] and trixie.c == dimensions_allice[1]:
                    break
                else:
                    print('Please ensure that the dimensions of the first matrix are equal to those of the second matrix.')
            
            allice = Matrix(dimensions_allice, matrix_option_allice)
            sum_trixie_and_allice = trixie.plus(allice)
            
            print('The sum of the first matrix')
            trixie.void_print()
            print('and the second matrix')
            allice.void_print()
            print('is equal to the following:')
            sum_trixie_and_allice.void_print()
        
        # Method (3)
        elif method == '3' or method == 'times':
            while True:
                matrix_option_allice = get_MatrixOption()
                dimensions_allice = get_Dimensions(matrix_option_allice)
                if trixie.c == dimensions_allice[0]:
                    break
                else:
                    print('Please ensure that the number of columns of the first matrix is equal to the number of rows of the second matrix.')
            
            allice = Matrix(dimensions_allice, matrix_option_allice)
            product_trixie_and_allice = trixie.times(allice)
            
            print('The product of the first matrix')
            trixie.void_print()
            print('and the second matrix')
            allice.void_print()
            print('is equal to the following:')
            product_trixie_and_allice.void_print()
        
        # Method (4)
        elif method == '4' or method == 'scalarTimesRow':
            # Asks the user for the scalar
            while True:
                scalar = input('What is the value of the scalar applied to the matrix?\n')
                try:
                    scalar = float(scalar)
                    break
                except:
                    print('Please ensure that the scalar is a float.')
            # Asks the user for the row number
            while True:
                rownumber = input('The scalar will be applied to which row number?\n')
                try:
                    rownumber = int(rownumber)
                    if rownumber >= 0 and rownumber < len(trixie.M):
                        break
                    else:
                        print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
                except:
                    print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
            
            scaled_trixie = trixie.scalarTimesRow(scalar, rownumber)
            
            print('The scalar of ' + str(scalar) + ' applied to row number ' + str(rownumber) + ' on the matrix')
            trixie.void_print()
            print('is equal to')
            scaled_trixie.void_print()
        
        # Method (5)
        elif method == '5' or method == 'switchRows':
            # Asks the user for the first row for switching
            while True:
                row_1 = input('What is the position for the first row for switching?\n')
                try:
                    row_1 = int(row_1)
                    if row_1 >= 0 and row_1 < len(trixie.M):
                        break
                    else:
                        print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
                except:
                    print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
            # Asks the user for the second row for switching
            while True:
                row_2 = input('What is the position for the second row for switching?\n')
                try:
                    row_2 = int(row_2)
                    if row_2 >= 0 and row_2 < len(trixie.M):
                        break
                    else:
                        print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
                except:
                    print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
            
            switched_trixie = trixie.switchRows(row_1, row_2)
            
            print('When row number ' + str(row_1) + ' is switched with ' + str(row_2) + ' on the matrix')
            trixie.void_print()
            print('the matrix becomes')
            switched_trixie.void_print()
        
        # Method (6)
        elif method == '6' or method == 'linearCombRows':
            # Asks the user for the scalar
            while True:
                scalar = input('What is the value of the scalar applied to one of the rows of the matrix?\n')
                try:
                    scalar = float(scalar)
                    break
                except:
                    print('Please ensure that the scalar is a float.')
            # Asks the user for the first row to which the scalar multiple will be applied
            while True:
                row_1 = input('The scalar multiple will be applied to which row number?\n')
                try:
                    row_1 = int(row_1)
                    if row_1 >= 0 and row_1 < len(trixie.M):
                        break
                    else:
                        print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
                except:
                    print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
            # Asks the user for the second row to which the scalar multiple of the first row will be applied        
            while True:
                row_2 = input('The scalar multiple of the first row will be added with which row number?\n')
                try:
                    row_2 = int(row_2)
                    if row_2 >= 0 and row_2 < len(trixie.M):
                        break
                    else:
                        print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
                except:
                    print('Please ensure that the row number is a natural number including zero less than or equal to the number of rows of your matrix.')
            
            linear_combinations_trixie = trixie.linearCombRows(scalar, row_1, row_2)
            
            print('For the following matrix')
            trixie.void_print()
            print('when the scalar multiple of ' + str(scalar) + ' was applied to row number ' + str(row_1) + ' and added to row number ' + str(row_2) + ', the result was as follows:')
            linear_combinations_trixie.void_print()
        
        # Method (7)
        elif method == '7' or method == 'rowreduce':
            rowreduce_trixie = trixie.rowreduce()
            rowreduce_trixie = rowreduce_trixie.round()
            
            print('The row reduction of the matrix that you constructed, which is')
            trixie.void_print()
            print('is as follows:')
            rowreduce_trixie.void_print()
        
        # Method (8)
        elif method == '8' or method == 'invert':
            if trixie.r == trixie.c:
                invert_trixie = trixie.invert()
                # Product verification
                product_1 = (trixie.times(invert_trixie)).round()
                product_2 = (invert_trixie.times(trixie)).round()
                invert_trixie = invert_trixie.round()
                
                verify = 'yes'
                for row in range(product_1.r):
                    for column in range(product_1.c):
                        if row == column:
                            if product_1.M[row][column] == 1:
                                continue
                            else:
                                verify = 'no'
                        else:
                            if product_1.M[row][column] == 0:
                                continue
                            else:
                                verify = 'no'
                for row in range(product_2.r):
                    for column in range(product_2.c):
                        if row == column:
                            if product_2.M[row][column] == 1:
                                continue
                            else:
                                verify = 'no'
                        else:
                            if product_2.M[row][column] == 0:
                                continue
                            else:
                                verify = 'no'
    
                # Product between constructed matrix and its inverse as well as the vice-versa
                if verify == 'yes':
                    print('The inverse of your constructed matrix')
                    trixie.void_print()
                    print('is equal to the following')
                    invert_trixie.void_print()
                    print('Since the product of your constructed matrix and its inverse is equal to the identity matrix as follows')
                    product_1.void_print()
                    print('and the product of its inverse and your constructed matrix is equal to the identity matrix as follows')
                    product_2.void_print()
                    print('your constructed matrix is indeed invertible and the above result is accurate.')
                else:
                    print('The matrix you constructed is as follows:')
                    trixie.void_print()
                    print('and its determined inverse matrix is as follows:')
                    invert_trixie.void_print()
                    print('Your constructed matrix is not invertible because the product of it and its determined inverse matrix')
                    product_1.void_print()
                    print('as well as the vice-versa')
                    product_2.void_print()
                    print('does not result in two identity matrices.')
                    print('This indicates that the determinant of your constructed matrix is equal to 0.')
            else:
                print('Since the matrix you constructed is not a square matrix, it has no inverse matrix.')
        
        # Repeating the executable methods
        while True:
            restart = input('Do you want to execute another method on your matrix? (yes or no)\n')
            if restart == 'yes':
                break
            elif restart == 'no':
                print('The program has ended...')
                break
            else:
                print("Please insert a 'yes' or 'no' answer.")
        print('\n')
if __name__ == '__main__':
    main()  