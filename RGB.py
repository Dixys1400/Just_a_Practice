
colors = {
'black': (0, 0, 0),
'white': (255, 255, 255),
'red': (255, 0, 0),
'blue': (0, 42, 255),
'violet': (140, 0, 255),
'orange': (255, 153, 0),
'yellow': (255, 242, 0)
}


color_name = input("Write the color name: black, white, red, blue, violet, orange, yellow")
if color_name in colors:
    rgb_code = colors[color_name]
    print("RGB code of", color_name, "is", rgb_code)
else:
    print("Color ot found")
