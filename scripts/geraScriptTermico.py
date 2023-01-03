# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import argparse


parser = argparse.ArgumentParser(usage=__doc__)

# Definicao dos percentuais de varredura (geracao dos arquivos)

parser.add_argument(
    "--file", type=string, help="arquivo de entrada"
)

args = parser.parse_args()

filename = args.file
Diam = 50.0
H = 100.0

c1 = 0
c2 = Diam
c3 = Diam/2.0
c4 = H
c5 = -1. * c2

texto1 = '# -*- coding: utf-8 -*-'
texto2 = 'from part import *'
texto3 = 'from material import *'
texto4 = 'from section import *'
texto5 = 'from assembly import *'
texto6 = 'from step import *'
texto7 = 'from interaction import *'
texto8 = 'from load import *'
texto9 = 'from mesh import *'
texto10 = 'from optimization import *'
texto11 = 'from job import *'
texto12 = 'from sketch import *'
texto13 = 'from visualization import *'
texto14 = 'from connectorBehavior import *'
texto15 = 'import numpy as np'
texto16 = 'import os'
texto17 = '#'
texto18 = 'if os.path.isfile("termico.odb"):'
texto19 = '     os.remove("termico.odb")'
texto20 = 'if os.path.isfile("termico.lck"):'
texto21 = '       os.remove("termico.lck")'
texto22= '#'
texto23= '#'
texto24= '#'
texto25= '#'
texto26= '#'
texto27= '#'
texto28 = '#'
texto29 = "os.system('C:\\Temp\\termico.*')"
texto30 = 'temperaturas = [293.15, 573.15, 723.15, 873.15]'
texto31= '#'
texto32= '#'
texto33= '#'
texto34 = '# DEFINE TIME PERIOD E INCREMENT SIZE'
texto35 = '#'
texto36 = 'time_period573 = 560'
texto37 = 'time_period723 = 300'
texto38 = 'time_period873 = 300'
texto39 = 'increment_size = 1'
texto40 = 'max_inc = int(time_period573/increment_size + time_period723/increment_size + time_period873/increment_size)'
texto41 = 'malha_agreg = 0.002*1e3'
texto42 = 'malha_arg = 0.002*1e3'
texto43 = '#'
texto44 = '# DEFINE PROPRIEDADES DOS MATERIAIS'
texto45 = '#'
texto46 = '# obs: propriedades termicas nbr 15220'
texto47= '#'
texto48= '#'
texto49= '#'
texto50= '#'
texto51 = "param_argamass = {'Density': 2252.0*1e-9, 'Conductivity': 1.15*60*1e-3, 'SpecificHeat': 1000.0, 'Expansion': 3.67e-6}"
texto52= '#'
texto53 = "param_agreg = {'Density': 2500.0*1e-9, 'Conductivity': 0.7*60*1e-3, 'SpecificHeat': 840.0, 'Expansion': 3.779e-6}"
texto54= '#'
texto55 = "#"
texto56 = "#"
texto57 = "#"
texto58 = "# CRIA RETANGULO"
texto59 = "#"
texto60 = "mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)"
texto61 = "mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues("
texto62 = "    viewStyle=AXISYM)"
texto63 = "mdb.models['Model-1'].sketches['__profile__'].ConstructionLine("
texto64 = "    point1=(0.0, 0.0), point2=(0.0, 1.0))"
texto65 = "mdb.models['Model-1'].sketches['__profile__'].FixedConstraint("
texto66 = "    entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])"
texto67 = "mdb.models['Model-1'].sketches['__profile__'].rectangle("
texto68 = "    point1=("+str(c1)+","+str(c1) + "), point2=("+str(c2)+","+str(c4)+"))"
texto69 = "mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR,"
texto70 = "                           name='Part-1', type=DEFORMABLE_BODY)"
texto71 = "mdb.models['Model-1'].parts['Part-1'].BaseShell("
texto72 = "    sketch=mdb.models['Model-1'].sketches['__profile__'])"
texto73 = "del mdb.models['Model-1'].sketches['__profile__']"
texto74 = "#"
texto75 = "# CRIA MATERIAIS E ATRIBUI AO RETANGULO"
texto76 = "#"
texto77 = "mdb.models['Model-1'].Material(name='Material-argamassa')"
texto78 = "mdb.models['Model-1'].materials['Material-argamassa'].Density(table=((param_argamass['Density'], ), ))"
texto79 = "mdb.models['Model-1'].materials['Material-argamassa'].Conductivity(table=((param_argamass['Conductivity'], ), ))"
texto80 = "mdb.models['Model-1'].materials['Material-argamassa'].SpecificHeat(table=((param_argamass['SpecificHeat'], ), ))"
texto81 = "mdb.models['Model-1'].materials['Material-argamassa'].Expansion(table=((param_argamass['Expansion'], ), ))"
texto82 = "mdb.models['Model-1'].materials['Material-argamassa'].expansion.setValues(zero=temperaturas[0])"
texto83 = "#"
texto84 = "mdb.models['Model-1'].Material(name='Material-agregado')"
texto85 = "mdb.models['Model-1'].materials['Material-agregado'].Density(table=((param_agreg['Density'], ), ))"
texto86 = "mdb.models['Model-1'].materials['Material-agregado'].Conductivity(table=((param_agreg['Conductivity'], ), ))"
texto87 = "mdb.models['Model-1'].materials['Material-agregado'].SpecificHeat(table=((param_agreg['SpecificHeat'], ), ))"
texto88 = "mdb.models['Model-1'].materials['Material-agregado'].Expansion(table=((param_agreg['Expansion'], ), ))"
texto89 = "mdb.models['Model-1'].materials['Material-agregado'].expansion.setValues(zero=temperaturas[0])"
texto90 = "#"
texto91 = "mdb.models['Model-1'].HomogeneousSolidSection(material='Material-argamassa',"
texto92 = "    name='Section-argamassa', thickness=None)"
texto93 = "mdb.models['Model-1'].HomogeneousSolidSection(material='Material-argamassa',"
texto94 = "    name='Section-ZTI', thickness=None)"
texto95 = "mdb.models['Model-1'].HomogeneousSolidSection(material='Material-agregado',"
texto96 = "    name='Section-agregado', thickness=None)"
texto97 = "mdb.models['Model-1'].parts['Part-1'].Set(faces="
texto98 = "    mdb.models['Model-1'].parts['Part-1'].faces.findAt(((1.0, 1.0,"
texto99 = "   0.0), (0.0, 0.0, 1.0)), ), name='Set-1')"
texto100 = "mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,"
texto101 = "    offsetField='', offsetType=MIDDLE_SURFACE, region="
texto102 = "    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName="
texto103 = "    'Section-argamassa', thicknessAssignment=FROM_SECTION)"
texto104 = "mdb.models['Model-1'].ConstrainedSketch(gridSpacing=5.59, name='__profile__',"
texto105 = "     sheetSize=223.6, transform="
texto106 = "     mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform("
texto107 = "     sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0],"
texto108 = "     sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))"
texto109 = "mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter="
texto110 = "     COPLANAR_EDGES,"
texto111 = "sketch=mdb.models['Model-1'].sketches['__profile__'])"
texto112 = "#"
texto113 = "mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models['Model-1'].parts['Part-1'].sets['Set-1'])"
texto114 = "#"
texto115 = "# CRIANDO AS BOLINHAS"
texto116 = "#"

