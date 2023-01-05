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
    center=(38.285306,12.227651), point1=(42.05345,12.227651))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(39.660656,28.815599), point1=(42.805844,28.815599))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(17.64471,27.426056), point1=(20.620204,27.426056))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(42.908512,19.278955), point1=(46.490975,19.278955))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(25.249145,19.390258), point1=(28.328314,19.390258))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(11.987949,40.572774), point1=(16.680243,40.572774))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(16.668667,8.793118), point1=(19.462315999999998,8.793118))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(22.364745,43.258362), point1=(26.335860999999998,43.258362))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(44.341162,40.042173), point1=(47.946467999999996,40.042173))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(35.576316,96.367882), point1=(38.184267999999996,96.367882))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(7.078427,68.196779), point1=(11.156682,68.196779))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(22.277725,14.536431), point1=(24.755019,14.536431))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(27.016788,57.277905), point1=(29.695200999999997,57.277905))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(15.573074,16.891585), point1=(18.647761,16.891585))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(29.645937,32.818306), point1=(32.216532,32.818306))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(14.849809,94.342912), point1=(20.251276,94.342912))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(21.962143,61.793839), point1=(25.386356,61.793839))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(42.882204,62.940395), point1=(45.294179,62.940395))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(30.770991,67.110328), point1=(33.207921,67.110328))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(22.465083,73.060264), point1=(25.241878,73.060264))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(29.123488,47.857902), point1=(32.129090999999995,47.857902))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(9.106079,31.958754), point1=(11.876386,31.958754))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(13.662949,82.028915), point1=(17.077821,82.028915))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.180505,58.024054), point1=(14.610467,58.024054))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(25.173012,80.60692), point1=(28.164113,80.60692))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(3.723845,93.739676), point1=(6.386018,93.739676))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(32.322523,88.463372), point1=(34.945755,88.463372))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(28.150192,94.480741), point1=(31.359058,94.480741))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(40.709039,83.802939), point1=(43.323994,83.802939))
#
# ATRIBUINDO MATERIAL AS BOLINHAS
#
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ), 	sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(
    (( 38.285306 , 12.227651 ,    0.0),),
    (( 39.660656 , 28.815599 ,    0.0),),
    (( 17.64471 , 27.426056 ,    0.0),),
    (( 42.908512 , 19.278955 ,    0.0),),
    (( 25.249145 , 19.390258 ,    0.0),),
    (( 11.987949 , 40.572774 ,    0.0),),
    (( 16.668667 , 8.793118 ,    0.0),),
    (( 22.364745 , 43.258362 ,    0.0),),
    (( 44.341162 , 40.042173 ,    0.0),),
    (( 35.576316 , 96.367882 ,    0.0),),
    (( 7.078427 , 68.196779 ,    0.0),),
    (( 22.277725 , 14.536431 ,    0.0),),
    (( 27.016788 , 57.277905 ,    0.0),),
    (( 15.573074 , 16.891585 ,    0.0),),
    (( 29.645937 , 32.818306 ,    0.0),),
    (( 14.849809 , 94.342912 ,    0.0),),
    (( 21.962143 , 61.793839 ,    0.0),),
    (( 42.882204 , 62.940395 ,    0.0),),
    (( 30.770991 , 67.110328 ,    0.0),),
    (( 22.465083 , 73.060264 ,    0.0),),
    (( 29.123488 , 47.857902 ,    0.0),),
    (( 9.106079 , 31.958754 ,    0.0),),
    (( 13.662949 , 82.028915 ,    0.0),),
    (( 12.180505 , 58.024054 ,    0.0),),
    (( 25.173012 , 80.60692 ,    0.0),),
    (( 3.723845 , 93.739676 ,    0.0),),
    (( 32.322523 , 88.463372 ,    0.0),),
    (( 28.150192 , 94.480741 ,    0.0),),
    (( 40.709039 , 83.802939 ,    0.0),),
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
    (( 38.285306 , 12.227651 ,    0.0),),
    (( 39.660656 , 28.815599 ,    0.0),),
    (( 17.64471 , 27.426056 ,    0.0),),
    (( 42.908512 , 19.278955 ,    0.0),),
    (( 25.249145 , 19.390258 ,    0.0),),
    (( 11.987949 , 40.572774 ,    0.0),),
    (( 16.668667 , 8.793118 ,    0.0),),
    (( 22.364745 , 43.258362 ,    0.0),),
    (( 44.341162 , 40.042173 ,    0.0),),
    (( 35.576316 , 96.367882 ,    0.0),),
    (( 7.078427 , 68.196779 ,    0.0),),
    (( 22.277725 , 14.536431 ,    0.0),),
    (( 27.016788 , 57.277905 ,    0.0),),
    (( 15.573074 , 16.891585 ,    0.0),),
    (( 29.645937 , 32.818306 ,    0.0),),
    (( 14.849809 , 94.342912 ,    0.0),),
    (( 21.962143 , 61.793839 ,    0.0),),
    (( 42.882204 , 62.940395 ,    0.0),),
    (( 30.770991 , 67.110328 ,    0.0),),
    (( 22.465083 , 73.060264 ,    0.0),),
    (( 29.123488 , 47.857902 ,    0.0),),
    (( 9.106079 , 31.958754 ,    0.0),),
    (( 13.662949 , 82.028915 ,    0.0),),
    (( 12.180505 , 58.024054 ,    0.0),),
    (( 25.173012 , 80.60692 ,    0.0),),
    (( 3.723845 , 93.739676 ,    0.0),),
    (( 32.322523 , 88.463372 ,    0.0),),
    (( 28.150192 , 94.480741 ,    0.0),),
    (( 40.709039 , 83.802939 ,    0.0),),
))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=0.7)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 42.05345 , 12.227651 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 42.805844 , 28.815599 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 20.620204 , 27.426056 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 46.490975 , 19.278955 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 28.328314 , 19.390258 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 16.680243 , 40.572774 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 19.462315999999998 , 8.793118 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 26.335860999999998 , 43.258362 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 47.946467999999996 , 40.042173 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 38.184267999999996 , 96.367882 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.156682 , 68.196779 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 24.755019 , 14.536431 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 29.695200999999997 , 57.277905 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 18.647761 , 16.891585 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 32.216532 , 32.818306 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 20.251276 , 94.342912 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.386356 , 61.793839 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 45.294179 , 62.940395 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 33.207921 , 67.110328 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.241878 , 73.060264 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 32.129090999999995 , 47.857902 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.876386 , 31.958754 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 17.077821 , 82.028915 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 14.610467 , 58.024054 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 28.164113 , 80.60692 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 6.386018 , 93.739676 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 34.945755 , 88.463372 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 31.359058 , 94.480741 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 43.323994 , 83.802939 ,    0.0),),), minSizeFactor=0.1, size=0.5)
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
