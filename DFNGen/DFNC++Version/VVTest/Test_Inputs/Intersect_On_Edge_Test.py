import os

main_input= '''
//==============================================================================
//Gereral Options & Fracture Network Parameters: 

stopCondition: 0
    /* 0: stop once nPoly fractures are accepted (Defined below)
       1: stop once all family's p32 values are equal or greater than the families
                   target p32 values (defined in stochastic family sections)
    */             

nPoly: 100
     /* Used when stopCondition = 0
        Total number of fractures you would like to have 
        in the domain you defined. The program will complete 
        once you have nPoly number of fractures, 
        maxPoly number of polygon/fracture rejections, 
        rejPoly number of rejections in a row, or reach a 
        specified fracture cluster size if using 
        stoppingParameter = -largestSize  */


outputAllRadii: 0  
/* 0: Do not output all radii file.
   1: Include file of all raddii (acepted+rejected fractures)
      in output files.
*/
                      

domainSize: {5,5,5} 
     /* Mandatory Parameter.
        Creates a domain with dimension x*y*z centered at the origin.*/

numOfLayers: 0    //number of layers


layers: 
{-500,0}
{0,500}

/*  Layers need to be listed line by line
    Format: {minZ, maxZ}
    
    The first layer listed is layer 1, the second is layer 2, etc
    Stochastic families can be assigned to theses layers (see stochastic
    shape familiy section) 
*/   


h: %f 
  /* Minimum fracture length scale(meters)
    Any fracture with a feature, such as and intersection, of less than h will be rejected. */

   
//==========================================================================//
/* Fracture Network Parameters:                                             */

tripleIntersections: 1
/* Options:     0: Off
                1: On    */

multipleClusters: 1 
/* Options:    0: Keep only largest cluster
               1: Keep all clusters */
                
printRejectReasons: 0
/* Useful for debugging, 
   This option will print all fracture rejection reasons as they occur.
        0: disable
        1: print all rejection reasons to screen
*/

disableFram: 0

visualizationMode: 1
/* Options: 0 or 1 
   Used during meshing: 
   0: creates a fine mesh, according to h parameter;
   1: produce only first round of triangulations. In this case no 
   modeling of flow and transport is possible. */ 

seed: 92731535
    //Seed for random generator. 
        

domainSizeIncrease: {3,3,3} 
          //temporary size increase for inserting fracture centers outside domain
          //increases the entire width by this ammount. So, {1,1,1} will increase
          //the domain by adding .5 to the +x, and subbtracting .5 to the -x, etc


keepOnlyLargestCluster: 0
    /* 0 = Keep any clusters which connects the specified 
           boundary faces in boundaryFaces option below
       
       1 = Keep only the largest cluster which connects 
           the specified boundary faces in boundaryFaces option below
    */

ignoreBoundaryFaces: 1  
/*
     0 = use boundaryFaces option below 

     1 = ignore boundaryFaces option and keep all clusters and
     will still remove fractures with no intersections               
*/
     
          
boundaryFaces: {1,1,1,1,1,1}
/*  DFN will only keep clusters with connections to domain boundaries which are set to 1:

    boundaryFaces[0] = +X domain boundary
    boundaryFaces[1] = -X domain boundary
    boundaryFaces[2] = +Y domain boundary
    boundaryFaces[3] = -Y domain boundary
    boundaryFaces[4] = +Z domain boundary
    boundaryFaces[5] = -Z domain boundary    
    
    Be sure to set ignoreBoundaryFaces to 0 when using this feature.     
*/
                          

rejectsPerFracture: 10  /*If fracture is rejected, it will be re-translated to a new
                         position this number of times. 
                         
                         This helps hit distribution targets for stochastic families 
                         (Set to 1 to ignore this feature)    */





//===========================================================================
//                  Shape and Probability Parameters
//===========================================================================

//user rectangles and user Ellipses defined in their cooresponding files

famProb: {.5, .5} 
/* Probability of occurrence of each family of randomly distrubuted rectangles
   and ellipses.
   User-ellipses and user-rectangles insertion will be attempted with 100 
   likelihood, but with possability they may be rejected.
   The famProb elements should add up to 1.0 (for 100).
   The probabilities are listed in order of families starting with all stochastic
   ellipses, and then all stochastic rectangles.
   
   For example: 
        If  then there are two ellipse families, each with probabiliy .3, 
        and two rectangle families, each with probabiliy .2, famProb will be:
        famProb: {.3,.3,.2,.2} Notice: famProb elements add to 1         
*/
 
 
insertUserRectanglesFirst: 1
 /*
    1: User rectangles will be inserted first
    0: User ellipses will be inserted first
 */
 
/*===========================================================================*/
//===========================================================================
//                      Elliptical Fracture Options                                     
//      NOTE: Number of elements must match number of ellipse families  
//            (first number in nShape input parameter)                         
//===========================================================================
/*===========================================================================*/

//Number of ellipse families
nFamEll: 0
    //Having this option = 0 will ignore all rectangle family variables

eLayer: {0,0}
    /* Defines which domain the family belings to.
     Layer 0 is the entire domain.
     Layers numbered > 0 coorespond to layers defined above
     1 corresponts to the first layer listed, 2 is the next layer listed, etc */

//edist is a mandatory parameter if using statistically generated ellipses 
edistr: {2,3}   /* Ellipse statistical distribution options:
                      1 - lognormal distribution
                      2 - truncated power law distribution   
                      3 - exponential distribution
                      4 - constant */
                                                                                       
                      
ebetaDistribution: {0,0}   /* Beta is the rotation around the polygon's normal
                    vector, with the polygon centered on x-y plane at the orgin 
                    
                    0 - uniform distribution [0, 2PI]    
                    1 - constant angle (specefied below by "ebeta")    */                
    
    
e_p32Targets: {.1,.1} 
/* Elliptical families target fracture intensity per family.
When using stopCondition = 1 (defined at the top of the input file), families will 
be inserted untill the families desired fracture intensity has been reached. 
Once all families desired fracture intensity has been met, fracture generation will 
be complete.
*/                      
                      
//===========================================================================
// Parameters used by all stochastic ellipse families 
// Mandatory Parameters if using statistically generated ellipses  

easpect: {1,1}  /* Aspect ratio. Used for lognormal and truncated 
                    power law distribution. */

enumPoints: {8, 12} /*Number of vertices used in creating each elliptical 
                           fracture family. Number of elements must match number 
                           of ellipse families (first number in nShape) */

eAngleOption: 0     /* All angles for ellipses: 
                       0 - degrees
                       1 - radians (Must use numerical value for PI) */
                        
etheta: {0, 45,} /*Ellipse fracture orientation.
                     The angle the normal vector makes with the z-axis */

ephi: {0,0}   /* Ellipse fracture orientation.
                    The angle the projection of the normal onto the x-y plane
                    makes with the x-axis */

ebeta: {0, 0)   /* rotation around the normal vector */


ekappa: {8,8}  /*Parameter for the fisher distribnShaprutions. The bigger, the more 
                        similar (less diverging) are the elliptical familiy's
                        normal vectors */                

//===========================================================================
// Options Specific For Ellipse Lognormal Distribution (edistr=1): 
// Mandatory Parameters if using ellispes with lognormal distribution 

//          NOTE: Number of elements must match number of
//                ellipse families (first number in nShape)

eLogMean: {2}  //Mean value For Lognormal Distribution.       
               

esd: {.5} // Standard deviation for lognormal distributions of ellipses

eLogMin: {1}

eLogMax: {15}

//===========================================================================
//     Options Specific For Ellipse Exponential Distribution (edistr=3): 
//     Mandatory Parameters if using ellispes with exponential distribution 


eExpMean: {2}  //Mean value for Exponential  Distribution     

eExpMin: {1}

eExpMax: {5}

//===========================================================================
//    Options Specific For Constant Size of ellipses (edistr=4):

econst: {10, 10, 10}  // Constant radius, defined per family     
               
//===========================================================================
// Options Specific For Ellipse Truncated Power-Law Distribution (edistr=2)
// Mandatory Parameters if using ellipses with truncated power-law dist. 

// NOTE: Number of elements must match number 
//       of ellipse families (first number in nShape)

emin: {1} // Minimum radius for each ellipse family. 
             // For power law distributions. 

emax: {6}  // Maximum radius for each ellipse family.
                  // For power law distributions. 
                    
ealpha: {2.4} // Alpha. Used in truncated power-law 
                        // distribution calculation


/*==================================================================================*/
/*==================================================================================*/
/*                             Rctangular Fractures Options                         */
/* NOTE: Number of elements must match number of rectangle families                 */
/*       (second number in nShape parameter)                                        */
/*==================================================================================*/
/*==================================================================================*/

//Number of rectangle families
nFamRect: 0
    //Having this option = 0 will ignore all rectangle family variables


rLayer: {0,0}
    /* Defines which domain the family belings to.
     Layer 0 is the entire domain.
     Layers numbered > 0 coorespond to layers defined above
     1 corresponts to the first layer listed, 2 is the next layer listed, etc */


/*rdist is a mandatory parameter if using statistically generated rectangles */
rdistr: {2,3}   /*  Rectangle statistical distribution options:
                        1 - lognormal distribution
                        2 - truncated power law distribution 
                        3 - exponential distribution
                        4 - constant */

rbetaDistribution: {1,1}   /* Beta is the rotation/twist about the z axis
                    with the polygon centered on x-y plane at the orgin 
                    before rotation into 3d space
                    
                    0 - uniform distribution [0, 2PI]    
                    1 - constant angle (specefied below by "rbeta")
                    
                */                                                 
                
r_p32Targets: {.1,.1} 
/* Rectangle families target fracture intensity per family.
When using stopCondition = 1 (defined at the top of the input file), families will 
be inserted untill the families desired fracture intensity has been reached. 
Once all families desired fracture intensity has been met, fracture generation will 
be complete.
*/      
                 
//============================================================================ 
// Parameters used by all stochastic rectangle families 
// Mandatory Parameters if using statistically generated rectangles   

raspect: {1,1}  /* Aspect ratio */
 
rAngleOption: 0     /* All angles for rectangles: 
                       0 - degrees
                       1 - radians (must be numerical value, cannot use "Pi") */
 
rtheta: {90,45} /*Rectangle fracture orientation.
                          The angle the normal vector makes with the z-axis */

rphi: {0,45} /* Rectangle fracture orientation.
                The angle the projection of the normal onto the x-y
                plane makes with the x-axis */
      
rbeta: {0,0)   /* rotation around the normal vector */

rkappa: {8,8}  /*Parameter for the fisher distributions. The bigger, 
                              the more similar (less diverging) are the rectangle 
                              familiy's normal vectors  */

//=============================================================================
// Options Specific For Rectangle Lognormal Distribution (rdistr=1):
// Mandatory Parameters if using rectangles with lognormal distribution 

rLogMean: {1.6}   /*For Lognormal Distribution. 
                    Mean radius (1/2 rectangle length) in 
                    lognormal distribution for rectangles. */
                   

rsd: {.4}     /* Standard deviation for lognormal distributions of 
                      rectangles */
                      
rLogMin: {2}

rLogMax: {10}                      

//=============================================================================
// Options Specific For Rectangle Truncated Power-Law Distribution (rdistr=2): 
// Mandatory Parameters if using rectangles with power-law distribution 

 rmin: {1,1}         /* Minimum radius for each rectangle family. 
                                 For power law distributions. */

 rmax: {6,5}   /* Maximum radius for each rectangle family.
                          For power law distributions. */

 ralpha: {2.4,2.5}   // Alpha. Used in truncated power-law 
                     // distribution calculation


/*===========================================================================*/
/* Options Specific For Rectangle Exponential Distribution (edistr=3):       */
/* Mandatory Parameters if using rectangules with exponential distribution   */

rExpMean: {2}  //Mean value for Exponential  Distribution

rExpMin: {1}

rExpMax: {10}

/*===========================================================================*/
/* Options Specific For Constant Size of rectangles (edistr=4):              */

rconst: {4,4}  // Constant radius, defined per rectangular family       
               
/*===========================================================================*/
/*===========================================================================*/
/* User-Specified Ellipses                                                   */
/* Mandatory Parameters if using user-ellipses                               */
/* NOTE: Number of elements must match number of user-ellipse families       */
/*(third number in nShape parameter)                                         */
/*===========================================================================*/
/* NOTE: Only one user-ellipse is placed into the domain per defined 
         user-ellipse, with possibility of being rejected  */

   
userEllipsesOnOff: 0    //0 - User Ellipses off
                        //1 - User Ellipses on

UserEll_Input_File_Path: ./inputFiles/userPolygons/closeAngleTest.dat


/*===========================================================================*/
/* User-Specified Rectangles                                                 */
/* Mandatory Parameters if using user-rectangles                             */
/* NOTE: Number of elements must match number of user-ellipse families       */
/* (fourth number in nShape parameter)                                       */
/*===========================================================================*/
/* NOTE: Only one user-rectangle is placed into the domain per defined 
         user-rectangle, with possibility of being rejected  */
         

userRectanglesOnOff: 1    //0 - User Rectangles off
                        //1 - User Rectangles on

UserRect_Input_File_Path: %s



/*===========================================================================*/
/* If you would like to input user specified rectangles according to their
  coordinates, you can use the parameter userDefCoordRec. In that case, all        
  of the user specified rectangles will have to be according to coordinates.
*/

userRecByCoord: 0
//  0 - user defined rectangles not used
//  1 - user defined rectangles used and defined by input file:

RectByCood_Input_File_Path: ./inputFiles/userPolygons/rectCoords.dat


/*WARNING: userDefCoordRec can cause LaGriT errors because the polygon 
vertices are not put in clockwise or counter-clockwise order.
If errors (Usualy seg fualt during meshing if using LaGriT), 
try to reorder the points till u get it right.
Also, coordinates must be co-planar */

/*===========================================================================*/
// Aperture [m]
/* Mandatory parameter, and can be specified in several ways:
- 1)meanAperture and stdAperture for using LogNormal distribution.
- 2)apertureFromTransmissivity, first transmissivity is defined, and then, 
  using a cubic law, the aperture is calculated;
- 3)constantAperture, all fractures, regardless of their size, will have 
  the same aperture value;
- 4)lengthCorrelatedAperture, aperture is defined as a function of fracture size*/

//NOTE: Only one aperture type may be used at a time 

aperture: 3  //choise of aperture option described above

//(**** 1)meanAperture and stdAperture for using LogNormal distribution.********)
meanAperture:  3 /*Mean value for aperture using  
                                   normal distribution */
stdAperture: 0.8  //Standard deviation     

/*(****** 2)apertureFromTransmissivity, first transmissivity is defined, 
  and then, using a cubic law, the aperture is calculated;***************/
apertureFromTransmissivity: {1.6e-9, 0.8}
    /* Transmissivity is calculated as transmissivity = F*R^k,
       where F is a first element in aperturefromTransmissivity,
       k is a second element and R is a mean radius of a polygon. 
       Aperture is calculated according to cubic law as 
       b=(transmissivity*12)^1/3 */
       
/*(****** 3)constantAperture, all fractures, regardless of their size, 
   will have the same aperture value;    **********************************/
      
constantAperture: 1e-5  //Sets constant aperture for all fractures 

/*(******** 4)lengthCorrelatedAperture, aperture is defined as a function of 
       fracture size *******************/
       
lengthCorrelatedAperture: {5e-5, 0.5}
    /*Length Correlated Aperture Option:
      Aperture is calculated by: b=F*R^k,
      where F is a first element in lengthCorrelatedAperture, 
      k is a second element and R is a mean radius of a polygon.*/


//============================================================================
//Permeability 
/* Options:
    0: Permeability of each fracture is a function of fracture aperture, 
     given by k=(b^2)/12, where b is an aperture and k is permeability
    1: Constant permeabilty for all fractures */

permOption: 1  //See above for options

constantPermeability: 1e-12  //Constant permeability for all fractures 


//=============================================================================
// Mandatory Meshing Grid Refinement Parameters: 

slope: 2 /* Factor used when refining fractures according to distance 
    from fractures' intersection lines. The bigger this number
    the more refined the mesh will be closer to the intersection
    line (multiplies the reference field in message2 
    in the files DFNgenerator/dfn/final_dfn.py or final_dfn _un.py). */ 

refineDist: 0.5  /*Factor used when refining fractures according to distance 
    from fractures' intersection lines. The bigger this number
    the more refined the mesh will be closer to the intersection
    line (adds a value to the reference field in massage2
    in the files DFNgenerator/dfn/final_dfn.py or final_dfn _un.py). */ 

//=============================================================================

'''




