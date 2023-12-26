import fullcontrol as fc
from math import tau, sin, cos, tan, radians, pi
#import numpy as np

def grow2(currPt, minLength=2, currAng = 90, length=20, splitAngle = 45):
    steps = [fc.Extruder(on=False),currPt]

    if length>minLength: # terminates at this angle
        steps.append(fc.Extruder(on=True))

        currXStep = cos(radians(currAng))*length
        currZStep = sin(radians(currAng))*length

        steps.append(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep)) # shouldnt have to add offsets to this

        newLength = length*0.75
        leftAngle = currAng + splitAngle/2
        rightAngle = currAng - splitAngle/2

        # left
        steps.extend(grow2(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep), currAng = leftAngle, length=newLength))
        
        # right
        steps.extend(grow2(fc.Point(x=currPt.x + currXStep,y=0,z=currPt.z + currZStep), currAng = rightAngle, length=newLength))

    return steps # steps


## needs to be written with relative spherical coordinates
def grow4(currPt, minLength=2, theta = 0, phi = 0, length=128, splitAngle = 60):# each axis alone works, but together it fucks up
    # issue is probably with going to the proper base location

    steps = [currPt, fc.Extruder(on=False)]

    if length>minLength: # terminates at this angle 
        steps.append(fc.Extruder(on=True))

        currXStep = sin(radians(theta))*cos(radians(phi))*length
        currYStep = sin(radians(theta))*sin(radians(phi))*length
        currZStep = cos(radians(theta))*length

        newLength = length*0.5

        # leftPitch = currPitch - splitAngle/2
        # rightPitch = currPitch + splitAngle/2

        # botRoll = currRoll - splitAngle/2
        # topRoll = currRoll + splitAngle/2

        # left
        steps.extend(grow4(fc.Point(x=currPt.x + currXStep,y=currPt.y + currYStep,z=currPt.z + currZStep), theta = theta-splitAngle/2*cos(radians(theta)), phi = 0, length=newLength))
        # right
        steps.extend(grow4(fc.Point(x=currPt.x + currXStep,y=currPt.y + currYStep,z=currPt.z + currZStep), theta = theta+splitAngle/2*cos(radians(theta)), phi = 0, length=newLength))
        # top
        # steps.extend(grow4(fc.Point(x=currPt.x,y=currPt.y + currYStep,z=currPt.z + currZStep), currRoll = topRoll, length=newLength))
        # bottom
        # steps.extend(grow4(fc.Point(x=currPt.x,y=currPt.y + currYStep,z=currPt.z + currZStep), currRoll = botRoll, length=newLength))

        steps.append(fc.Point(x=currPt.x,y=currPt.y,z=currPt.z)) # go back to origin

    return steps # steps

steps = grow4(fc.Point(x=0,y=0,z=0), theta = 0, phi = 0)
# steps = grow2(fc.Point(x=0,y=0,z=0))
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
