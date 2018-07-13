"""
This is a sample program to show how to draw using functions
"""

import arcade


def draw_grass():
    """
    This function draws the grass.
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

def draw_pine_tree():
    """
    This function draws a pine tree.
    """

    # Draw the trunk
    # (center_x, center_y, width, height, colour)
    arcade.draw_rectangle_filled(100, 200, 30, 80, arcade.color.BROWN)

    # Draw three levels of triangles
    # (x1, y1, x2, y2, x3, y3, colour)
    arcade.draw_triangle_filled(50, 215, 150, 215, 100, 320, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(50, 255, 150, 255, 100, 360, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(60, 295, 140, 295, 100, 400, arcade.color.FOREST_GREEN)

arcade.open_window(800, 600, "Drawing with Functions")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Call our function to draw the grass
draw_grass()
draw_pine_tree()

arcade.finish_render()
arcade.run()