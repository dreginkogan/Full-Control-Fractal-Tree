import fullcontrol as fc
from math import tau, sin, cos, tan, radians
import numpy as np

lh = 0.2 # layer height

# arcs with height change dont rly make sense, might be best to just do circles
def grow(maxlength, minlength, maxangle, segments, maxwidth): #length in mm
    # list of length of each segment, descending
    maxangle = radians(maxangle)
    lengthArr = [minlength+(a/(segments-1))*(maxlength-minlength) for a in range(0, segments)][::-1]
    thicknessArr = [(b/(segments))*maxwidth for b in range(segments+1)][::-1] # length segments + 1
    angleArr = [(c/(segments-1))*maxangle for c in range(segments)]

    print(angleArr)

    steps = [fc.Point(x=0,y=0,z=0)]

    offset = 0
    height = 0
    
    for i in range(len(lengthArr)):
        height += cos(angleArr[i])*lengthArr[i]
        offset += sin(angleArr[i])*lengthArr[i]
        steps = np.append(steps, fc.Point(x=offset,y=0,z=height))
        steps = fc.move_polar(steps, fc.Point(x=offset,y=0,z=height), 0, tau/6, copy=True, copy_quantity=3)
        print(cos(angleArr[i])*lengthArr[i])
        offset+=1

    print(steps)

    # 1) create array of points that make up the fractal tree
    # 2) make each point be the print height above eachother
    # 2) iterate over the list and draw circles around each point
    # for i in range(len(lengthArr)):
    #     steps2 = fc.variable_arcXY(fc.Point(x=(1-cos(angleArr[i]))*lengthArr[i], y=0, z=height), thicknessArr[i], 0, tau*64, 512, thicknessArr[i+1]-thicknessArr[i], lengthArr[i])
    #     height += lengthArr[i]
    #     offset+=1
    #     print(lengthArr[i]-lengthArr[len(lengthArr)-1])
    #     steps = np.append(steps, steps2)



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
steps = grow(20, 5, 45, 3, 4)
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
