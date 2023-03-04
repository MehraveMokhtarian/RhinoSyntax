

import rhinoscriptsyntax as rs

###input plan
#plan = rs.GetObject('select a circle', rs.filter.curve)
#
#for i in range(1,7):
#    plan = rs.CopyObject(plan, (0,0,1.7*i+16/i))
#    centroid = rs.CurveAreaCentroid(plan)[0]
#    plan = rs.ScaleObject(plan, centroid, (0.7,0.7,0.7))
##loft_circles

#SURFACE POINTS
def SurfacePoints(STRSRF, INTU, INTV):
#    create empty dictionary
    ptMTX = {}
    
#    find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
#    print domain values
    print 'Udomain: ', Udomain
    print 'Vdomain: ', Vdomain
    
#    calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
#    print step values
    print 'stepU: ', stepU
    print 'stepV: ', stepV
    
#    PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
#            define u and v in terms of step values and i and j
            u = Udomain[0] + stepU * i
            v = Vdomain[0] + stepV * j
            
#            evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
#    #LABEL POINTS ON SURFACE WITH (i,j) KEYS
#    for i in range(INTU+1):
#        for j in range(INTV+1):
#            rs.AddTextDot((i,j),ptMTX[(i,j)])
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                crv1 = rs.AddCurve((ptMTX[(i-1,j-1)], ptMTX[(i,j-1)], 
                ptMTX[(i+1,j)], ptMTX[(i,j)], ptMTX[(i-1,j-1)] ),1)
                crv2 = rs.AddCurve((ptMTX[(i-1,j)], ptMTX[(i,j)], 
                ptMTX[(i+1,j-1)], ptMTX[(i,j-1)], ptMTX[(i-1,j)]),1)
#                rs.AddLoftSrf((crv1, crv2))
                rs.AddPipe(crv1, 0, .3)
                rs.AddPipe(crv2, 0, 0.3)

                
def main():
#    collect data
    strSRF = rs.GetObject('select surface', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 10)
    intV = rs.GetInteger('how many V intervals?', 10)
    rs.HideObject(strSRF)
#    call function
    rs.EnableRedraw(False)
    SurfacePoints(strSRF, intU, intV)
    rs.EnableRedraw(True)
    
main()
