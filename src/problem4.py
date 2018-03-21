"""
Exam 1, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Kevin Chou.  March 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4   function. """
    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem4   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 2
    answer = problem4(10)
    print()
    print('Test 1 is: problem4(10)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 2:
    expected = 6
    answer = problem4(24)
    print()
    print('Test 2 is: problem4(24)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 3:
    expected = 0
    answer = problem4(13)
    print()
    print('Test 3 is: problem4(13)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 4:
    expected = 6
    answer = problem4(30)
    print()
    print('Test 4 is: problem4(30)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 5:
    expected = 22
    answer = problem4(360)
    print()
    print('Test 5 is: problem4(360)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 6:
    expected = 0
    answer = problem4(97)
    print()
    print('Test 6 is: problem4(97)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 7:
    expected = 14
    answer = problem4(1000)
    print()
    print('Test 7 is: problem4(1000)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 8:
    expected = 6
    answer = problem4(1001)
    print()
    print('Test 8 is: problem4(1001)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 9:
    expected = 34
    answer = problem4(100000)
    print()
    print('Test 9 is: problem4(100000)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 10:
    expected = 2
    answer = problem4(100001)
    print()
    print('Test 10 is: problem4(100001)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 11:
    expected = 46
    answer = problem4(2224422)
    print()
    print('Test 10 is: problem4(2224422)')
    print('  Expected:', expected)
    print('  Actual:  ', answer)


def problem4(m):
    """
    What comes in:  Positive integer m.
    What goes out:  Returns the number of non-trival FACTORS of m, where:
      -- a FACTOR of m is a positive integer that divides evenly into m
      -- the TRIVIAL factors of m are 1 and m, and the NON-TRIVIAL factors
           of m are all the factors EXCEPT the trivial ones.
    Side effects:   None.
    Examples:
      -- problem4(10)  returns 2  because 10 has 2 non-trivial factors,
                                      namely: 2 and 5.
      -- problem4(24)  returns 6  because 24 has 6 non-trivial factors,
                                      namely: 2, 3, 4, 6, 8, and 12.
      -- problem4(13)  returns 0  because  7 has no non-trivial factors.
      -- problem4(30)  returns 6  because 30 has 6 non-trivial factors,
                                      namely: 2, 3, 5, 6, 10, and 15.
      -- problem4(360) returns 22
            because 360 has 22  non-trivial factors,
            namely:  2,  3,  4,  5,  6,  8,  9, 10, 12, 15, 18, 20, 24, 30,
                    36, 40, 45, 60, 72, 90, 120, and 180.
      -- problem4(97)   returns 0 because 97 has no non-trivial factors
                                 (i.e., it is prime)
    """
    # -------------------------------------------------------------------------
    # DONE: 7. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    total = 0
    for k in range(m-2):
        if m % (k+2) == 0:
            total = total + 1
    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
