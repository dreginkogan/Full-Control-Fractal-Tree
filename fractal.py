import fullcontrol as fc
from math import tau, sin
import numpy as np

def grow(maxlength, minlength, maxangle, segments, maxwidth): #length in mm
    # list of length of each segment, descending
    lengthArr = [minlength+(a/(segments-1))*(maxlength-minlength) for a in range(0, segments)][::-1]
    thicknessArr = [(b/(segments))*maxwidth for b in range(0, segments+1)][::-1] # length segments + 1

    print(thicknessArr)

    steps = []

    height = 0
    for i in range(len(lengthArr)):
        steps2 = fc.variable_arcXY(fc.Point(x=0, y=0, z=height), thicknessArr[i], 0, tau*64, 512, thicknessArr[i+1]-thicknessArr[i], lengthArr[i])
        height += lengthArr[i]
        print(lengthArr[i]-lengthArr[len(lengthArr)-1])
        steps = np.append(steps, steps2)

    return steps

# pt1 = fc.Point(x=0,y=0,z=0)
# pt2 = fc.Point(x=0,y=20,z=0)
# pt3 = fc.polar_to_point(pt2, -10, tau/8)
# pt4 = fc.midpoint(pt1, pt2)
# steps = [pt1, pt2, pt3, pt4]
# steps.append(fc.PlotAnnotation(point=pt4, label="midpoint between point 1 and point 2"))
# steps.append(fc.PlotAnnotation(point=pt1, label="point 1"))
# steps.append(fc.PlotAnnotation(point=pt2, label="point 2"))
# steps.append(fc.PlotAnnotation(point=pt3, label="point defined by polar coordinates relative to point 2"))
steps = grow(20, 5, 45, 4, 4)
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
