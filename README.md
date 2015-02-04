# PolyPy

This small project turns images into their low-poly versions. It is painfully 
slow right now, hopefully there is a way to speed it up a bit in the future.

## Examples

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/lena/lena.jpg)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/lena/lena3.png)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/sf/sf.jpg)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/sf/sf4.jpg)

## To do:

 - Automated calculation of constants
 - Parallel processing (the loop in the `triangulate` function is by far the slowest part)
 - User interface (Qt or console?)
