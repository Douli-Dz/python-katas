"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Example:
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).
"""
#solve it in recursive way

def bouncingBall(h, bounce, window):
    if(h>0 and (0<bounce<1) and (window<h)):
      return 2 + bouncingBall(bounce*h,bounce,window)
    else:
        return -1

"""
-- best solution:
def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return 2 + bouncingBall(h * bounce, bounce, window)

def bouncingBall(h, bounce, window):
    count = -1
    if h>0 and 0<bounce<1 and 0<window<h :
        while h > window:
            h = h*bounce
            count += 2
    return count

---------TOP SOLUTION---------

# The height of the ball after bouncing can be expressed as an exponential function:
#
# f(x) = h * bounce^x
# f(x) is the height the ball reaches after x bounces
# h is initial height
# bounce is the decay factor
#
# By solving the equation f(x) = window, we get the number of 
# bounces that will finally put the ball at the exact window height.
#
# Example:
# f(x) = 3 * 0.66^x
# f(x) = 1.5  -->  x ~= 1.67
# So the first bounce will put the ball a bit above window height,
# but the second will put it a bit below.
# This means the ball will pass the window 2 times (one bounce).
#
# If a bounce puts the ball at the exact window height (an exact 
# number of bounces, x is an integer), this would mean the ball 
# won't pass the window, only appear in front of it.
# However, due to the restriction in this assignment, the ball
# can only be seen if it's height is _strictly_ greater than the 
# window height.

import math

def bouncingBall(h, bounce, window):
    # If parameters don't fulfil conditions, return -1
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    # Solve equation for f(x) = window, using logarithms
    bounces = math.log(window / h, bounce)
    # Get actual number of bounces that still puts the ball above window height
    exactBounces = math.floor(bounces)
    # If last bounce is not strictly higher than window height, it can't be seen
    if bounces == exactBounces: 
        exactBounces -= 1
    # The ball will pass the window two times for each bounce, up and down, 
    # plus one for the initial drop past window, before first bounce
    passes = exactBounces * 2 + 1
    return passes

"""
