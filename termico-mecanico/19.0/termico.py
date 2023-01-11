# -*- coding: utf-8 -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import numpy as np
import os
#
if os.path.isfile("termico.odb"):
     os.remove("termico.odb")
if os.path.isfile("termico.lck"):
       os.remove("termico.lck")
#
#
#
#
#
#
#
os.system('C:\Temp\termico.*')
temperaturas = [293.15, 573.15, 723.15, 873.15]
#
#
#
# DEFINE TIME PERIOD E INCREMENT SIZE
#
time_period573 = 560
time_period723 = 300
time_period873 = 300
increment_size = 1
max_inc = int(time_period573/increment_size + time_period723/increment_size + time_period873/increment_size)
malha_agreg = 0.002*1e3
malha_arg = 0.002*1e3
#
# DEFINE PROPRIEDADES DOS MATERIAIS
#
# obs: propriedades termicas nbr 15220
#
#
#
#
param_argamass = {'Density': 2252.0*1e-9, 'Conductivity': 1.15*60*1e-3, 'SpecificHeat': 1000.0, 'Expansion': 3.67e-6}
#
param_agreg = {'Density': 2500.0*1e-9, 'Conductivity': 0.7*60*1e-3, 'SpecificHeat': 840.0, 'Expansion': 3.779e-6}
#
#
#
#
# CRIA RETANGULO
#
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(
    point1=(0.0, 0.0), point2=(0.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(
    entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].rectangle(
    point1=(0,0), point2=(50.0,100.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR,
                           name='Part-1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(
    sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
#
# CRIA MATERIAIS E ATRIBUI AO RETANGULO
#
mdb.models['Model-1'].Material(name='Material-argamassa')
mdb.models['Model-1'].materials['Material-argamassa'].Density(table=((param_argamass['Density'], ), ))
mdb.models['Model-1'].materials['Material-argamassa'].Conductivity(table=((param_argamass['Conductivity'], ), ))
mdb.models['Model-1'].materials['Material-argamassa'].SpecificHeat(table=((param_argamass['SpecificHeat'], ), ))
mdb.models['Model-1'].materials['Material-argamassa'].Expansion(table=((param_argamass['Expansion'], ), ))
mdb.models['Model-1'].materials['Material-argamassa'].expansion.setValues(zero=temperaturas[0])
#
mdb.models['Model-1'].Material(name='Material-agregado')
mdb.models['Model-1'].materials['Material-agregado'].Density(table=((param_agreg['Density'], ), ))
mdb.models['Model-1'].materials['Material-agregado'].Conductivity(table=((param_agreg['Conductivity'], ), ))
mdb.models['Model-1'].materials['Material-agregado'].SpecificHeat(table=((param_agreg['SpecificHeat'], ), ))
mdb.models['Model-1'].materials['Material-agregado'].Expansion(table=((param_agreg['Expansion'], ), ))
mdb.models['Model-1'].materials['Material-agregado'].expansion.setValues(zero=temperaturas[0])
#
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-argamassa',
    name='Section-argamassa', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-argamassa',
    name='Section-ZTI', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-agregado',
    name='Section-agregado', thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.findAt(((1.0, 1.0,
   0.0), (0.0, 0.0, 1.0)), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
    'Section-argamassa', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=5.59, name='__profile__',
     sheetSize=223.6, transform=
     mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
     sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0],
     sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
     COPLANAR_EDGES,
sketch=mdb.models['Model-1'].sketches['__profile__'])
#
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models['Model-1'].parts['Part-1'].sets['Set-1'])
#
# CRIANDO AS BOLINHAS
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(19.991977,37.369972), point1=(23.306872,37.369972))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.763916,36.255077), point1=(36.384155,36.255077))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(10.601993,30.320154), point1=(14.207299,30.320154))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(41.417167,29.698146), point1=(44.562355,29.698146))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(7.76317,95.781028), point1=(10.425343,95.781028))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(10.848319,21.803243), point1=(14.838102,21.803243))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(34.875157,8.320791), point1=(39.474050000000005,8.320791))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(38.680129,19.071307), point1=(44.743173,19.071307))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(15.105844,76.163871), point1=(18.081338,76.163871))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(20.70755,48.764079), point1=(25.705868000000002,48.764079))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.244466,91.023287), point1=(37.905977,91.023287))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(8.9879,81.186038), point1=(11.979001,81.186038))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(33.317821,65.396423), point1=(39.687392,65.396423))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.868138,76.118789), point1=(34.46177,76.118789))
#
# ATRIBUINDO MATERIAL AS BOLINHAS
#
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ), 	sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(
    (( 19.991977 , 37.369972 ,    0.0),),
    (( 30.763916 , 36.255077 ,    0.0),),
    (( 10.601993 , 30.320154 ,    0.0),),
    (( 41.417167 , 29.698146 ,    0.0),),
    (( 7.76317 , 95.781028 ,    0.0),),
    (( 10.848319 , 21.803243 ,    0.0),),
    (( 34.875157 , 8.320791 ,    0.0),),
    (( 38.680129 , 19.071307 ,    0.0),),
    (( 15.105844 , 76.163871 ,    0.0),),
    (( 20.70755 , 48.764079 ,    0.0),),
    (( 30.244466 , 91.023287 ,    0.0),),
    (( 8.9879 , 81.186038 ,    0.0),),
    (( 33.317821 , 65.396423 ,    0.0),),
    (( 30.868138 , 76.118789 ,    0.0),),
 ),name='Set-3')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName=
    'Section-agregado', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models['Model-1'].parts['Part-1'].sets['Set-3'])
