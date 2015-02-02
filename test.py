import colorsys
from itertools import product
from PIL import Image, ImageDraw, ImageFilter
import random
from scipy.spatial import Delaunay
import sys

POINTS_COUNT = 600
POINT_PROPAGATION = 500
POINT_DISTANCE = 100
BLUR_RADIUS = 0.15
EDGE_THRESHOLD = 172
EDGE_RATIO = .98
DARKENING_FACTOR = 35

if len(sys.argv) != 2 or not sys.argv[1]:
    print("Please provide the name of the file to process as an argument")
    exit()

im = Image.open(sys.argv[1])
im_edges = im.filter(ImageFilter.GaussianBlur(BLUR_RADIUS))
im_edges = im_edges.filter(ImageFilter.FIND_EDGES)
(size_x, size_y) = im.size

# Point generation
points = []
# Random points
for _ in range(POINTS_COUNT):
    x = random.randrange(round((size_x + POINT_PROPAGATION) / POINT_DISTANCE)) \
        * POINT_DISTANCE - (POINT_PROPAGATION / 2)
    y = random.randrange(round((size_y + POINT_PROPAGATION) / POINT_DISTANCE)) \
        * POINT_DISTANCE - (POINT_PROPAGATION / 2)
    points.append([x, y])
# Edge points
for x, y in product(range(size_x), range(size_y)):
    (r, g, b) = im_edges.getpixel((x, y))
    if (0.2126*r + 0.7152*g + 0.0722*b) > EDGE_THRESHOLD and \
            random.random() > EDGE_RATIO:
        points.append([x, y])

# Delaunay triangulation and color calculation
tri = Delaunay(points)
colors = [None] * len(tri.simplices)
for x, y in product(range(size_x - 1), range(size_y - 1)):
    t = tri.find_simplex((x, y)).flat[0]
    if not ~t:
        continue
    if not colors[t]:
        colors[t] = []
    colors[t].append(im.getpixel((x, y)))

# Color averaging, correction and drawing
draw = ImageDraw.Draw(im)
for t, t_colors in enumerate(colors):
    end_color = (0, 0, 0)
    if t_colors:
        avg = [round(sum(y) / len(y)) for y in zip(*t_colors)]
        # Random darkening of the triangles
        (h, s, v) = colorsys.rgb_to_hsv(avg[0], avg[1], avg[2])
        end_color = colorsys.hsv_to_rgb(h, s, v - random.random() *
                                        DARKENING_FACTOR)
        end_color = tuple(map(lambda x: round(x), end_color))
    draw.polygon([tuple(points[y]) for y in tri.simplices[t]], fill=end_color)

im.save("result.png", "png")