v = np.loadtxt(filename)

R = v[:, 2]
G = v[:, (0, 1)]

xx = G[:, 0] + R
yy = G[:, 1] + R

n = len(R)
i=116

for k in range(0, n):
    globals()['texto'+str(i)] = "mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter("
    i=i+1
    globals()['texto'+str(i)] = "    center=("+str(G[k, 0])+","+str(G[k, 1])+"), point1=("+str(xx[k])+","+str(G[k, 1])+"))"
    i=i+1

textFile = open("termico.py", "w")
for j in range(1, i):
    textFile.write(globals()['texto'+str(j)])
    textFile.write('\n')

texto_a_1 = "#"
texto_a_2 = "# ATRIBUINDO MATERIAL AS BOLINHAS"
texto_a_3 = "#"
texto_a_4 = "mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask("
texto_a_5 = "    ('[#1 ]', ), ), 	sketch=mdb.models['Model-1'].sketches['__profile__'])"
texto_a_6 = "del mdb.models['Model-1'].sketches['__profile__']"
texto_a_7 = "mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt("

q = 1
a = 1
p = 1
i=8

for k in range(0, n):
    if (q <= 254):
        globals()['texto_a_'+str(i)] = "    (( "+str(G[k, 0])+" , "+str(G[k, 1])+" ,    0.0),),"
        i=i+1
        a = a+1
    elif (a < 508):
        globals()['texto_a_'+str(i)] =" ),name=\'Set-2\')"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
        i=i+1
        globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-2\'], sectionName="
        i=i+1
        globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models['Model-1'].parts['Part-1'].sets['Set-3'])"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].Set(faces="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
        i=i+1
        globals()['texto_a_'+str(i)] = "    (( "+str(G[k, 0])+" , "+str(G[k, 1])+" ,    0.0),),"
        i=i+1
        q = 0
        p = 10
    elif (a < 762):
        globals()['texto_a_'+str(i)] =" ),name=\'Set-3\')"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
        i=i+1
        globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'], sectionName="
        i=i+1
        globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'])"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].Set(faces="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
        i=i+1
        globals()['texto_a_'+str(i)] = "    (( "+str(G[k, 0])+" , "+str(G[k, 1])+" ,    0.0),),"
        i=i+1
        q = 0
    else:
        globals()['texto_a_'+str(i)] =" ),name=\'Set-4\')"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
        i=i+1
        globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'], sectionName="
        i=i+1
        globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'])"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].Set(faces="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
        i=i+1
        globals()['texto_a_'+str(i)] = "    (( "+str(G[k, 0])+" , "+str(G[k, 1])+" ,    0.0),),"
        i=i+1
        q = 0
    
    q = q+1