input_fracture_file = '''
************************* USER DEFINED RECTANGLES ***************************/
/*****************************************************************************/

/*****************************************************************************/
//Number of User Defined Rectangles
/*****************************************************************************/
nUserRect: 6


/*****************************************************************************/
//Radius for each rectangle (one per line)
/*****************************************************************************/
Radii:
1
1
1
1
1
1

/*****************************************************************************/
//Apect Ratio for each rectangle (one per line)
/*****************************************************************************/
Aspect_Ratio:
1
1
1
1
1
1

/*****************************************************************************/
//Angle Option: 0 - All angles in radians	
//				1 - All angles in degrees	
/*****************************************************************************/
AngleOption: 
1

/*****************************************************************************/
//Rotation around center for each rectangle (one per line)
/*****************************************************************************/
Beta:
0
0
0
0
0
0

/*****************************************************************************/
//Translation of each rectangle according to its center {x,y,z} (one per line)
/*****************************************************************************/
Translation:
{-1,0,0}
{1,0,0}
{0,-1,0}
{0,1,0}
{0,0,-1}
{0,0,1}

/*****************************************************************************/
//Normal Vecor for each rectangle (one per line)
/*****************************************************************************/
Normal:
{1,0,0}
{1,0,0}
{0,1,0}
{0,1,0}
{0,0,1}
{0,0,1}

'''
def test(outputPath):

	#create subfolder for this test
	test_folder = outputPath + '/Intersections_On_Edge_Tests'
	os.makedirs(test_folder)

	h =  0.25

	Key =  [1] #might pass once FRAM is updated 
	#key: 0 = test should pass, 1 = test should fail
	
	print "\n******** Running Intersection On Edges Test: ********"
	print   "*****************************************************\n"
	
	#for i in range(len(list)):
        
	test_name = 'Intersections_On_Edges'
	test_subFolder = test_folder + "/" + test_name + "/"
	os.makedirs(test_subFolder)
		
	main_filename =  test_subFolder + "input_" + test_name + ".dat"
	input_filename = test_subFolder + 'input_Intersections_On_Edges.dat'
        
	f = open(main_filename,'w')
	f.write(main_input%(h,input_filename))
	f.close()
		
	f = open(input_filename,'w')
	f.write(input_fracture_file)
	f.close()
		
	cmd = './Test_Inputs/testDFN.sh '+ test_subFolder + ' ' + main_filename + ' 2 > ' + test_subFolder + 'programOutput.txt'
		
	print "Running test: " + test_name
	exitVal = os.system(cmd)
	if (exitVal == 0 and Key[0] == 0) or (exitVal != 0 and Key[0] == 1):
		print "Test passed (exit value = %d, Key = %d)"%(exitVal, Key[0]) + "\n"
	else:
		print "TEST FAILED (exit value = %d, Key = %d)"%(exitVal, Key[0]) + "\n"
			

		


