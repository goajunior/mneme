# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

filename = "C:\\IC\\teste scripts\\40,0p\\stones2DA3C1-40,0-fit.dgibi"
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
texto18 = 'if os.path.isfile("mecanico.odb"):'
texto19 = '    os.remove("mecanico.odb")'
texto20 = 'if os.path.isfile("mecanico.lck"):'
texto21 = '    os.remove("mecanico.lck")'
texto22 = 'if os.path.isfile("curva_media.txt"):'
texto23 = '    os.remove("curva_media.txt")'
texto24 = 'if os.path.isfile("curva_referencia.txt"):'
texto25 = '    os.remove("curva_referencia.txt")'
texto26 = 'if os.path.isfile("rms_erro.txt"):'
texto27 = '    os.remove("rms_erro.txt")'
texto28 = '#'
texto29 = "os.system('C:\\IC\\Teste 2022\\mecanico.odb')"
texto30 = 'temperaturas = [293.15, 473.15, 673.15, 1073.15]'
texto31 = "umat_path = ('C:\\IC\\bi\\subrotina_umat.for')"
texto32 = "odb = ('C:\\IC\\Teste 2022\\termico.odb')"
texto33 = '# command line'
texto34 = '# abq611pr3 cae noGUI=script.py -- 0.95 10000.0 1.0 3000.0 0.00001 1.0'
texto35 = '#'
texto36 = '# DEFINE TIME PERIOD E INCREMENT SIZE'
texto37 = '#'
texto38 = 'time_period = 1'
texto39 = 'increment_size = 0.1'
texto40 = 'max_inc = int(time_period/increment_size)'
texto41 = 'malha_agreg = 0.002*1e3'
texto42 = 'malha_arg = 0.002*1e3'
texto43 = '#'
texto44 = '# DEFINE PROPRIEDADES DOS MATERIAIS'
texto45 = '#'
texto46 = '# obs: propriedades termicas nbr 15220'
texto47 = "#param_mazars = {'alpha_t': float(sys.argv[-3]), 'bheta_t': float(sys.argv[-2]), 'alpha_c': 0.0, 'bheta_c': 0.0, 'e_d0': float(sys.argv[-1]), 'bheta': 1.0}"
texto48 = "param_mazars = {'alpha_t': 1.826, 'bheta_t': 750.603,"
texto49 = "                'alpha_c': 0.0, 'bheta_c': 0.0, 'e_d0': 6.024e-4, 'bheta': 1.0}"
texto50 = '#fmin(f, [0.95, 1000.0, 0.001])'
texto51 = "param_argamass = {'E': 31.00*1e3, 'mu': 0.132, 'T0': 273.15, 'Density': 2252.0 *"
texto52 = "                  1e-9, 'Conductivity': 1.15*60*1e-3, 'SpecificHeat': 1000.0, 'Expansion': 3.67e-6}"
texto53 = "param_agreg = {'E': 39.042*1e3, 'mu': 0.225, 'T0': 273.15, 'Density': 2500.0 *"
texto54 = "               1e-9, 'Conductivity': 0.7*60*1e-3, 'SpecificHeat': 840.0, 'Expansion': 3.779e-6}"
texto55 = "#"
texto56 = "# erro 5,74%"
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
texto78 = "mdb.models['Model-1'].materials['Material-argamassa'].Density("
texto79 = "    table=((param_argamass['Density'], ),))"
texto80 = "mdb.models['Model-1'].materials['Material-argamassa'].Depvar(n=15)"
texto81 = "mdb.models['Model-1'].materials['Material-argamassa'].UserMaterial(mechanicalConstants=(param_argamass['E'], param_argamass['mu'], param_argamass['T0'], param_argamass['Expansion'],"
texto82 = "                                                                   param_mazars['alpha_t'], param_mazars['bheta_t'], param_mazars['alpha_c'], param_mazars['bheta_c'], param_mazars['e_d0'], param_mazars['bheta']), type=MECHANICAL)"
texto83 = "#"
texto84 = "mdb.models['Model-1'].Material(name='Material-agregado')"
texto85 = "mdb.models['Model-1'].materials['Material-agregado'].Density("
texto86 = "    table=((param_agreg['Density'], ), ))"
texto87 = "mdb.models['Model-1'].materials['Material-agregado'].Depvar(n=15)"
texto88 = "mdb.models['Model-1'].materials['Material-agregado'].UserMaterial(mechanicalConstants=(param_agreg['E'], param_agreg['mu'], param_agreg['T0'], param_agreg['Expansion'],"
texto89 = "                                                                  param_mazars['alpha_t'], param_mazars['bheta_t'], param_mazars['alpha_c'], param_mazars['bheta_c'], param_mazars['e_d0'], param_mazars['bheta']), type=MECHANICAL)"
texto90 = "#"
texto91 = "mdb.models['Model-1'].HomogeneousSolidSection(material='Material-argamassa',"
texto92 = "                                              name='Section-argamassa', thickness=None)"
texto93 = "mdb.models['Model-1'].HomogeneousSolidSection(material='Material-agregado',"
texto94 = "                                              name='Section-agregado', thickness=None)"
texto95 = "mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((1.0, 1.0,"
texto96 = "                                                                                                     0.0), (0.0, 0.0, 1.0)), ), name='Set-1')"
texto97 = "mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,"
texto98 = "                                                        offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Section-argamassa', thicknessAssignment=FROM_SECTION)"
texto99 = "mdb.models['Model-1'].ConstrainedSketch(gridSpacing=5.59, name='__profile__',"
texto100 = "                                        sheetSize=223.6, transform=mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform("
texto101 = "                                            sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0],"
texto102 = "                                            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))"
texto103 = "mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=COPLANAR_EDGES,"
texto104 = "                                                                  sketch=mdb.models['Model-1'].sketches['__profile__'])"
texto105 = "#"
texto106 = "mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType("
texto107 = "    elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models['Model-1'].parts['Part-1'].sets['Set-1'])"
texto108 = "#"
texto109 = "# CRIANDO AS BOLINHAS"
texto110 = "#"

