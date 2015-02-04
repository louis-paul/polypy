import colorsys
from itertools import product
from PIL import Image, ImageDraw, ImageFilter
import random
from scipy.spatial import Delaunay
import sys

POINTS_COUNT = 150
POINT_PROPAGATION_X = -1  # Generated later based on the width of the image
POINT_PROPAGATION_Y = -1  # Generated later based on the height of the image
POINT_DISTANCE = -1  # Generated later
EDGE_THRESHOLD = 172
EDGE_RATIO = .98
DARKENING_FACTOR = 35


def main():
    global POINT_PROPAGATION_X
    global POINT_PROPAGATION_Y
    global POINT_DISTANCE

    if len(sys.argv) != 2 or not sys.argv[1]:
        print("Please provide the name of the file to process as an argument")
        exit()

    im = Image.open(sys.argv[1])
    POINT_PROPAGATION_X = im.size[0] / 4
    POINT_PROPAGATION_Y = im.size[1] / 4
    POINT_DISTANCE = min(im.size[0], im.size[1]) / 16

    # Random point generation
    points = []
    generate_random(im, points)
    # Generation of "interesting" points
    generate_edges(im, points)
    # Triangulation and color listing
    triangles, colors = triangulate(im, points)
    # Final color calculation and drawing
    draw(im, points, triangles, colors)

    im.save("result.jpg", "jpeg", quality=95)


# generate_random places semi-random point in a list
def generate_random(im, points):
    for _ in range(POINTS_COUNT):
        x = random.randrange(round(
            (im.size[0] + POINT_PROPAGATION_X) / POINT_DISTANCE
            )) * POINT_DISTANCE - (POINT_PROPAGATION_X / 2)
        y = random.randrange(round(
            (im.size[1] + POINT_PROPAGATION_Y) / POINT_DISTANCE
            )) * POINT_DISTANCE - (POINT_PROPAGATION_Y / 2)
        points.append([x, y])


# generate_edges generates semi-random points in a list, based on an image that
# was applied an matrix for edge detection
def generate_edges(im, points):
    im_edges = im.filter(ImageFilter.SHARPEN).filter(ImageFilter.FIND_EDGES)
    for x, y in product(range(im.size[0]), range(im.size[1])):
        (r, g, b) = im_edges.getpixel((x, y))
        if (0.2126*r + 0.7152*g + 0.0722*b) > EDGE_THRESHOLD and \
                random.random() > EDGE_RATIO:
            points.append([x, y])


# triangulate generates triangles between points and the list of the colors of
# the pixels containes within
def triangulate(im, points):
    triangles = Delaunay(points)
    colors = [None] * len(triangles.simplices)
    for x, y in product(range(im.size[0] - 1), range(im.size[1] - 1)):
        t = triangles.find_simplex((x, y)).flat[0]
        if not ~t:
            continue
        if not colors[t]:
            colors[t] = []
        colors[t].append(im.getpixel((x, y)))
    return (triangles, colors)


# draw draws triangles on an existing image using the average colors of the
# pixels contained within them and a random darkening
def draw(im, points, triangles, colors):
    d = ImageDraw.Draw(im)
    for t, t_colors in enumerate(colors):
        end = (0, 0, 0)
        if t_colors:
            avg = [round(sum(y) / len(y)) for y in zip(*t_colors)]
            # Random darkening of the triangles
            (h, s, v) = colorsys.rgb_to_hsv(avg[0], avg[1], avg[2])
            end = colorsys.hsv_to_rgb(h,
                                      s,
                                      v - random.random() * DARKENING_FACTOR)
        d.polygon(
            [tuple(points[y]) for y in triangles.simplices[t]],
            fill=tuple(map(lambda x: round(x), end))
        )


if __name__ == "__main__":
    sys.exit(main())