if a < 510:
    globals()['texto_a_'+str(i)] =" ),name=\'Set-3\')"
    i=i+1
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
    i=i+1
    globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
    i=i+1
    globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'], sectionName="
    i=i+1
    globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
    i=i+1
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'])"
    i=i+1
    globals()['texto_a_'+str(i)] ="#"
    i=i+1
    globals()['texto_a_'+str(i)] ="#CRIANDO MALHA"
    i=i+1
    globals()['texto_a_'+str(i)] ="#"
    i=i+1
    globals()['texto_a_'+str(i)] ="mdb.models[\'Model-1\'].parts[\'Part-1\'].setMeshControls(elemShape=TRI, regions="
    i=i+1
    globals()['texto_a_'+str(i)] ="    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
    i=i+1

if a > 510:
    if a < 766:
        globals()['texto_a_'+str(i)] =" ),name=\'Set-4\')"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
        i=i+1
        globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'], sectionName="
        i=i+1
        globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'])"
        i=i+1
        globals()['texto_a_'+str(i)] ="#"
        i=i+1
        globals()['texto_a_'+str(i)] ="#CRIANDO MALHA"
        i=i+1
        globals()['texto_a_'+str(i)] ="#"
        i=i+1
        globals()['texto_a_'+str(i)] ="mdb.models[\'Model-1\'].parts[\'Part-1\'].setMeshControls(elemShape=TRI, regions="
        i=i+1
        globals()['texto_a_'+str(i)] ="    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
        i=i+1

