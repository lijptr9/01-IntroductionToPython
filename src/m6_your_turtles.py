"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ji Li.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()


cortana = rg.SimpleTurtle('turtle')
cortana.pen = rg.Pen('blue', 4)
cortana.speed = 20
size = 180
for k in range (10):
    cortana.draw_circle(size)
    cortana.pen_up()
    cortana.right(36)
    cortana.forward(10)
    cortana.right(36)
    cortana.pen_down()
    size = size - 10

siri = rg.SimpleTurtle('turtle')
siri.pen = rg.Pen('red', 4)
siri.speed = 20
size2 = 180
for m in range (10):
    siri.draw_square(size2)
    siri.pen_up()
    siri.left(36)
    siri.forward(10)
    siri.left(36)
    siri.pen_down()
    size2 = size2 - 10

window.close_on_mouse_click()

