# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

filename = "C:\\IC\\Teste 2022\\40,0p\\stones2DA3C1-40,0-fit.dgibi"
Diam=50.0
H=100.0

c1 = 0
c2 = Diam
c3 = Diam/2.0
c4 = H
c5 = -1. * c2

texto0 ='# -*- coding: utf-8 -*-'
texto1 ='from part import *'
texto2 ='from material import *'
texto3 ='from section import *'
texto4 ='from assembly import *'
texto5 ='from step import *'
texto6 ='from interaction import *'
texto7 ='from load import *'
texto8 ='from mesh import *'
texto9 ='from optimization import *'
texto10 ='from job import *'
texto11 ='from sketch import *'
texto12 ='from visualization import *'
texto13 ='from connectorBehavior import *\nimport numpy as np'

texto14 = '#CRIANDO RETANGULO';

texto15 ='mdb.models[\'Model-1\'].ConstrainedSketch(name=\'__profile__\', sheetSize=150.0)';
texto95 ='mdb.models[\'Model-1\'].sketches[\'__profile__\'].sketchOptions.setValues(viewStyle=AXISYM)';
texto96 ='mdb.models[\'Model-1\'].sketches[\'__profile__\'].ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 1.0))'; 
texto99 ='mdb.models[\'Model-1\'].sketches[\'__profile__\'].FixedConstraint(entity=mdb.models[\'Model-1\'].sketches[\'__profile__\'].geometry[2])';
texto16 ='mdb.models[\'Model-1\'].sketches[\'__profile__\'].rectangle(point1=(';
texto17 =',';
texto18 ='), point2=(';
texto19 ='))';
texto20 ='mdb.models[\'Model-1\'].Part(dimensionality=TWO_D_PLANAR, name=\'Part-1\', type=';
texto21 ='     DEFORMABLE_BODY)';
texto22 ='mdb.models[\'Model-1\'].parts[\'Part-1\'].BaseShell(sketch=';
texto23 ='     mdb.models[\'Model-1\'].sketches[\'__profile__\'])';
texto24 ='del mdb.models[\'Model-1\'].sketches[\'__profile__\']';


texto25 = '#CRIANDO MATERIAIS E ATRIBUINDO AO RETANGULO';

texto26 = 'mdb.models[\'Model-1\'].Material(name=\'Material-argamassa\')';
texto27 = 'mdb.models[\'Model-1\'].materials[\'Material-argamassa\'].Density(table=((param_argmass[\'Density\'], param_argmass[\'T0\']), ), temperatureDependency=ON)\nmdb.models[\'Model-1\'].materials[\'Material-argamassa\'].Depvar(n=10)';
texto76 = 'mdb.models[\'Model-1\'].materials[\'Material-argamassa\'].UserMaterial(mechanicalConstants=(param_argmass[\'E\'], param_argmass[\'mu\'], param_argmass[\'T0\'], param_argmass[\'Expansion\'], param_mazars[\'alpha_t\'], param_mazars[\'bheta_t\'], param_mazars[\'alpha_c\'], param_mazars[\'bheta_c\'], param_mazars[\'e_d0\'], param_mazars[\'bheta\']),  thermalConstants=(param_argmass[\'Conductivity\'], param_argmass[\'SpecificHeat\']), type=THERMOMECHANICAL, unsymm=ON)';    
    
texto28 = 'mdb.models[\'Model-1\'].Material(name=\'Material-agregado\')';
texto29 = 'mdb.models[\'Model-1\'].materials[\'Material-agregado\'].Density(table=((param_agreg[\'Density\'], ), ))\nmdb.models[\'Model-1\'].materials[\'Material-agregado\'].Elastic(table=((param_agreg[\'E\'], param_agreg[\'mu\'], param_agreg[\'T0\']), ), temperatureDependency=ON)';
texto77 = 'mdb.models[\'Model-1\'].materials[\'Material-agregado\'].Conductivity(table=((param_agreg[\'Conductivity\'], ), ))\nmdb.models[\'Model-1\'].materials[\'Material-agregado\'].SpecificHeat(table=((param_agreg[\'SpecificHeat\'], ), ))\nmdb.models[\'Model-1\'].materials[\'Material-agregado\'].Expansion(table=((param_agreg[\'Expansion\'], ), ))';


