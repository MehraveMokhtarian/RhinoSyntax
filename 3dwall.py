
#3D POINT MATRIX CONES
#import modules
import rhinoscriptsyntax as rs
import ran


def PointMatrix(IMAX,JMAX,KMAX):

    #set up empty list
    ptList = []
    ptDict = {}
    
    #loop to generate point values as a product of the loop counter
    #save values in list
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                #define x,y,z in terms of i,j,k
                x = i * 12 
                y = j * 12
                z = k * 12 
                #save point values in dictionary
                point = (x,y,z)
                ptDict[(i,j,k)] = point
                #print out dictionary key:value pairs
                #print (i,j,k,h), ':', point
                #render point in rhinospace
                rs.AddPoint(point)
#    for i in range(IMAX):
#        for j in range(JMAX):
#            for k in range(KMAX):
#                rs.AddTextDot((i,j,k), ptDict[(i,j,k)])
        
    #loop through dictionary to create spheres
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                if i > 0 and j > 0 and k > 0 :
                    ####  CREATE GEOMETRY  ####
                    #CREATE BACK CURVE
                    #middle1 = MidPt(ptDict[(i-1,j,k)],ptDict[(i,j,k)])
                    #middle2 = MidPt(ptDict[(i-1,j-1,k-1)],ptDict[(i,j-1,k-1)])
                    #crvBack = rs.AddCurve((middle1,
                    #ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)], middle1), 1)
                    #crvFront = rs.AddCurve((ptDict[(i,j-1,k)], ptDict[(i-1,j-1,k)],
                    #middle2, ptDict[(i,j-1,k)]), 1)
                    sss = square1 = rs.AddCurve((ptDict[(i,j,k)], ptDict[(i+1,j,k)],ptDict[(i+1,j+1,k)], ptDict[(i,j+1,k)]
                    #SCALE FRONT CURVE WITH FOUND MID POINT
                    #origin = MidPt(ptDict[(i-1,j-1,k-1)], ptDict[(i,j-1,k)])
                    #crvFront = rs.ScaleObject(crvFront, origin, (0.5,0.5,0.5))
                    #randNum = rnd.randint(0,8)*0.1*j
                    #crvFront = rs.MoveObject(sss, (0,0,randNum))
                    #LOFT CURVES TO CREATE CONES
                    rs.AddLoftSrf((sss, crvFront))
                    #CREATE FRONT CIRCLE USING MID POINT AS ORIGIN
                    #rs.AddCircle(origin, 2)
                   
#def MidPt(PT01, PT02):
    
    #clear all data being held in point variable
    point = None
    #calculate mid-point position from input point data
    point = [(PT01[0] + PT02[0]) / 2,(PT01[1] + PT02[1]) / 2,
    (PT01[2] + PT02[2]) / 2,]
    #return mid-point to main() function where MidPt() function was called
    return point
            
def main():
    
    #get values from user
    imax = rs.GetInteger('maximum number x', 12)
    jmax = rs.GetInteger('maximum number y', 2)
    kmax = rs.GetInteger('maximum number z', 12)
    
    #call function
    rs.EnableRedraw(False)
    PointMatrix(imax,jmax,kmax)
    rs.EnableRedraw(True)
    
#call main() function to start program
main()