if a > 765:
    globals()['texto_a_'+str(i)] =" ),name=\'Set-5\')"
    i=i+1
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].SectionAssignment(offset=0.0,"
    i=i+1
    globals()['texto_a_'+str(i)] = "    offsetField=\'\', offsetType=MIDDLE_SURFACE, region="
    i=i+1
    globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-5\'], sectionName="
    i=i+1
    globals()['texto_a_'+str(i)] = "    \'Section-agregado\', thicknessAssignment=FROM_SECTION)"
    i=i+1
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=DC2D4, elemLibrary=STANDARD), ElemType(elemCode=DC2D3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-5\'])"
    i=i+1
    globals()['texto_a_'+str(i)] ="#"
    i=i+1
    globals()['texto_a_'+str(i)] ="#CRIANDO MALHA"
    i=i+1
    globals()['texto_a_'+str(i)] ="#"
    i=i+1
    globals()['texto_a_'+str(i)] ="mdb.models[\'Model-1\'].parts[\'Part-1\'].setMeshControls(elemShape=TRI, regions="
    i=i+1
    globals()['texto_a_'+str(i)] ="    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
    i=i+1

q = 1

for k in range(0, n):
    if (q <= 255):
        globals()['texto_a_'+str(i)] = "    (( "+str(G[k, 0])+" , "+str(G[k, 1])+" ,    0.0),),"
        i=i+1
    else:
        globals()['texto_a_'+str(i)] = "))"
        i=i+1
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setMeshControls(elemShape=TRI, regions="
        i=i+1
        globals()['texto_a_'+str(i)] = "    mdb.models[\'Model-1\'].parts[\'Part-1\'].faces.findAt("
        i=i+1
        q=0
    q = q+1

globals()['texto_a_'+str(i)] ="))"
i=i+1
globals()['texto_a_'+str(i)] ="mdb.models[\'Model-1\'].parts[\'Part-1\'].seedPart(deviationFactor=0.1,"
i=i+1
globals()['texto_a_'+str(i)] ="    minSizeFactor=0.1, size=0.7)"
i=i+1

tamanho = np.zeros(n)

for k in range(0, n):
    tamanho[k] = 0.5  # abs((1/2)*(R(k,1)+G(k,1)));
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].seedEdgeBySize(constraint=FINER,"
    i=i+1
    globals()['texto_a_'+str(i)] = "    deviationFactor=0.1, edges = mdb.models[\'Model-1\'].parts[\'Part-1\'].edges.findAt("
    i=i+1
    globals()['texto_a_'+str(i)] = "        (( "+str(xx[k])+" , "+str(G[k,1])+" ,    0.0),),), minSizeFactor=0.1, size="+str(tamanho[k])+")"
    i=i+1


globals()['texto_a_'+str(i)] ="mdb.models[\'Model-1\'].parts[\'Part-1\'].generateMesh()"
i=i+1
globals()['texto_a_'+str(i)] ="#"
i=i+1

for j in range(1, i):
    textFile.write(globals()['texto_a_'+str(j)])
    textFile.write('\n')


texto_b_1 = "# FAZ O ASSEMBLY, CRIANDO OS PONTOS DE CONTROLE E AS CONDIÇÕES DE CONTORNO"
texto_b_2 = "#"
texto_b_3 = "mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)"
texto_b_4 = "mdb.models['Model-1'].rootAssembly.Instance("
texto_b_5 = "    dependent=ON, name='Part-1-1', part=mdb.models['Model-1'].parts['Part-1'])"
texto_b_6 = "mdb.models['Model-1'].rootAssembly.Set("
texto_b_7 = "    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((0.0 , "+str(Diam)+" , 0.0),), ), name='Lateral1')"
texto_b_8 = "mdb.models['Model-1'].rootAssembly.Set("
texto_b_9 = "    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt((( "+str(Diam)+' , '+str(Diam)+" , 0.0),), ), name='Lateral2')"
texto_b_10 = "mdb.models['Model-1'].rootAssembly.Set("
texto_b_11 = "    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((1*1e-3, 0.0, 0.0),), ), name='Base')"
texto_b_12 = "mdb.models['Model-1'].rootAssembly.Set("
texto_b_13 = "    edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.findAt(((1*1e-3 , "+str(H)+" , 0.0),), ), name='Topo')"
texto_b_14 = "#"
texto_b_15 = "# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((17.431429 , 57.588253, 0.0),), ), name='Ponto3')"
texto_b_16 = "# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((23.388278 , 95.099907, 0.0),), ), name='Ponto2')"
texto_b_17 = "# mdb.models['Model-1'].rootAssembly.Set(vertices=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((50.0, 100.0 , 0.0),), ), name='Ponto1')"
texto_b_18 = "#"
texto_b_19 = "# aplica temperatura inicial"
texto_b_20 = "mdb.models['Model-1'].Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=temperaturas[0],"
texto_b_21 = "  name='Temperatura Inicial', region=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Set-1'])"
texto_b_22 = "#"
texto_b_23 = "#"
texto_b_24 = "#"
texto_b_25 = "#"
texto_b_26 = "#"
texto_b_27 = "#"
texto_b_28 = "#"
texto_b_29 = "#step1 - carga573"
texto_b_30 = "mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga573', previous='Initial', timeIncrementationMethod=FIXED, timePeriod=time_period573, amplitude=RAMP)"
texto_b_31 = "mdb.models['Model-1'].TemperatureBC(amplitude=UNSET, createStepName='Carga573', distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=temperaturas[1], name='Temp-' + str(1), region=mdb.models['Model-1'].rootAssembly.sets['Lateral2'])"
texto_b_32 = "mdb.models['Model-1'].TemperatureBC(amplitude=UNSET, createStepName='Carga573', distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=temperaturas[1], name='Temp-' + str(2), region=mdb.models['Model-1'].rootAssembly.sets['Topo'])"
texto_b_33 = "#"
texto_b_34 = "#"
texto_b_35 = "#"
texto_b_36 = "#step2 - carga723"
texto_b_37 = "mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga723', previous='Carga573', timeIncrementationMethod=FIXED, "
texto_b_38 = "    timePeriod=time_period723, amplitude=RAMP)"
texto_b_39 = "mdb.models['Model-1'].boundaryConditions['Temp-' + str(1)].setValuesInStep(magnitude=temperaturas[2], stepName='Carga723')"
texto_b_40 = "mdb.models['Model-1'].boundaryConditions['Temp-' + str(2)].setValuesInStep(magnitude=temperaturas[2], stepName='Carga723')	"
texto_b_41 = "#"
texto_b_42 = "#step3 - carga873"
texto_b_43 = "mdb.models['Model-1'].HeatTransferStep(initialInc=increment_size, maxNumInc=max_inc, name='Carga873', previous='Carga723', timeIncrementationMethod=FIXED, "
texto_b_44 = "    timePeriod=time_period873, amplitude=RAMP)"
texto_b_45 = "mdb.models['Model-1'].boundaryConditions['Temp-' + str(1)].setValuesInStep(magnitude=temperaturas[3], stepName='Carga873')"
texto_b_46 = "mdb.models['Model-1'].boundaryConditions['Temp-' + str(2)].setValuesInStep(magnitude=temperaturas[3], stepName='Carga873')"
texto_b_47 = "#"
texto_b_48 = "# CRIA O JOB"
texto_b_49 = "#"
texto_b_50 = "mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(frequency = LAST_INCREMENT, variables=('NT', 'TEMP'))"
texto_b_51 = ""
texto_b_52 = "#"
texto_b_53 = "myJob = mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, memory=90, "
texto_b_54 = "                	memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, multiprocessingMode=DEFAULT, name='termico', nodalOutputPrecision=SINGLE, numCpus=1, "
texto_b_55 = "                	queue=None, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)"
texto_b_56 = "#"
texto_b_57 = "#SUBMETE O JOB PARA ANÁLISE"
texto_b_58 = "#"
texto_b_59 = "myJob.submit()"
texto_b_60 = "myJob.waitForCompletion()"
texto_b_61 = "odbName = 'termico.odb'"
texto_b_62 = "odb = openOdb(path=odbName)"
texto_b_63 = "odb.close()"


for j in range(1, 63):
    textFile.write(globals()['texto_b_'+str(j)])
    textFile.write('\n')