texto30 = 'mdb.models[\'Model-1\'].HomogeneousSolidSection(material=\'Material-argamassa\','; 
texto31 = '    name=\'Section-argamassa\', thickness=None)';
texto32 = 'mdb.models[\'Model-1\'].HomogeneousSolidSection(material=\'Material-agregado\','; 
texto33 = '    name=\'Section-agregado\', thickness=None)';
texto34 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].Set(faces=';
texto35 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt(((1.0, 1.0,'; 
texto36 = '   0.0), (0.0, 0.0, 1.0)), ), name=\'Set-1\')';
texto37 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,'; 
texto38 = '    offsetField=\'\', offsetType=MIDDLE_SURFACE, region=';
texto39 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-1\'], sectionName=';
texto40 = '    \'Section-argamassa\', thicknessAssignment=FROM_SECTION)';


texto41 ='mdb.models[\'Model-1\'].ConstrainedSketch(gridSpacing=5.59*1e-3, name=\'__profile__\',';
texto42 ='     sheetSize=223.6, transform=';
texto43 ='     mdb.models[\'Model-1\'].parts[\'Part-1\'].MakeSketchTransform(';
texto44 ='     sketchPlane=mdb.models[\'Model-1\'].parts[\'Part-1\'].faces[0],';
texto45 ='     sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))';
texto46 ='mdb.models[\'Model-1\'].parts[\'Part-1\'].projectReferencesOntoSketch(filter=';
texto47 ='     COPLANAR_EDGES,';
texto48 = 'sketch=mdb.models[\'Model-1\'].sketches[\'__profile__\'])';


textFile = open("script.py", "w")

textFile.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n\n%s\n\n' % (texto0,texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14))

textFile.write('\ntemperaturas = [573.15, 723.15, 873.15]\numat_path = \'c:\\\Users\\\Lahis Assis\\\Desktop\\\script\\\umat_termomecanico_sem_dano.for\'')

textFile.write('\n#command line')
textFile.write('\n#abq611pr3 cae noGUI=abaqus2D_Agreg0.py -- 0.95 10000.0 1.0 3000.0 0.00001 1.0')

textFile.write('\nparam_argmass = {\'E\': 34.0*1e9, \'mu\': 0.2, \'T0\': 0.0, \'Density\': 2252.0, \'Conductivity\': 1.15, \'SpecificHeat\': 1000.0, \'Expansion\': 0.0}')
textFile.write('\nparam_agreg = {\'E\': 50.0*1e9, \'mu\': 0.1, \'T0\': 0.0, \'Density\': 2550.0, \'Conductivity\': 2.0, \'SpecificHeat\': 1000.0, \'Expansion\': 0.00001715}')
textFile.write('\n#param_mazars = {\'alpha_t\': float(sys.argv[-6]), \'bheta_t\': float(sys.argv[-5]), \'alpha_c\': float(sys.argv[-4]), \'bheta_c\': float(sys.argv[-3]), \'e_d0\': float(sys.argv[-2]), \'bheta\': float(sys.argv[-1])}')
textFile.write('\nparam_mazars = {\'alpha_t\': 0.95, \'bheta_t\': 10000.0, \'alpha_c\': 1.0, \'bheta_c\': 3000.0, \'e_d0\': 0.00001, \'bheta\': 1.0}')


textFile.write('\n\n%s\n%s\n%s\n%s\n%s%f%s%f%s%f%s%f%s\n' % (texto15,texto95,texto96,texto99,texto16,c1,texto17,c1,texto18,c2,texto17,c4,texto19))

textFile.write('%s\n%s\n%s\n%s\n%s\n\n%s\n\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (texto20,texto21,texto22,texto23,texto24,texto25,texto26,texto27,texto76,texto28,texto29,texto77,texto30,texto31,texto32,texto33,texto34,texto35,texto36,texto37,texto38,texto39,texto40))

textFile.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (texto41,texto42,texto43,texto44,texto45, texto46,texto47, texto48))

textFile.write('\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-1\'])\n')



v = np.loadtxt(filename)

R = v[:,2]
G = v [:,(0,1)]

xx = G[:,0] + R
yy = G[:,1] + R

texto65 = '#CRIANDO AS BOLINHAS'

texto49 ='mdb.models[\'Model-1\'].sketches[\'__profile__\'].CircleByCenterPerimeter(center=(';
texto50 ='), point1=(';
texto51 ='))';

textFile.write('\n\n%s\n\n' % (texto65));

n=len(R)

for k in range(0,n):
    textFile.write('%s%f%s' % (texto49,G[k,0],texto17) )
    textFile.write('%f %s %f %s %f %s\n' % (G[k,1],texto50,xx[k],texto17, G[k,1],texto51) )


texto52 ='mdb.models[\'Model-1\'].parts[\'Part-1\'].PartitionFaceBySketch(faces=';
texto53 ='     mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.getSequenceFromMask((\'[#1 ]\', ), ), 	sketch=mdb.models[\'Model-1\'].sketches[\'__profile__\'])';
texto54 ='del mdb.models[\'Model-1\'].sketches[\'__profile__\']';


texto66 = '#ATRIBUINDO MATERIAL AS BOLINHAS';

texto55 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].Set(faces=';
texto56 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt(';
texto57 = '((';
texto58 = '    0.0),),';
texto59 = ' ),name=\'Set-2\')';
texto106 = ' ),name=\'Set-3\')';
texto108 = ' ),name=\'Set-4\')';
texto110 = ' ),name=\'Set-5\')';
texto112 = ' ),name=\'Set-6\')';
texto60 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,'; 
texto61 = '    offsetField=\'\', offsetType=MIDDLE_SURFACE, region=';
texto62 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-2\'], sectionName=';
texto107 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'], sectionName=';
texto109 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'], sectionName=';
texto111 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-5\'], sectionName=';
texto113 = '    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-6\'], sectionName=';
texto63 = '    \'Section-agregado\', thicknessAssignment=FROM_SECTION)';


texto71 = '#CRIANDO MALHA';

texto64 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].setMeshControls(elemShape=TRI, regions=';
texto65 = '))';
texto67 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].seedPart(deviationFactor=0.1,'; 
texto68 = '    minSizeFactor=0.1, size=0.7)';
texto69 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].seedEdgeBySize(constraint=FINER,'; 
texto70 = '    deviationFactor=0.1, edges=';
texto72 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].edges.findAt(';
texto73 = '), minSizeFactor=0.1, size=';
texto74 = ')';
texto75 = 'mdb.models[\'Model-1\'].parts[\'Part-1\'].generateMesh()';


textFile.write('\n\n%s\n\n%s\n%s\n%s\n%s\n%s\n' % (texto66,texto52,texto53,texto54,texto55, texto56) );
q = 1;
a=1
p=1

for k in range(0,n):
    if(q<=254):
        textFile.write('%s %f %s %f %s %s\n' % (texto57,G[k,0],texto17,G[k,1],texto17,texto58))
        a=a+1
    elif (a<508):
        textFile.write('%s\n%s\n%s\n%s\n%s\n' % (texto59,texto60,texto61,texto62,texto63))
        textFile.write('\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-2\'])\n')
        textFile.write('%s\n%s\n' % (texto55, texto56))
        textFile.write('%s %f %s %f %s %s\n' % (texto57,G[k,0],texto17,G[k,1],texto17,texto58))
        q=0
        p=10
        
    elif (a<762):
        textFile.write('%s\n%s\n%s\n%s\n%s\n' % (texto106,texto60,texto61,texto107,texto63))
        textFile.write('\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'])\n')        
        textFile.write('%s\n%s\n' % (texto55, texto56))
        textFile.write('%s %f %s %f %s %s\n' % (texto57,G[k,0],texto17,G[k,1],texto17,texto58))
        q=0
    else:
        textFile.write('%s\n%s\n%s\n%s\n%s\n',texto108,texto60,texto61,texto109,texto63)
        textFile.write('\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'])\n')
        textFile.write('%s\n%s\n', texto55, texto56)
        textFile.write('%s %f %s %f %s %s\n',texto57,G[k,0],texto17,G[k,1],texto17,texto58)
        q=0
        
        
    q = q+1


if a<510:
    textFile.write('%s\n%s\n%s\n%s\n%s\n\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'])\n\n%s\n\n%s\n%s\n' % (texto106,texto60,texto61,texto107,texto63,texto71,texto64,texto56))
    
    
if a>510:
    if a <766:
        
        textFile.write('%s\n%s\n%s\n%s\n%s\n\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'])\n\n%s\n\n%s\n%s\n' % (texto108,texto60,texto61,texto109,texto63,texto71,texto64,texto56))
        
        
if a>765:
    textFile.write('%s\n%s\n%s\n%s\n%s\n\nmdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4T, elemLibrary=STANDARD), ElemType(elemCode=CPS3T, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-5\'])\n\n%s\n\n%s\n%s\n' % (texto110,texto60,texto61,texto111,texto63,texto71,texto64,texto56))
    


q=1; 
for k in range(0,n):
    if(q<=255):
        textFile.write('%s%f%s%f%s%s\n' % (texto57,G[k,0],texto17,G[k,1],texto17,texto58))
    else: 
        textFile.write('%s\n%s\n%s\n' % (texto65,texto64,texto56))
        q=0
    q = q+1

textFile.write('%s\n%s\n%s\n' % (texto65,texto67,texto68))


tamanho = np.zeros(n)

for k in range(0,n):
    tamanho[k] = 0.5 #abs((1/2)*(R(k,1)+G(k,1)));
    textFile.write('%s\n %s\n %s\n %s %f %s %f %s %s %s %f %s\n' % (texto69,texto70,texto72,texto57,xx[k],texto17,G[k,1],texto17,texto58,texto73,tamanho[k],texto74))

textFile.write('%s\n\n' % (texto75))


texto78 = '#COLOCANDO NO ASSEMBLY, CRIANDO O ELEMENTO E CRIANDO CONDIÇÕES DE CONTORNO';

texto79 = 'mdb.models[\'Model-1\'].rootAssembly.DatumCsysByDefault(CARTESIAN)';
texto80 = 'mdb.models[\'Model-1\'].rootAssembly.Instance(dependent=ON, name=\'Part-1-1\', part=mdb.models[\'Model-1\'].parts[\'Part-1\'])';
texto100 = 'mdb.models[\'Model-1\'].rootAssembly.Set(edges=mdb.models[\'Model-1\'].rootAssembly.instances[\'Part-1-1\'].edges.findAt((( 0.0 , ' + str(Diam) + ' ,     0.0),), ), name=\'Lateral1\')\nmdb.models[\'Model-1\'].rootAssembly.Set(edges=mdb.models[\'Model-1\'].rootAssembly.instances[\'Part-1-1\'].edges.findAt((( ' + str(Diam) + ' , ' + str(Diam) + ' ,     0.0),), ), name=\'Lateral2\')';
#texto101 = 'mdb.models[\'Model-1\'].XsymmBC(createStepName=\'Initial\', localCsys=None, name=\'Axissimetrico\', region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Geratriz\'])';mdb.models['Model-1'].rootAssembly.Set(elements=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].elements.getSequenceFromMask(mask=('[#0:10 #1000 ]', ), ), name='Elemento')

texto81 = 'x, y, z = 42.0, 75.0, 0.0\nshift = 0.5\nx1, y1, z1, x2, y2, z2 = x-shift, y-shift, z, x+shift, y+shift, z\na = mdb.models[\'Model-1\'].rootAssembly\nels_1 = a.instances[\'Part-1-1\'].elements\nCoh_els = els_1.getByBoundingBox(x1, y1, z1, x2, y2, z2 )\na.Set(elements=Coh_els, name=\'Elemento\')';


texto82 = 'mdb.models[\'Model-1\'].rootAssembly.Set(edges=mdb.models[\'Model-1\'].rootAssembly.instances[\'Part-1-1\'].edges.findAt((( 1*1e-3 , 0.0 ,     0.0),), ), name=\'Base\')';

texto83 = 'mdb.models[\'Model-1\'].EncastreBC(createStepName=\'Initial\', localCsys=None, name=\'Engaste\', region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Base\'])';
texto84 = 'mdb.models[\'Model-1\'].rootAssembly.Set(edges=mdb.models[\'Model-1\'].rootAssembly.instances[\'Part-1-1\'].edges.findAt((( 1*1e-3 ,' + str(H) + ' ,     0.0),), ), name=\'Topo\')\nmdb.models[\'Model-1\'].EncastreBC(createStepName=\'Initial\', localCsys=None, name=\'Engaste2\', region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Topo\'])';

textFile.write('%s\n\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n\n' % (texto78,texto79,texto80,texto100,texto81,texto82,texto83,texto84))


textFile.write('\nmdb.models[\'Model-1\'].CoupledTempDisplacementStep(amplitude=RAMP, cetol=None, creepIntegration=None, deltmx=None, name=\'Step-1\', previous=\'Initial\', response=STEADY_STATE)')
textFile.write('\nmdb.models[\'Model-1\'].TemperatureBC(amplitude=UNSET, createStepName=\'Step-1\', distributionType=UNIFORM, fieldName=\'\', fixed=OFF, magnitude=temperaturas[0], name=\'Temp-\' + str(1), region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Lateral1\'])')
textFile.write('\nmdb.models[\'Model-1\'].TemperatureBC(amplitude=UNSET, createStepName=\'Step-1\', distributionType=UNIFORM, fieldName=\'\', fixed=OFF, magnitude=temperaturas[0], name=\'Temp-\' + str(2), region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Lateral2\'])')
textFile.write('\nmdb.models[\'Model-1\'].TemperatureBC(amplitude=UNSET, createStepName=\'Step-1\', distributionType=UNIFORM, fieldName=\'\', fixed=OFF, magnitude=temperaturas[0], name=\'Temp-\' + str(3), region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Base\'])')
textFile.write('\nmdb.models[\'Model-1\'].TemperatureBC(amplitude=UNSET, createStepName=\'Step-1\', distributionType=UNIFORM, fieldName=\'\', fixed=OFF, magnitude=temperaturas[0], name=\'Temp-\' + str(4), region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Topo\'])\n\n')

textFile.write('\nmdb.models[\'Model-1\'].CoupledTempDisplacementStep(amplitude=RAMP, cetol=None, creepIntegration=None, deltmx=None, name=\'Step-2\', previous=\'Step-1\', response=STEADY_STATE)')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(1)].setValuesInStep(magnitude=temperaturas[1], stepName=\'Step-2\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(2)].setValuesInStep(magnitude=temperaturas[1], stepName=\'Step-2\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(3)].setValuesInStep(magnitude=temperaturas[1], stepName=\'Step-2\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(4)].setValuesInStep(magnitude=temperaturas[1], stepName=\'Step-2\')')