v = np.loadtxt(filename)

R = v[:, 2]
G = v[:, (0, 1)]

xx = G[:, 0] + R
yy = G[:, 1] + R

n = len(R)
i=111

for k in range(0, n):
    globals()['texto'+str(i)] = "mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter("
    i=i+1
    globals()['texto'+str(i)] = "    center=("+str(G[k, 0])+","+str(G[k, 1])+"), point1=("+str(xx[k])+","+str(G[k, 1])+"))"
    i=i+1

textFile = open("mecanico.py", "w")
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
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-2\'])"
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
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-3\'])"
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
        globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-4\'])"
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
    globals()['texto_a_'+str(i)] = "mdb.models[\'Model-1\'].parts[\'Part-1\'].setElementType(elemTypes=(ElemType(elemCode=CPS4, elemLibrary=STANDARD), ElemType(elemCode=CPS3, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), regions=mdb.models[\'Model-1\'].parts[\'Part-1\'].sets[\'Set-5\'])"
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
texto_b_21 = "                                  name='Temperatura Inicial', region=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Set-1'])"
texto_b_22 = "#"
texto_b_23 = "# aplica condicoes de simetria"
texto_b_24 = "mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None,"
texto_b_25 = "                              name='SimetriaY', region=mdb.models['Model-1'].rootAssembly.sets['Lateral1'])"
texto_b_26 = "mdb.models['Model-1'].YsymmBC(createStepName='Initial', localCsys=None,"
texto_b_27 = "                              name='SimetriaX', region=mdb.models['Model-1'].rootAssembly.sets['Base'])"
texto_b_28 = "#"
texto_b_29 = "#step1 - carga573"
texto_b_30 = "mdb.models['Model-1'].StaticStep(initialInc=increment_size, maxNumInc=max_inc,"
texto_b_31 = "                                 name='Carga573', previous='Initial', timeIncrementationMethod=FIXED, timePeriod=time_period)"
texto_b_32 = "mdb.models['Model-1'].Temperature(absoluteExteriorTolerance=0.0, beginIncrement=0,"
texto_b_33 = "                                  beginStep=1, createStepName='Carga573', distributionType=FROM_FILE, endIncrement=560, endStep=1, exteriorTolerance=0.05,"
texto_b_34 = "                                  fileName=odb, interpolate=OFF, name='Campo de Temperaturas')"
texto_b_35 = "#"
texto_b_36 = "#step2 - carga723"
texto_b_37 = "mdb.models['Model-1'].StaticStep(initialInc=increment_size, maxNumInc=max_inc,"
texto_b_38 = "                                 name='Carga723', previous='Carga573', timeIncrementationMethod=FIXED, timePeriod=time_period)"
texto_b_39 = "mdb.models['Model-1'].predefinedFields['Campo de Temperaturas'].setValuesInStep("
texto_b_40 = "    beginStep=2, endStep=2, endIncrement=300, stepName='Carga723')"
texto_b_41 = "#"
texto_b_42 = "#step3 - carga873"
texto_b_43 = "mdb.models['Model-1'].StaticStep(initialInc=increment_size, maxNumInc=max_inc,"
texto_b_44 = "                                 name='Carga873', previous='Carga723', timeIncrementationMethod=FIXED, timePeriod=time_period)"
texto_b_45 = "mdb.models['Model-1'].predefinedFields['Campo de Temperaturas'].setValuesInStep("
texto_b_46 = "    beginStep=3, endStep=3, endIncrement=300, stepName='Carga873')"
texto_b_47 = "#"
texto_b_48 = "# CRIA O JOB"
texto_b_49 = "#"
texto_b_50 = "mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues("
texto_b_51 = "    variables=('NT', 'TEMP', 'S', 'E', 'U', 'SDV', 'EVOL'))"
texto_b_52 = "#"
texto_b_53 = "myJob = mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, memory=90,"
texto_b_54 = "                memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, multiprocessingMode=DEFAULT, name='mecanico', nodalOutputPrecision=SINGLE, numCpus=1,"
texto_b_55 = "                queue=None, scratch='', type=ANALYSIS, userSubroutine=umat_path, waitHours=0, waitMinutes=0)"
texto_b_56 = "#"
texto_b_57 = "#"
texto_b_58 = "#"
texto_b_59 = "#"
texto_b_60 = "# SUBMETE O JOB PARA ANÁLISE"
texto_b_61 = "#"
texto_b_62 = "myJob.submit()"
texto_b_63 = "myJob.waitForCompletion()"
texto_b_64 = "odbName = 'mecanico.odb'"
texto_b_65 = "odb = openOdb(path=odbName)"
texto_b_66 = "#"
texto_b_67 = "# Calcula E pela media ponderada"
texto_b_68 = "#"
texto_b_69 = "curva_media = [[temperaturas[0], 34.19*1e3]]"
texto_b_70 = "young = []"
texto_b_71 = "curva_referencia = [[temperaturas[0], 34.19*1e3], [temperaturas[1],"
texto_b_72 = "                                                   21.64*1e3], [temperaturas[2], 12.98*1e3], [temperaturas[3], 5.01*1e3]]"
texto_b_73 = "erro = 0.0"
texto_b_74 = "#"
texto_b_75 = "#"
texto_b_76 = "for step_id in range(len(odb.steps)):"
texto_b_77 = "    young = []"
texto_b_78 = "    E_medio = 0.0"
texto_b_79 = "    areaTotal = 0.0"
texto_b_80 = "#"
texto_b_81 = "    field2 = odb.steps.values()[step_id].frames[-1].fieldOutputs['EVOL']"
texto_b_82 = "    area = np.zeros(len(field2.values))"
texto_b_83 = "#"
texto_b_84 = "    for v in field2.values:"
texto_b_85 = "        area[v.elementLabel - 1] = v.data"
texto_b_86 = "        areaTotal += v.data"
texto_b_87 = "#"
texto_b_88 = "    field = odb.steps.values()[step_id].frames[-1].fieldOutputs['SDV10']"
texto_b_89 = "#"
texto_b_90 = "    for val in field.values:"
texto_b_91 = "        young.append([val.elementLabel, val.data])"
texto_b_92 = "#"
texto_b_93 = "    E = np.zeros(len(area))"
texto_b_94 = "    cont = np.zeros(len(area))"
texto_b_95 = "#"
texto_b_96 = "    for v in young:"
texto_b_97 = "        E[v[0]-1] += v[1]"
texto_b_98 = "        cont[v[0]-1] += 1"
texto_b_99 = "#"
texto_b_100 = "    E = E/cont"
texto_b_101 = "    area = np.array(area)"
texto_b_102 = "#"
texto_b_103 = "    for i in range(len(area)):"
texto_b_104 = "        E_medio += area[i]*E[i]"
texto_b_105 = "#"
texto_b_106 = "    E_medio = E_medio/areaTotal"
texto_b_107 = "#"
texto_b_108 = "    curva_media.append([temperaturas[step_id+1], E_medio])"
texto_b_109 = "#"
texto_b_110 = "print 'E media: ', curva_media"
texto_b_111 = "np.savetxt('curva_media.txt', curva_media)"
texto_b_112 = "#"
texto_b_113 = "print 'E referencia: ', curva_referencia"
texto_b_114 = "np.savetxt('curva_referencia.txt', curva_referencia)"
texto_b_115 = "#"
texto_b_116 = "#"
texto_b_117 = "odb.close()"


for j in range(1, 118):
    textFile.write(globals()['texto_b_'+str(j)])
    textFile.write('\n')