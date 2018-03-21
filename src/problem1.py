"""
Exam 1, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Kevin Chou.  March 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


###############################################################################
# DONE: 2.  READ the doc-string for the   product_of_digits   function below.
#           Ask your instructor for help if you do not understand it.
#
#   Once you are confident that you understand the doc-string
#   (ignore the code itself!), change the TO-DO for this problem to DONE.
###############################################################################
def product_of_digits(number):
    """
    What comes in:  A positive integer.
    What goes out:  The product of the digits in the given integer.
    Side effects:   None.
    Examples:
      -- product_of_integers(83135)  returns (8 * 3 * 1 * 3 * 5), which is 360

      -- product_of_integers(107)    returns (1 * 0 * 7), which is 0

      -- product_of_integers(2255)   returns (2 * 2 * 5 * 5), which is 100

      -- product_of_integers(8)      returns 8
    """
    digit_product = 1
    remaining_number = number
    while True:
        if remaining_number == 0:
            break
        digit_product = digit_product * (remaining_number % 10)
        remaining_number = remaining_number // 10

    return digit_product
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   product_of_digits   function
    #      - it has no TO-DO.
    #
    #   Do NOT copy code from the above   product_of_digits   function.
    #   Instead, ** CALL ** that function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 25 + 26 + 30 + 31  # which is 112
    answer = problem1a(25, 31, 14)
    print()
    print('Test 1 is: problem1a(25, 31, 14)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 2:
    expected = 4 + 10 + 11 + 12 + 13 + 14  # which is 64
    answer = problem1a(4, 17, 5)
    print()
    print('Test 2 is: problem1a(4, 17, 5)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 3:
    expected = 10 + 11 + 12 + 13  # which is 46
    answer = problem1a(4, 17, 4)
    print()
    print('Test 3 is: problem1a(4, 17, 4)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 4:
    expected = 10  # Only 10 has a product-of-digits that is less than 1
    answer = problem1a(4, 17, 1)
    print()
    print('Test 4 is: problem1a(4, 17, 1)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 5:
    expected = 0
    answer = problem1a(4, 17, 0)
    print()
    print('Test 5 is: problem1a(4, 17, 0)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 6:
    expected = 109 + 110 + 111 + 112 + 120 + 121 + 130  # which is 813
    answer = problem1a(109, 139, 3)
    print()
    print('Test 6 is: problem1a(109, 139, 3)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 7:
    expected = 109 + 110 + 111 + 112 + 120 + 121 + 130 + 140  # which is 953
    answer = problem1a(109, 140, 3)
    print()
    print('Test 7 is: problem1a(109, 140, 3)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 8:
    expected = 120 + 121 + 130 + 140  # which is 511
    answer = problem1a(113, 140, 3)
    print()
    print('Test 8 is: problem1a(113, 140, 3)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 9:
    expected = 139184
    answer = problem1a(1, 1000, 25)
    print()
    print('Test 9 is: problem1a(1, 1000, 25)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 10:
    expected = 1000 * (1 + 1000) // 2
    answer = problem1a(1, 1000, (9 * 9 * 9) + 1)
    print()
    print('Test 10 is: problem1a(1, 1000, (9 * 9 * 9) + 2)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 11:
    expected = (1000 * (1 + 1000) // 2) - 999
    answer = problem1a(1, 1000, (9 * 9 * 9))
    print()
    print('Test 11 is: problem1a(1, 1000, (9 * 9 * 9) + 1)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 12:
    expected = 91405
    answer = problem1a(1, 1000, 1)
    print()
    print('Test 12 is: problem1a(1, 1000, 1')
    print('  Expected:', expected)
    print('  Actual:  ', answer)


###############################################################################
# IMPORTANT note: in the following problem,
#    **  For full credit you must appropriately use (call)
#    **  the appropriate function(s) that are defined above.
###############################################################################
def problem1a(a, b, threshold):
    """
    What comes in:
      -- Positive integers a and b with a <= b
      -- A number ('threshold')
    What goes out:  Returns the sum of the numbers from a to b, inclusive,
      whose product-of-digits is strictly less than the given threshold.
    Side effects:   None.
    Examples:
      -- problem1a(25, 31, 14)  returns 112  because:

           The product-of-digits of 25 is 10, which  IS  less than 14
           The product-of-digits of 26 is 12, which  IS  less than 14
           The product-of-digits of 27 is 14, which  is NOT  less than 14
           The product-of-digits of 28 is 16, which  is NOT  less than 14
           The product-of-digits of 29 is 18, which  is NOT  less than 14
           The product-of-digits of 30 is  0, which  IS  less than 14
           The product-of-digits of 31 is  3, which  IS  less than 14

         and so the function returns the sum of the integers above
         whose product-of-digits are less than 14,
         i.e.   25 + 26 + 30 + 31,  which is 112

      -- problem1a(4, 17, 5) returns 4 + 10 + 11 + 12 + 13 + 14,  which is 64
      -- problem1a(4, 17, 4) returns 10 + 11 + 12 + 13,  which is 46
      -- problem1a(4, 17, 1) returns 10
      -- problem1a(4, 17, 0) returns 0
      -- problem1a(109, 139, 3)
              returns 109 + 110 + 111 + 112 + 120 + 121 + 130,  which is 813
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # IMPORTANT NOTE
    #     If you happen to know how to use a RANGE expression with 2 or 3
    #     arguments, don't do that.  You are only allowed to use the
    #     1-argument version of the RANGE statement to solve this problem.
    # -------------------------------------------------------------------------
    total = 0
    for k in range(b-a+1):
        if product_of_digits(a+k) < threshold:
            total = total + a + k
    return total


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement at least 4 tests of the problem1b function.
    #   Note that you CANNOT use  problem1b(1)  or  problem1b(2)  as tests, per
    #   the specification below that says that the argument must be at least 3.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')
    print('Test1:')
    print('When r = 3')
    answer = problem1b(3)
    print('Expected: 3')
    print('Actual:', answer)

    print('--------------------------------------------------')
    print('Test2:')
    print('When r = 4')
    answer = problem1b(4)
    # 4 + 10 + 11 + 12 + 13 + 14
    print('Expected: 64')
    print('Actual:', answer)

    print('--------------------------------------------------')
    print('Test3:')
    print('When r = 5')
    answer = problem1b(5)
    # 5+10+11+12+13+14+15+20+21+22
    print('Expected: 143')
    print('Actual:', answer)

    print('--------------------------------------------------')
    print('Test4:')
    print('When r = 6')
    answer = problem1b(6)
    # 6+10+11+12+13+14+15+16+20+21+22+23+30+31+32
    print('Expected: 276')
    print('Actual:', answer)

###############################################################################
# IMPORTANT note: in the following problem,
#    **  For full credit you must appropriately use (call)
#    **  the appropriate functions that are defined above,
#    **  possibly including ones you have written.
###############################################################################


def problem1b(r):
    """
    What comes in:  An integer r that is at least 3.
    What goes out:  Returns the sum of the numbers from r to (r squared),
      inclusive, whose product-of-digits is less than or equal to r.
    Side effects:   None.
    Examples:
      -- problem1b(8)  returns 682  because:
           Of the numbers from 8 to 64,
           the ones whose product-of-digits is less than or equal to 8 are:
    8 10 11 12 13 14 15 16 17 18  20 21 22 23 24  30 31 32 40 41 42 50 51 60 61
           and the sum of the above numbers is 682
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          See the IMPORTANT NOTE just before the DEF above.
    # -------------------------------------------------------------------------
    return problem1a(r, r**2, r+1)
    # for k in range(r**2 - r+1):


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
