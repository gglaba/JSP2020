import colorsys
def konwerter(r,g,b):
    print(colorsys.rgb_to_hsv(r/255,g/255,b/255))
konwerter(128,78,140)