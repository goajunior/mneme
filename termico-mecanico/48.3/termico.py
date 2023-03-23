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
    center=(6.919308,4.708702), point1=(10.899474,4.708702))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(14.514517,5.846683), point1=(17.969825,5.846683))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(27.398474,5.361244), point1=(32.040424,5.361244))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(35.413537,10.475537), point1=(40.178052,10.475537))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(39.340788,95.283701), point1=(42.488566000000006,95.283701))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(46.170408,94.210584), point1=(49.213437,94.210584))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.27698,20.245891), point1=(9.663096,20.245891))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(9.568492,13.732793), point1=(12.109055000000001,13.732793))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(14.874695,18.254652), point1=(17.502841999999998,18.254652))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(17.746858,12.152931), point1=(20.535541,12.152931))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(25.937328,14.867302), point1=(30.864193,14.867302))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(45.424624,15.226389), point1=(49.818036,15.226389))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(46.026458,6.019104), point1=(48.865013999999995,6.019104))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(3.318303,28.49114), point1=(5.766216,28.49114))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(8.97305,30.769944), point1=(11.803344000000001,30.769944))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.585229,24.943239), point1=(15.535002,24.943239))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(18.728149,27.066844), point1=(21.475893999999997,27.066844))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(22.860307,23.097796), point1=(25.774071,23.097796))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(28.333117,27.734338), point1=(31.200349000000003,27.734338))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(32.291822,19.682191), point1=(34.817787,19.682191))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(46.336816,24.517231), point1=(49.183980999999996,24.517231))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.246097,38.047126), point1=(9.768481999999999,38.047126))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(14.616174,32.037203), point1=(17.510489,32.037203))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(15.602788,40.358542), point1=(18.119169,40.358542))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(26.622316,34.188459), point1=(29.70369,34.188459))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(27.165936,42.434252), point1=(30.208444,42.434252))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(36.331779,34.081323), point1=(40.09403,34.081323))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(46.248095,36.58024), point1=(49.342037,36.58024))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(6.199361,47.934404), point1=(10.124891,47.934404))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(13.384122,47.469275), point1=(16.096602999999998,47.469275))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(20.643801,43.132391), point1=(23.503031,43.132391))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(29.921788,49.602312), point1=(33.783232,49.602312))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(32.87281,40.199497), point1=(35.406951,40.199497))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(41.379385,43.507024), point1=(46.065833,43.507024))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(3.207248,53.826926), point1=(5.8899170000000005,53.826926))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(5.913459,58.987986), point1=(8.963733,58.987986))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.69955,54.874998), point1=(16.318076,54.874998))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(19.751618,50.698879), point1=(24.038873000000002,50.698879))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(31.847372,56.298596), point1=(34.571099,56.298596))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(38.335116,56.037459), point1=(41.479822,56.037459))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(45.443078,54.139098), point1=(49.26277,54.139098))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(6.868628,67.387664), point1=(9.858876,67.387664))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(16.891766,66.120385), point1=(20.606311,66.120385))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.158996,61.652701), point1=(14.589881,61.652701))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(20.095581,59.105538), point1=(23.096413,59.105538))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(24.191825,63.545272), point1=(27.019223,63.545272))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(31.476387,65.238595), point1=(34.263976,65.238595))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(43.867374,68.271875), point1=(49.107881,68.271875))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(4.284536,72.954003), point1=(7.279955,72.954003))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(17.933817,78.985933), point1=(22.110663000000002,78.985933))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(21.451046,71.485678), point1=(24.097625,71.485678))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(26.571102,77.251591), point1=(29.399902,77.251591))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(28.845636,70.679884), point1=(31.353369999999998,70.679884))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(34.821992,69.984515), point1=(37.838204000000005,69.984515))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(39.298942,76.255243), point1=(43.074149,76.255243))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(47.41089,75.461089), point1=(49.898422000000004,75.461089))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(4.526426,85.055083), point1=(8.387844,85.055083))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(11.476451,83.851041), point1=(14.257841,83.851041))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(20.905506,88.33468), point1=(25.264888,88.33468))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(25.095641,82.829512), point1=(27.527189,82.829512))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(28.444741,87.527562), point1=(31.553549,87.527562))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(33.699451,81.755032), point1=(36.349819000000004,81.755032))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(35.396254,87.504322), point1=(38.132612,87.504322))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(41.079391,85.202563), point1=(43.763867000000005,85.202563))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(3.994296,92.552552), point1=(7.248715,92.552552))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(12.176407,93.922768), point1=(16.330927,93.922768))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(22.255732,96.19935), point1=(25.080999,96.19935))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(
    center=(29.617144,94.398051), point1=(32.569968,94.398051))
