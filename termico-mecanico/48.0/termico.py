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
    center=(10.884251,9.70274), point1=(19.548920000000003,9.70274))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(24.836193,6.277025), point1=(30.313252000000002,6.277025))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(44.26359,5.845128), point1=(47.518009,5.845128))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(41.30236,20.794422), point1=(45.064611,20.794422))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(36.940855,2.873181), point1=(39.448589,2.873181))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.558564,25.093371), point1=(9.626628,25.093371))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(21.388376,28.010412), point1=(27.297235,28.010412))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.965233,18.161072), point1=(36.677901,18.161072))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(34.815985,31.597999), point1=(42.491474999999994,31.597999))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(6.473431,43.497384), point1=(11.400296,43.497384))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(9.644558,32.926606), point1=(12.368285,32.926606))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(24.670634,44.461659), point1=(30.952082,44.461659))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(40.559214,45.786513), point1=(44.420657999999996,45.786513))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(46.535521,30.130967), point1=(49.585795000000005,30.130967))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.820197,59.703067), point1=(11.511934,59.703067))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.857696,52.356229), point1=(15.594054,52.356229))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.446255,65.100389), point1=(36.636675,65.100389))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(45.921744,38.286522), point1=(48.669489,38.286522))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(32.812095,49.477887), point1=(35.650650999999996,49.477887))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(41.489274,54.317647), point1=(45.848656000000005,54.317647))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(4.239361,72.790662), point1=(7.953906,72.790662))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(10.092571,68.468682), point1=(13.237276999999999,68.468682))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(16.075371,58.248903), point1=(18.759847,58.248903))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(23.557651,73.818616), point1=(27.377343,73.818616))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(19.907882,63.928481), point1=(22.775114000000002,63.928481))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(42.414284,79.695805), point1=(49.727050000000006,79.695805))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(14.079453,75.267686), point1=(17.854660000000003,75.267686))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.104875,85.566829), point1=(9.746825,85.566829))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(17.217902,84.179587), point1=(22.746183,84.179587))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(29.476732,81.645565), point1=(33.095258,81.645565))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(42.455756,93.357427), point1=(48.371454,93.357427))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(3.258449,95.260381), point1=(6.117679000000001,95.260381))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.403405,92.848693), point1=(16.264823,92.848693))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(18.620146,96.599651), point1=(21.572969999999998,96.599651))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(25.838275,89.248382), point1=(28.919649,89.248382))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.305268,94.744762), point1=(33.760576,94.744762))
