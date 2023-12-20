import fullcontrol as fc
from math import tau, sin, cos, tan, radians, pi
#import numpy as np

def grow2(currPt, minLength=2, currAng = 90, length=20, splitAngle = 30):
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

def grow3(currPt, minLength=2, currTheta = 0, currPhi = 0, length=20, splitTheta = 15):
    steps = [fc.Extruder(on=False),currPt]

    if length>minLength: # terminates at this angle
        steps.append(fc.Extruder(on=True))

        currHStep = sin(radians(currAng))*length 
        currZStep = cos(radians(currAng))*length

        steps.append(fc.Point(x=currPt.x + cos(radians(currPhi))*currHStep,y=currPt.y + cos(radians(currPhi))*currHStep,z=currPt.z + currZStep))

        newLength = length*0.75
        leftAngle = currAng + splitAngle/2
        rightAngle = currAng - splitAngle/2

        # left
        steps.extend(grow2(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep), currAng = leftAngle, length=newLength))
        
        # right top
        steps.extend(grow2(fc.Point(=currPt.x + cos(radians(currPhi))*currHStep,y=currPt.y + cos(radians(currPhi))*currHStep,z=currPt.z + currZStep), currAng = rightAngle, length=newLength))

    return steps # steps

steps = grow2(fc.Point(x=0,y=0,z=0))
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
