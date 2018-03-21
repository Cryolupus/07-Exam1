"""
Exam 1, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Kevin Chou.  March 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


def run_test_problem2():
    """ Tests the   problem2   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem2  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 and 2 of problem2'
    window = rg.RoseWindow(400, 250, title)

    # Test 1:
    line = rg.Line(rg.Point(30, 25),
                   rg.Point(80, 200))
    other_line = rg.Line(rg.Point(130, 60),
                         rg.Point(90, 100))
    line.thickness = 5
    line.color = 'forest green'
    other_line.color = 'red'
    problem2(line, other_line, 5, window)

    window.render()  # In case students forget to do so.
    window.continue_on_mouse_click()

    # Test 2:
    line = rg.Line(rg.Point(350, 100),
                   rg.Point(300, 250))
    other_line = rg.Line(rg.Point(250, 20),
                         rg.Point(375, 100))
    line.thickness = 1
    other_line.thickness = 5
    line.color = 'blue'
    other_line.color = 'black'
    problem2(line, other_line, 3, window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem2'
    window = rg.RoseWindow(300, 300, title)

    # Test 3:
    line = rg.Line(rg.Point(100, 50),
                   rg.Point(200, 50))
    other_line = rg.Line(rg.Point(50, 200),
                         rg.Point(200, 200))
    line.thickness = 8
    other_line.thickness = 2
    line.color = 'magenta'
    other_line.color = 'black'
    problem2(line, other_line, 8, window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()


###############################################################################
#
# IMPORTANT:  In the following problem:
#   -- Write ONLY the code for Step 1 of the Side Effects below.
#        TEST and get it correct.
#   -- Then add ONLY the code for Step 2 of the Side Effects below.
#        TEST and get it correct.
#   -- Etc. for Steps 3 and 4, ** ONE AT A TIME. **
#
###############################################################################
def problem2(line1, line2, thickness, win):
    """
    See   problem2_pictures.pdf   for pictures that may help you
    better understand the following specification:

    What comes in:
      -- Two rg.Line objects.
      -- A positive integer
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e
    Side effects:., None).


      1. Draws the given rg.Line objects (line1 and line2)
           on the given rg.RoseWindow.

      2. Draws an rg.Rectangle such that [SEE THE PDF for a helpful picture]:
           -- one corner is the midpoint of line1
           -- the other corner is the midpoint of line2

      3.   Where the outline thickness of the rg.Rectangle is the given
             thickness,

      4.   And its outline color is the same as the color of line1.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type line1:      rg.Line
      :type line2:      rg.Line
      :type thickness:  int
      :type win:        rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function, TESTING each step as you go.
    #          Tests have been written for you (above).
    #   See the IMPORTANT NOTE just above the DEF line above.
    # -------------------------------------------------------------------------
    line1.attach_to(win)
    line2.attach_to(win)
    korner1 = line1.get_midpoint()
    korner2 = line2.get_midpoint()
    rect1 = rg.Rectangle(korner1, korner2)
    rect1.outline_thickness = thickness
    rect1.outline_color = line1.color
    rect1.attach_to(win)

    win.render()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()