#
# ATRIBUINDO MATERIAL AS BOLINHAS
#
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ), 	sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(
    (( 10.884251 , 9.70274 ,    0.0),),
    (( 24.836193 , 6.277025 ,    0.0),),
    (( 44.26359 , 5.845128 ,    0.0),),
    (( 41.30236 , 20.794422 ,    0.0),),
    (( 36.940855 , 2.873181 ,    0.0),),
    (( 5.558564 , 25.093371 ,    0.0),),
    (( 21.388376 , 28.010412 ,    0.0),),
    (( 30.965233 , 18.161072 ,    0.0),),
    (( 34.815985 , 31.597999 ,    0.0),),
    (( 6.473431 , 43.497384 ,    0.0),),
    (( 9.644558 , 32.926606 ,    0.0),),
    (( 24.670634 , 44.461659 ,    0.0),),
    (( 40.559214 , 45.786513 ,    0.0),),
    (( 46.535521 , 30.130967 ,    0.0),),
    (( 5.820197 , 59.703067 ,    0.0),),
    (( 12.857696 , 52.356229 ,    0.0),),
    (( 30.446255 , 65.100389 ,    0.0),),
    (( 45.921744 , 38.286522 ,    0.0),),
    (( 32.812095 , 49.477887 ,    0.0),),
    (( 41.489274 , 54.317647 ,    0.0),),
    (( 4.239361 , 72.790662 ,    0.0),),
    (( 10.092571 , 68.468682 ,    0.0),),
    (( 16.075371 , 58.248903 ,    0.0),),
    (( 23.557651 , 73.818616 ,    0.0),),
    (( 19.907882 , 63.928481 ,    0.0),),
    (( 42.414284 , 79.695805 ,    0.0),),
    (( 14.079453 , 75.267686 ,    0.0),),
    (( 5.104875 , 85.566829 ,    0.0),),
    (( 17.217902 , 84.179587 ,    0.0),),
    (( 29.476732 , 81.645565 ,    0.0),),
    (( 42.455756 , 93.357427 ,    0.0),),
    (( 3.258449 , 95.260381 ,    0.0),),
    (( 12.403405 , 92.848693 ,    0.0),),
    (( 18.620146 , 96.599651 ,    0.0),),
    (( 25.838275 , 89.248382 ,    0.0),),
    (( 30.305268 , 94.744762 ,    0.0),),
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
    (( 10.884251 , 9.70274 ,    0.0),),
    (( 24.836193 , 6.277025 ,    0.0),),
    (( 44.26359 , 5.845128 ,    0.0),),
    (( 41.30236 , 20.794422 ,    0.0),),
    (( 36.940855 , 2.873181 ,    0.0),),
    (( 5.558564 , 25.093371 ,    0.0),),
    (( 21.388376 , 28.010412 ,    0.0),),
    (( 30.965233 , 18.161072 ,    0.0),),
    (( 34.815985 , 31.597999 ,    0.0),),
    (( 6.473431 , 43.497384 ,    0.0),),
    (( 9.644558 , 32.926606 ,    0.0),),
    (( 24.670634 , 44.461659 ,    0.0),),
    (( 40.559214 , 45.786513 ,    0.0),),
    (( 46.535521 , 30.130967 ,    0.0),),
    (( 5.820197 , 59.703067 ,    0.0),),
    (( 12.857696 , 52.356229 ,    0.0),),
    (( 30.446255 , 65.100389 ,    0.0),),
    (( 45.921744 , 38.286522 ,    0.0),),
    (( 32.812095 , 49.477887 ,    0.0),),
    (( 41.489274 , 54.317647 ,    0.0),),
    (( 4.239361 , 72.790662 ,    0.0),),
    (( 10.092571 , 68.468682 ,    0.0),),
    (( 16.075371 , 58.248903 ,    0.0),),
    (( 23.557651 , 73.818616 ,    0.0),),
    (( 19.907882 , 63.928481 ,    0.0),),
    (( 42.414284 , 79.695805 ,    0.0),),
    (( 14.079453 , 75.267686 ,    0.0),),
    (( 5.104875 , 85.566829 ,    0.0),),
    (( 17.217902 , 84.179587 ,    0.0),),
    (( 29.476732 , 81.645565 ,    0.0),),
    (( 42.455756 , 93.357427 ,    0.0),),
    (( 3.258449 , 95.260381 ,    0.0),),
    (( 12.403405 , 92.848693 ,    0.0),),
    (( 18.620146 , 96.599651 ,    0.0),),
    (( 25.838275 , 89.248382 ,    0.0),),
    (( 30.305268 , 94.744762 ,    0.0),),
))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=0.7)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 19.548920000000003 , 9.70274 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 30.313252000000002 , 6.277025 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 47.518009 , 5.845128 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 45.064611 , 20.794422 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 39.448589 , 2.873181 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 9.626628 , 25.093371 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 27.297235 , 28.010412 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 36.677901 , 18.161072 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 42.491474999999994 , 31.597999 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.400296 , 43.497384 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 12.368285 , 32.926606 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 30.952082 , 44.461659 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 44.420657999999996 , 45.786513 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.585795000000005 , 30.130967 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.511934 , 59.703067 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 15.594054 , 52.356229 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 36.636675 , 65.100389 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 48.669489 , 38.286522 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 35.650650999999996 , 49.477887 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 45.848656000000005 , 54.317647 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 7.953906 , 72.790662 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 13.237276999999999 , 68.468682 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 18.759847 , 58.248903 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 27.377343 , 73.818616 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 22.775114000000002 , 63.928481 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.727050000000006 , 79.695805 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 17.854660000000003 , 75.267686 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 9.746825 , 85.566829 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 22.746183 , 84.179587 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 33.095258 , 81.645565 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 48.371454 , 93.357427 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 6.117679000000001 , 95.260381 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 16.264823 , 92.848693 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 21.572969999999998 , 96.599651 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 28.919649 , 89.248382 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 33.760576 , 94.744762 ,    0.0),),), minSizeFactor=0.1, size=0.5)
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