#
# ATRIBUINDO MATERIAL AS BOLINHAS
#
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ), 	sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(
    (( 6.919308 , 4.708702 ,    0.0),),
    (( 14.514517 , 5.846683 ,    0.0),),
    (( 27.398474 , 5.361244 ,    0.0),),
    (( 35.413537 , 10.475537 ,    0.0),),
    (( 39.340788 , 95.283701 ,    0.0),),
    (( 46.170408 , 94.210584 ,    0.0),),
    (( 5.27698 , 20.245891 ,    0.0),),
    (( 9.568492 , 13.732793 ,    0.0),),
    (( 14.874695 , 18.254652 ,    0.0),),
    (( 17.746858 , 12.152931 ,    0.0),),
    (( 25.937328 , 14.867302 ,    0.0),),
    (( 45.424624 , 15.226389 ,    0.0),),
    (( 46.026458 , 6.019104 ,    0.0),),
    (( 3.318303 , 28.49114 ,    0.0),),
    (( 8.97305 , 30.769944 ,    0.0),),
    (( 12.585229 , 24.943239 ,    0.0),),
    (( 18.728149 , 27.066844 ,    0.0),),
    (( 22.860307 , 23.097796 ,    0.0),),
    (( 28.333117 , 27.734338 ,    0.0),),
    (( 32.291822 , 19.682191 ,    0.0),),
    (( 46.336816 , 24.517231 ,    0.0),),
    (( 5.246097 , 38.047126 ,    0.0),),
    (( 14.616174 , 32.037203 ,    0.0),),
    (( 15.602788 , 40.358542 ,    0.0),),
    (( 26.622316 , 34.188459 ,    0.0),),
    (( 27.165936 , 42.434252 ,    0.0),),
    (( 36.331779 , 34.081323 ,    0.0),),
    (( 46.248095 , 36.58024 ,    0.0),),
    (( 6.199361 , 47.934404 ,    0.0),),
    (( 13.384122 , 47.469275 ,    0.0),),
    (( 20.643801 , 43.132391 ,    0.0),),
    (( 29.921788 , 49.602312 ,    0.0),),
    (( 32.87281 , 40.199497 ,    0.0),),
    (( 41.379385 , 43.507024 ,    0.0),),
    (( 3.207248 , 53.826926 ,    0.0),),
    (( 5.913459 , 58.987986 ,    0.0),),
    (( 12.69955 , 54.874998 ,    0.0),),
    (( 19.751618 , 50.698879 ,    0.0),),
    (( 31.847372 , 56.298596 ,    0.0),),
    (( 38.335116 , 56.037459 ,    0.0),),
    (( 45.443078 , 54.139098 ,    0.0),),
    (( 6.868628 , 67.387664 ,    0.0),),
    (( 16.891766 , 66.120385 ,    0.0),),
    (( 12.158996 , 61.652701 ,    0.0),),
    (( 20.095581 , 59.105538 ,    0.0),),
    (( 24.191825 , 63.545272 ,    0.0),),
    (( 31.476387 , 65.238595 ,    0.0),),
    (( 43.867374 , 68.271875 ,    0.0),),
    (( 4.284536 , 72.954003 ,    0.0),),
    (( 17.933817 , 78.985933 ,    0.0),),
    (( 21.451046 , 71.485678 ,    0.0),),
    (( 26.571102 , 77.251591 ,    0.0),),
    (( 28.845636 , 70.679884 ,    0.0),),
    (( 34.821992 , 69.984515 ,    0.0),),
    (( 39.298942 , 76.255243 ,    0.0),),
    (( 47.41089 , 75.461089 ,    0.0),),
    (( 4.526426 , 85.055083 ,    0.0),),
    (( 11.476451 , 83.851041 ,    0.0),),
    (( 20.905506 , 88.33468 ,    0.0),),
    (( 25.095641 , 82.829512 ,    0.0),),
    (( 28.444741 , 87.527562 ,    0.0),),
    (( 33.699451 , 81.755032 ,    0.0),),
    (( 35.396254 , 87.504322 ,    0.0),),
    (( 41.079391 , 85.202563 ,    0.0),),
    (( 3.994296 , 92.552552 ,    0.0),),
    (( 12.176407 , 93.922768 ,    0.0),),
    (( 22.255732 , 96.19935 ,    0.0),),
    (( 29.617144 , 94.398051 ,    0.0),),
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
    (( 6.919308 , 4.708702 ,    0.0),),
    (( 14.514517 , 5.846683 ,    0.0),),
    (( 27.398474 , 5.361244 ,    0.0),),
    (( 35.413537 , 10.475537 ,    0.0),),
    (( 39.340788 , 95.283701 ,    0.0),),
    (( 46.170408 , 94.210584 ,    0.0),),
    (( 5.27698 , 20.245891 ,    0.0),),
    (( 9.568492 , 13.732793 ,    0.0),),
    (( 14.874695 , 18.254652 ,    0.0),),
    (( 17.746858 , 12.152931 ,    0.0),),
    (( 25.937328 , 14.867302 ,    0.0),),
    (( 45.424624 , 15.226389 ,    0.0),),
    (( 46.026458 , 6.019104 ,    0.0),),
    (( 3.318303 , 28.49114 ,    0.0),),
    (( 8.97305 , 30.769944 ,    0.0),),
    (( 12.585229 , 24.943239 ,    0.0),),
    (( 18.728149 , 27.066844 ,    0.0),),
    (( 22.860307 , 23.097796 ,    0.0),),
    (( 28.333117 , 27.734338 ,    0.0),),
    (( 32.291822 , 19.682191 ,    0.0),),
    (( 46.336816 , 24.517231 ,    0.0),),
    (( 5.246097 , 38.047126 ,    0.0),),
    (( 14.616174 , 32.037203 ,    0.0),),
    (( 15.602788 , 40.358542 ,    0.0),),
    (( 26.622316 , 34.188459 ,    0.0),),
    (( 27.165936 , 42.434252 ,    0.0),),
    (( 36.331779 , 34.081323 ,    0.0),),
    (( 46.248095 , 36.58024 ,    0.0),),
    (( 6.199361 , 47.934404 ,    0.0),),
    (( 13.384122 , 47.469275 ,    0.0),),
    (( 20.643801 , 43.132391 ,    0.0),),
    (( 29.921788 , 49.602312 ,    0.0),),
    (( 32.87281 , 40.199497 ,    0.0),),
    (( 41.379385 , 43.507024 ,    0.0),),
    (( 3.207248 , 53.826926 ,    0.0),),
    (( 5.913459 , 58.987986 ,    0.0),),
    (( 12.69955 , 54.874998 ,    0.0),),
    (( 19.751618 , 50.698879 ,    0.0),),
    (( 31.847372 , 56.298596 ,    0.0),),
    (( 38.335116 , 56.037459 ,    0.0),),
    (( 45.443078 , 54.139098 ,    0.0),),
    (( 6.868628 , 67.387664 ,    0.0),),
    (( 16.891766 , 66.120385 ,    0.0),),
    (( 12.158996 , 61.652701 ,    0.0),),
    (( 20.095581 , 59.105538 ,    0.0),),
    (( 24.191825 , 63.545272 ,    0.0),),
    (( 31.476387 , 65.238595 ,    0.0),),
    (( 43.867374 , 68.271875 ,    0.0),),
    (( 4.284536 , 72.954003 ,    0.0),),
    (( 17.933817 , 78.985933 ,    0.0),),
    (( 21.451046 , 71.485678 ,    0.0),),
    (( 26.571102 , 77.251591 ,    0.0),),
    (( 28.845636 , 70.679884 ,    0.0),),
    (( 34.821992 , 69.984515 ,    0.0),),
    (( 39.298942 , 76.255243 ,    0.0),),
    (( 47.41089 , 75.461089 ,    0.0),),
    (( 4.526426 , 85.055083 ,    0.0),),
    (( 11.476451 , 83.851041 ,    0.0),),
    (( 20.905506 , 88.33468 ,    0.0),),
    (( 25.095641 , 82.829512 ,    0.0),),
    (( 28.444741 , 87.527562 ,    0.0),),
    (( 33.699451 , 81.755032 ,    0.0),),
    (( 35.396254 , 87.504322 ,    0.0),),
    (( 41.079391 , 85.202563 ,    0.0),),
    (( 3.994296 , 92.552552 ,    0.0),),
    (( 12.176407 , 93.922768 ,    0.0),),
    (( 22.255732 , 96.19935 ,    0.0),),
    (( 29.617144 , 94.398051 ,    0.0),),
))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=0.7)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 10.899474 , 4.708702 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 17.969825 , 5.846683 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 32.040424 , 5.361244 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 40.178052 , 10.475537 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 42.488566000000006 , 95.283701 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.213437 , 94.210584 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 9.663096 , 20.245891 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 12.109055000000001 , 13.732793 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 17.502841999999998 , 18.254652 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 20.535541 , 12.152931 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 30.864193 , 14.867302 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.818036 , 15.226389 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 48.865013999999995 , 6.019104 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 5.766216 , 28.49114 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 11.803344000000001 , 30.769944 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 15.535002 , 24.943239 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 21.475893999999997 , 27.066844 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.774071 , 23.097796 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 31.200349000000003 , 27.734338 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 34.817787 , 19.682191 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.183980999999996 , 24.517231 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 9.768481999999999 , 38.047126 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 17.510489 , 32.037203 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 18.119169 , 40.358542 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 29.70369 , 34.188459 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 30.208444 , 42.434252 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 40.09403 , 34.081323 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.342037 , 36.58024 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 10.124891 , 47.934404 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 16.096602999999998 , 47.469275 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 23.503031 , 43.132391 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 33.783232 , 49.602312 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 35.406951 , 40.199497 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 46.065833 , 43.507024 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 5.8899170000000005 , 53.826926 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 8.963733 , 58.987986 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 16.318076 , 54.874998 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 24.038873000000002 , 50.698879 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 34.571099 , 56.298596 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 41.479822 , 56.037459 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.26277 , 54.139098 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 9.858876 , 67.387664 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 20.606311 , 66.120385 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 14.589881 , 61.652701 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 23.096413 , 59.105538 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 27.019223 , 63.545272 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 34.263976 , 65.238595 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.107881 , 68.271875 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 7.279955 , 72.954003 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 22.110663000000002 , 78.985933 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 24.097625 , 71.485678 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 29.399902 , 77.251591 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 31.353369999999998 , 70.679884 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 37.838204000000005 , 69.984515 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 43.074149 , 76.255243 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 49.898422000000004 , 75.461089 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 8.387844 , 85.055083 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 14.257841 , 83.851041 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.264888 , 88.33468 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 27.527189 , 82.829512 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 31.553549 , 87.527562 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 36.349819000000004 , 81.755032 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 38.132612 , 87.504322 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 43.763867000000005 , 85.202563 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 7.248715 , 92.552552 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 16.330927 , 93.922768 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 25.080999 , 96.19935 ,    0.0),),), minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(constraint=FINER,
    deviationFactor=0.1, edges = mdb.models['Model-1'].parts['Part-1'].edges.findAt(
        (( 32.569968 , 94.398051 ,    0.0),),), minSizeFactor=0.1, size=0.5)
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