textFile.write('\n\n\nmdb.models[\'Model-1\'].CoupledTempDisplacementStep(amplitude=RAMP, cetol=None, creepIntegration=None, deltmx=None, name=\'Step-3\', previous=\'Step-2\', response=STEADY_STATE)')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(1)].setValuesInStep(magnitude=temperaturas[2], stepName=\'Step-3\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(2)].setValuesInStep(magnitude=temperaturas[2], stepName=\'Step-3\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(3)].setValuesInStep(magnitude=temperaturas[2], stepName=\'Step-3\')')
textFile.write('\nmdb.models[\'Model-1\'].boundaryConditions[\'Temp-\' + str(4)].setValuesInStep(magnitude=temperaturas[2], stepName=\'Step-3\')')

texto90 = '#CRIANDO HISTORY OUTPUT E O JOB';

texto91 = 'mdb.models[\'Model-1\'].HistoryOutputRequest(createStepName=\'Step-1\', name=\'Tensao-Deform\', rebar=EXCLUDE, region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Elemento\'], sectionPoints=DEFAULT, variables=(\'MISES\', \'E22\'))';
texto92 = 'mdb.models[\'Model-1\'].HistoryOutputRequest(createStepName=\'Step-1\', name=\'Deslocamento\', rebar=EXCLUDE, region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Topo\'], sectionPoints=DEFAULT, variables=(\'U2\', ))';
texto93 = 'mdb.models[\'Model-1\'].HistoryOutputRequest(createStepName=\'Step-1\', name=\'Reacao\', rebar=EXCLUDE, region=mdb.models[\'Model-1\'].rootAssembly.sets[\'Base\'], sectionPoints=DEFAULT, variables=(\'RF2\', ))';
texto94 = 'myJob = mdb.Job(atTime=None, contactPrint=OFF, description=\'\', echoPrint=OFF, explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model=\'Model-1\', modelPrint=OFF, multiprocessingMode=DEFAULT, name=\'Analise\', nodalOutputPrecision=SINGLE, numCpus=1, queue=None, scratch=\'\', type=ANALYSIS, userSubroutine=umat_path, waitHours=0, waitMinutes=0)';

textFile.write('\n\nmdb.models[\'Model-1\'].fieldOutputRequests[\'F-Output-1\'].setValues(variables=(\'S\', \'E\', \'PE\', \'PEEQ\', \'PEMAG\', \'LE\', \'U\', \'RF\', \'CF\', \'CSTRESS\', \'CDISP\', \'NT\', \'SDV\', \'TEMP\', \'FV\', \'UVARM\'))')

texto102 = '#SUBMETE O JOB PARA ANÁLISE';

texto103 = 'myJob.submit()';
texto104 = 'myJob.waitForCompletion()';
texto105 = 'odbName = \'Analise.odb\'';

textFile.write('%s\n\n%s\n%s\n%s\n%s\n\n%s\n\n%s\n%s\n%s\n' % (texto90,texto91,texto92,texto93,texto94, texto102, texto103, texto104, texto105))



textFile.close()
