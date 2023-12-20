import fullcontrol as fc
from math import tau, sin, cos, tan, radians, pi
#import numpy as np

def circleChain(startPt, endPt, layerHeight): # takes two points, draws circles between them every z of layer height
    # do a try except thing if the layer height is not compatible with the thing idk, or maybe
    pass

# would need different algorithm to make it printable, so it prints sequentilaly from lowest to highest. alternatively, just 
# recursively generating the 3D model and then slicing that would be better
def grow2(currPt, minLength=2, currAng = 90, currHorAng = 0, length=20, splitAngle = 30):
    steps = [fc.Extruder(on=False),currPt]

    if length>minLength: # terminates at this angle
        steps.append(fc.Extruder(on=True))

        currXStep = cos(radians(currAng))*length
        currZStep = sin(radians(currAng))*length

        steps.append(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep))

        newLength = length*0.75
        leftAngle = currAng + splitAngle/2
        rightAngle = currAng - splitAngle/2

        # left
        steps.extend(grow2(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep), currAng = leftAngle, length=newLength))
        
        # right
        steps.extend(grow2(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep), currAng = rightAngle, length=newLength))

    return steps # steps


# arcs with height change dont rly make sense, might be best to just do circles
def grow(maxlength, minlength, maxangle, segments, maxwidth): #length in mm
    # list of length of each segment, descending
    maxangle = radians(maxangle)
    lengthArr = [minlength+(a/(segments-1))*(maxlength-minlength) for a in range(segments)][::-1]
    thicknessArr = [(b/(segments))*maxwidth for b in range(segments+1)][::-1] # length segments + 1
    angleArr = [(c/(segments-1))*maxangle for c in range(segments)]

    print(angleArr)

    trunk = [fc.Point(x=0,y=0,z=0), fc.Point(x=0,y=0,z=lengthArr[0])]

    steps = []

    offset = 0
    height = lengthArr[0]
    
    for i in range(len(lengthArr)):
        steps.append(fc.Extruder(on=True))
        height += cos(angleArr[i])*lengthArr[i]
        offset += sin(angleArr[i])*lengthArr[i]
        steps.append(fc.Point(x=offset,y=0,z=height))
        steps.append(fc.Extruder(on=False))
        steps.extend(fc.move_polar(steps, fc.Point(x=0,y=0,z=0), 0, tau/3, copy=True, copy_quantity=3))
        print(cos(angleArr[i])*lengthArr[i])

    trunk.extend(steps)

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



    return trunk

steps = grow2(fc.Point(x=0,y=0,z=0))
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