#
#CRIANDO MALHA
#
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TRI, regions=
    mdb.models['Model-1'].parts['Part-1'].faces.findAt(
    (( 19.991977 , 37.369972 ,    0.0),),
    (( 30.763916 , 36.255077 ,    0.0),),
    (( 10.601993 , 30.320154 ,    0.0),),
    (( 41.417167 , 29.698146 ,    0.0),),
    (( 7.76317 , 95.781028 ,    0.0),),
    (( 10.848319 , 21.803243 ,    0.0),),
    (( 34.875157 , 8.320791 ,    0.0),),
    (( 38.680129 , 19.071307 ,    0.0),),
    (( 15.105844 , 76.163871 ,    0.0),),
    (( 20.70755 , 48.764079 ,    0.0),),
    (( 30.244466 , 91.023287 ,    0.0),),
    (( 8.9879 , 81.186038 ,    0.0),),
    (( 33.317821 , 65.396423 ,    0.0),),
    (( 30.868138 , 76.118789 ,    0.0),),
))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=0.7)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 23.306872 , 37.369972 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 36.384155 , 36.255077 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 14.207299 , 30.320154 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 44.562355 , 29.698146 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 10.425343 , 95.781028 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 14.838102 , 21.803243 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 39.474050000000005 , 8.320791 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 44.743173 , 19.071307 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 18.081338 , 76.163871 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.705868000000002 , 48.764079 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 37.905977 , 91.023287 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.979001 , 81.186038 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 39.687392 , 65.396423 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 34.46177 , 76.118789 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
#
# FAZ O ASSEMBLY, CRIANDO OS PONTOS DE CONTROLE E AS CONDIÇÕES DE CONTORNO
#
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(
    dependent=ON, name='Part-1-1', part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.Set(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((0.0 , 50.0 , 0.0),), ), name='Lateral1')
mdb.models['Model-1'].rootAssembly.Set(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt((( 50.0 , 50.0 , 0.0),), ), name='Lateral2')
mdb.models['Model-1'].rootAssembly.Set(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((1*1e-3, 0.0, 0.0),), ), name='Base')
mdb.models['Model-1'].rootAssembly.Set(
    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((1*1e-3 , 100.0 , 0.0),), ), name='Topo')
#
# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((17.431429 , 57.588253, 0.0),), ), name='Ponto3')
# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((23.388278 , 95.099907, 0.0),), ), name='Ponto2')
# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((50.0, 100.0 , 0.0),), ), name='Ponto1')
#
# aplica temperatura inicial
mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=temperaturas[0],
  name='Temperatura Inicial', region=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Set-1'])
#
#
#
#
#
#
#
#step1 - carga573
mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga573', previous='Initial', timeIncrementationMethod=FIXED, timePeriod=time_period573, amplitude=RAMP)
mdb.models['Model-1'].TemperatureBC(amplitude=UNSET, createStepName='Carga573', distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=temperaturas[1], name='Temp-' + str(1), region=mdb.models['Model-1'].rootAssembly.sets['Lateral2'])
mdb.models['Model-1'].TemperatureBC(amplitude=UNSET, createStepName='Carga573', distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=temperaturas[1], name='Temp-' + str(2), region=mdb.models['Model-1'].rootAssembly.sets['Topo'])
#
#
#
#step2 - carga723
mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga723', previous='Carga573', timeIncrementationMethod=FIXED, 
    timePeriod=time_period723, amplitude=RAMP)
mdb.models['Model-1'].boundaryConditions['Temp-' + str(1)].setValuesInStep(magnitude=temperaturas[2], stepName='Carga723')
mdb.models['Model-1'].boundaryConditions['Temp-' + str(2)].setValuesInStep(magnitude=temperaturas[2], stepName='Carga723')	
#
#step3 - carga873
mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga873', previous='Carga723', timeIncrementationMethod=FIXED, 
    timePeriod=time_period873, amplitude=RAMP)
mdb.models['Model-1'].boundaryConditions['Temp-' + str(1)].setValuesInStep(magnitude=temperaturas[3], stepName='Carga873')
mdb.models['Model-1'].boundaryConditions['Temp-' + str(2)].setValuesInStep(magnitude=temperaturas[3], stepName='Carga873')
#
# CRIA O JOB
#
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(frequency = LAST_INCREMENT, variables=('NT', 'TEMP'))

#
myJob = mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, memory=90, 
                	memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, multiprocessingMode=DEFAULT, name='termico', nodalOutputPrecision=SINGLE, numCpus=1, 
                	queue=None, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
#
#SUBMETE O JOB PARA ANÁLISE
#
myJob.submit()
myJob.waitForCompletion()
odbName = 'termico.odb'
odb = openOdb(path=odbName)
