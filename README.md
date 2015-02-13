# PolyPy

This small project turns images into their low-poly versions. 

## Requirements

All of these should be installable via `pip`.

 - [Pillow](https://pypi.python.org/pypi/Pillow/)

 - [SciPy](http://www.scipy.org)

Pillow is used as a general-purpose imaging library (image manipulation, 
filters, drawing). SciPy hosts the Delauay triangulation algorithm used to 
generate the final polygons.

## Usage

	python poly.py examples/lena/lena.jpg

To change the internal settings related to the image generation, the code must 
be edited. Here is a quick overview of the available constants to modify:

|   Constant name    | Description | Default value |
| ------------------ | ------------------------------------------------------------------------------------ | ---- |
| POINT_COUNT        | Number of points to generate for the triangles                                       | 150  |
| EDGE_THRESHOLD     | Grayscale RGB value needed for a pixel to be considered as an edge                   | 172  |
| EDGE_RATIO         | Ratio of edges pixels/generated pixels on the edges                                  | 0.98 |
| DARKENING_FACTOR   | Factor for the maximum possible darkening of pixels in the final step                | 35   |
| SPEEDUP_FACTOR_X   | Number of rows to skip when browsing the image for the mean color of a triangle      | 1    |
| SPEEDUP_FACTOR_Y   | Number of columns to skip when browsing the image for the mean color of a triangle   | 1    |
| CONCURRENCY_FACTOR | Number of processes to run concurrently when collecting the pixels inside a triangle | 3    |

## Examples

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/lena/lena.jpg)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/lena/lena3.png)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/sf/sf.jpg)

![](https://raw.githubusercontent.com/louis-paul/polypy/master/examples/sf/sf4.jpg)

## To do

 - Automated calculation of constants

 - User interface. This work has been started (the current QML interface can be found in qt/), but qt5 + python3 don't seem to have any good bindings.
