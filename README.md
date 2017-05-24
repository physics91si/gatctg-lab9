# Lab 9 Comments

## particle.py
* Good docstrings

## quadratic.py
* Looks like you're trying to do a lot of good error checking inside your find_roots() function. However, no matter the input that you enter, a call to quadratic.py only returns 2 lines of "Please enter 3 numbers representing the polynomial coefficients" (1 comes from the except statement in main() and the other from the except statement in find_roots())

* The error might lie in the call to find_roots() in main. Note that you never call find_roots() with any "extra" parameters.

* Good effort overall though!