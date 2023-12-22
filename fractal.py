import fullcontrol as fc
from math import tau, sin, cos, tan, radians, pi
#import numpy as np

def grow2(currPt, minLength=2, currAng = 90, length=20, splitAngle = 45):
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

# def grow3(currPt, minLength=2, currTheta = 0, currPhi = 0, length=128, splitTheta = 30): # gonna hard code the 3 branches, will make it expandable later
#     steps = [fc.Extruder(on=False),currPt]

#     if length>minLength: # terminates at this angle
#         steps.append(fc.Extruder(on=True))

#         currHStep = sin(radians(currTheta))*length # component of length on xy plane

#         currZStep = cos(radians(currTheta))*length # to determine seed position

#         # rTZ = 
#         # rBZ =  

#         # rTX =
#         # rBX =  

#         # rTY = 
#         # rBY = 

#         # to draw singular line to here, the point where the other branches will seed from
#         steps.append(fc.Point(x=currPt.x + cos(radians(currPhi))*currHStep ,y=currPt.y + sin(radians(currPhi))*currHStep,z=currPt.z + currZStep))

#         newLength = length*0.5 # how much length shrinks by
        

#         # right # does not need phi
#         steps.extend(grow3(fc.Point(x=currPt.x + currHStep * cos(0),y=currPt.y + currHStep * sin(0), z=currPt.z + currZStep), currTheta = currTheta + splitTheta, currPhi = currPhi+0, length=newLength))
    
#         # left top
#         # steps.extend(grow3(fc.Point(x=currPt.x + cos(radians(currPhi-120))*currHStep,y=currPt.y + sin(radians(currPhi-120))*currHStep,z=currPt.z + currZStep), currTheta = currTheta + splitTheta, currPhi = currPhi+120, length=newLength))

#         # left bottom
#         # steps.extend(grow3(fc.Point(x=currPt.x + cos(radians(currPhi+120))*currHStep,y=currPt.y + sin(radians(currPhi+120))*currHStep,z=currPt.z + currZStep), currTheta = currTheta + splitTheta, currPhi = currPhi-120, length=newLength))

#     return steps # steps

# def grow4(currPt, minLength=2, currAng = 90, length=128, splitAngle = 45):
#     steps = [fc.Extruder(on=False),currPt]

#     if length>minLength: # terminates at this angle
#         steps.append(fc.Extruder(on=True))

#         currXStep = cos(radians(currAng))*length
#         currZStep = sin(radians(currAng))*length

#         steps.append(fc.Point(x=currPt.x ,y=currPt.y,z=currPt.z)) # the next seed location

#         newLength = length*0.5
#         leftAngle = currAng + splitAngle/2
#         rightAngle = currAng - splitAngle/2

#         # left
#         steps.extend(grow4(fc.Point(x=currPt.x + currXStep,y=currPt.y,z=currPt.z + currZStep), currAng = leftAngle, length=newLength))
        
#         # right
#         steps.extend(grow4(fc.Point(x=currPt.x + currXStep,y=currPt.y,z=currPt.z + currZStep), currAng = rightAngle, length=newLength))

#         # top
#         steps.extend(grow4(fc.Point(x=currPt.x,y=currPt.y + currXStep,z=currPt.z + currZStep), currAng = rightAngle, length=newLength))

#         # bottom
#         steps.extend(grow4(fc.Point(x=currPt.x,y=currPt.y + currXStep,z=currPt.z + currZStep), currAng = leftAngle, length=newLength))

#     return steps # steps

steps = grow2(fc.Point(x=0,y=0,z=0))
# steps = grow2(fc.Point(x=0,y=0,z=0))
# steps = np.append(steps, fc.PlotAnnotation(steps[0], label="point 1"))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='line'))
