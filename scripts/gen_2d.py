# -*- coding: UTF8 -*-

import argparse
import random
import time
import os
import numpy as np
import sys
from sklearn.neighbors import KDTree

try:
    import cPickle as pickle
except:
    import pickle

parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument("--percent", type=float, default=0.25, help="percentual de agregados")
parser.add_argument("--agreg", type=int, default=2, help="agregados a serem usados")
# parser.add_argument('--guess', type=float, default=1.0, help='initial guess')
# parser.add_argument('--output', default='plot.png', help='output image file')
args = parser.parse_args()

percents = [args.percent]
# =============================================================================
#
# constantes com dados de configuração...
#

# tamanho do retângulo.
widthRectangle = 50.0  # 1/4 do retângulo do cilindro 160x320.
heightRectangle = 100.0  # 1/4 do retângulo do cilindro 160x320.

# número de amostras a serem criadas.
maxSamples = 1  # índice máximo para geração de amostras;
minSamples = 1  # índice mínimo para geração de amostras;

# percentual de agregados relativo à area total do retângulo.
# percents = [0.125, 0.25, 0.375, 0.45]
# percents = [0.18]

# agregados a serem usados
aggregateList = [args.agreg]

# variáveis para mudar distribuição dos círculos.
shakingNumber = 5000  # número de vezes para andar com todas as esferas.
percentMTT = 0.3  # quanto andar...
collisionOffset = 0.00001  #

#
tryMOVEMAX = 200

# -
showRectangles = False

# -
randomSeed = 1234

# --
globalSAMPLE = ""
globalPERCENT = 0.0
globalAGGREGATE = 0


# -----------------------------------------------------------------------------

# Desenha círculos em um retângulo.
# noinspection PyPep8Naming,PyShadowingNames
def drawCircles(
    pointCircles,
    radiusCircles,
    widthRectangle,
    heightRectangle,
    figsize=10,
    fname="output.png",
):
    import matplotlib.pyplot as plt

    # plt.switch_backend('nbagg')
    #    print len(pointCircles)
    figh = figsize
    figw = figh * ((widthRectangle + 0.0) / heightRectangle)
    fig = plt.figure(num=None, figsize=(figw, figh), dpi=80)
    plt.axis([0, widthRectangle, 0, heightRectangle])
    for i in range(0, len(pointCircles)):
        fig.gca().add_artist(
            plt.Circle(pointCircles[i], radiusCircles[i], color="0.95")
        )
    plt.savefig(fname)

    if showRectangles:
        plt.show()


#
# deposita os círculos no fundo do retângulo, da direita para esquerda e
# debaixo para cima.
#
# noinspection PyPep8Naming,PyShadowingNames
def depositInRectangle(radiusCircles, widthRectangle, heightRectangle, percentual):

    # -
    minRadius = min(radiusCircles)
    maxRadius = max(radiusCircles)

    # **************************************
    # ****** Model De larrard **************

    # compacity of a sample
    #   > Compacity g is the ratio between the volume of aggregates
    #   > and the total volume of a sample.
    g = percentual

    # virtual compacity
    #   > The virtual compacity is defined as the maximum density
    #   > for a given mixture, and its expression for rounded
    #   > aggregates, as lightweight aggregates, is defined as:
    gv = 1 - 0.47 * (minRadius / maxRadius) ** 0.22

    # MTT - Maximum Mortar Thickness
    #   > The distance MMT is depending on g; gv and maxRadius by
    #   > the mathematical relationship:
    mtt = maxRadius * ((gv / g) ** (1 / 3.0) - 1)
    # **************************************

    offset = mtt * percentMTT
    if offset > collisionOffset:
        offset = collisionOffset

    # --

    baseX = 0.0
    baseY = 0.0
    maxRadius = 0.0
    depositPoints = []
    depositRadius = []
    for radius in radiusCircles:

        x = baseX + radius + offset
        y = baseY + radius + offset

        # guarda o maior raio inserido na linha para
        # usar no deslocamento de linha.
        if radius > maxRadius:
            maxRadius = radius

        # verifica se o círculo ainda cabe na linha (eixo x do retângulo);
        # se extrapolar, recomeça na linha acima.
        if x + radius > widthRectangle:
            baseX = 0
            baseY += maxRadius * 2
            maxRadius = 0
            # -
            x = baseX + radius
            y = baseY + radius

        # verifica se o círculo será inserido dentro do retângulo
        # (eixo y do retângulo).
        if y + radius <= heightRectangle:
            depositPoints.append([x, y])
            depositRadius.append(radius)
            baseX += radius * 2

        # se não couber, então abandona o laço.
        else:
            break
            # sys.exit("Can't deposit all circles in rectangle.")

    # -
    return len(depositPoints), depositPoints, depositRadius


#
# calcula a área de vários círculos.
#
# noinspection PyPep8Naming,PyShadowingNames
def rectPercArea(radius, rectangleWidth, rectangleHeight, div4=False):
    rectarea = rectangleWidth * rectangleHeight
    if div4:
        rectarea = rectarea / 4
    radiusarea = np.sum((np.array(radius) ** 2.0) * np.pi)
    perc = radiusarea / rectarea
    return perc


# grava um objeto em um arquivo no disco.
# noinspection PyPep8Naming,PyShadowingNames
def save_object(obj, filename):
    with open(filename, "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


# restaura um objeto de um arquivo no disco.
# noinspection PyPep8Naming,PyShadowingNames
def load_object(filename):
    with open(filename, "rb") as input:
        obj = pickle.load(input)
        return obj


# formato um número percentual.
# noinspection PyPep8Naming,PyShadowingNames
def formatFilePercent(value):
    return format_float(value * 100)


# noinspection PyPep8Naming,PyShadowingNames
def format_float(value, precision=1):
    formatString = "%0." + str(precision) + "f"
    str_val = formatString % value
    first, second = str_val.split(".")
    first = int(first)
    group = []
    while True:
        result, mod = int(first / 1000), first % 1000
        group.append(str(mod))
        if result == 0:
            break
        first = result
    group.reverse()
    return ".".join(group) + "," + second


# apresenta uma barra de progressão no terminal.
# noinspection PyPep8Naming,PyShadowingNames
def updateProgress(progress, text="", newline=False):
    os.sys.stdout.write(
        "\r(P{0:4.1f}A{2:1d}S{1:2d}) Progress: [{3:35s}] {4:6.2f}% {5}".format(
            globalPERCENT * 100,
            globalSAMPLE,
            globalAGGREGATE,
            "#" * int(progress * 35),
            progress * 100,
            text,
        )
    )
    if newline or progress >= 1.0:
        os.sys.stdout.write("\n")
    os.sys.stdout.flush()


# apresenta um texto no terminal.
# noinspection PyPep8Naming,PyShadowingNames
def display(text=" "):
    os.sys.stdout.write(
        "(P{0:4.1f}A{2:1d}S{1:2d}) {3}\n".format(
            globalPERCENT * 100, globalSAMPLE, globalAGGREGATE, text
        )
    )
    os.sys.stdout.flush()


# grava os dados de granulometria no arquivo.
def savePDInfo(fileName, PD, PDm, areaElements, elements):

    tmp = [[range(1, 12)], PD[range(0, 11)], PDm, areaElements, elements]
    head = ["     ;", "   PD;", "  PDm;", " area;", "elems;"]
    fmt = ["%10d", "% 10.4f", "% 10.4f", "% 10.4f", "%10d"]

    with open(fileName, "wb") as f:
        i = 0
        for data_slice in tmp:
            type(head[i])
            f.write(head[i].encode())
            np.savetxt(f, data_slice, delimiter=";", newline=";", fmt=fmt[i])
            f.write("\n".encode())
            i = i + 1


# fixa o gerador aleatório para conseguir reproduzir a distribuição
# dos círculos no retângulo.
random.seed(randomSeed)

# cria um subdiretório para guardar os dados.
dirData = os.path.join(os.getcwd(), "data2d")
if not os.path.exists(dirData):
    os.makedirs(dirData)

# =============================================================================
#
# distribuição granulométrica para cada agregado.
#

# tamanho da peneira
# theta = np.array([25.00, 20.00, 16.00, 12.50, 10.00, 8.00, 6.30, 5.00, 4.00, 2.50, 1.25, 0.000000001])
theta = np.array(
    [64, 50, 38, 32, 25, 19, 12.5, 9.5, 6.3, 4.8, 2.4, 1.2, 0.6, 0.3, 0.15]
)
# percentual para cada agregado; agregados: 0/4 650 A, 4/10 550 A, 4/10 430 A,
#                                           4/10 520 S, 4/8 750 S;
# PDall = np.zeros(shape=(5, 12))
# PDall[0] = np.array([1.00,   1.00,  1.00,  1.0000, 1.0000, 0.9990, 0.9983, 0.9883, 0.8184, 0.1875, 0.0574, 0])
# PDall[1] = np.array([1.00,   1.00,  1.00,  1.0000, 0.9532, 0.3287, 0.1456, 0.0516, 0.0215, 0.0021, 0.0006, 0])
# PDall[2] = np.array([1.00,   1.00,  1.00,  1.0000, 0.9830, 0.6854, 0.2261, 0.2261, 0.0165, 0.0000, 0.0000, 0])
# PDall[3] = np.array([1.00,   1.00,  1.00,  0.9993, 0.9828, 0.7054, 0.3211, 0.3211, 0.0198, 0.0005, 0.0005, 0])
# PDall[4] = np.array([1.00,   1.00,  1.00,  1.0000, 0.9986, 0.9605, 0.6880, 0.2963, 0.1060, 0.0265, 0.0133, 0])

PDall = np.zeros(shape=(4, 15))
PDall[0] = np.array(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0.9712, 0.9138, 0.8264, 0.4838, 0.1435, 0.0207]
)  # B
PDall[1] = np.array(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.7804, 0.6906, 0.5508, 0.4551, 0.2678]
)  # G
PDall[2] = np.array(
    [1, 1, 1, 1, 1, 1, 1, 0.9004, 0.3107, 0.0456, 0.023, 0.023, 0.023, 0.023, 0.023]
)  # X
PDall[3] = np.array(
    [
        1,
        1,
        1,
        1,
        1,
        0.9826,
        0.6585,
        0.3628,
        0.09902,
        0.01452,
        0.00153,
        0.00153,
        0.00153,
        0.00153,
        0.00153,
    ]
)  # N

for i in range(0, len(PDall)):
    idx = 8
    while True:
        sumIdx = np.sum(PDall[i, range(idx, 15)])
        if sumIdx > 1.0:
            idx += 1
        else:
            PDall[i, idx] = sumIdx
            PDall[i, range(idx + 1, 12)] = 0
            break
##    PD[i,8] += 0.025
# ----------------------------------------------------

# =============================================================================
#
# Gera os círculos de acordo com a curva granulométrica e faz o packing no
#    retângulo.
#
# --

for perAgreggate in percents:
    globalPERCENT = perAgreggate

    perDescription = formatFilePercent(perAgreggate)

    for countAggregate in aggregateList:
        globalAGGREGATE = countAggregate

        aggrDescription = "A%d" % countAggregate

        for countSample in range(minSamples, maxSamples + 1):
            random.seed(randomSeed + int(countSample + perAgreggate * 100))
            globalSAMPLE = countSample

            fileName = "stones2D%sC%d-%s.dgibi" % (
                aggrDescription,
                countSample,
                perDescription,
            )

            # se o arquivo já existe, não precisa repetir o processo.
            if os.path.isfile(os.path.join(dirData, ("%s-rawdep.bin" % fileName))):
                continue

            # -
            while True:

                # Diametros medios
                thetam = np.array([])
                PDm = np.array([])
                PD = PDall[countAggregate - 1]
                for i in range(0, len(theta) - 1):
                    thetam = np.append(thetam, (theta[i] + theta[i + 1]) / 2)
                    PDm = np.append(PDm, PD[i] - PD[i + 1])

                areaTotal = heightRectangle * widthRectangle
                areaAggregate = perAgreggate * areaTotal
                vthetam = np.pi * (thetam / 2) ** 2  # area of circle
                areaElements = (
                    areaAggregate * PDm * np.random.choice([1.0, 1.005, 1.01])
                )
                elements = np.array(areaElements / vthetam).round().astype(np.int64)

                radiusCircles = np.array([]).astype(np.float64)
                areaElementsReal = np.zeros(len(PDm))
                areaRestElements = 0
                for i in range(0, len(areaElements)):
                    if areaElements[i] > 0:
                        arearadiusCircleElements = 0
                        areaRestElements += areaElements[i]
                        areaTempMin = np.pi * (theta[i + 1] / 2) ** 2
                        countTry = 0
                        while (areaRestElements - 0.001) > areaTempMin:
                            radTemp = (
                                theta[i + 1]
                                + (theta[i] - theta[i + 1]) * random.random()
                            ) / 2
                            areaTemp = np.pi * radTemp**2
                            if (areaRestElements - areaTemp) > 0:
                                areaRestElements -= areaTemp
                                areaElementsReal[i] += areaTemp
                                radiusCircles = np.append(radiusCircles, radTemp)
                                countTry = 0
                            else:
                                countTry += 1
                                if countTry > 50:
                                    break

                display(
                    "radiusCircles %%: %.3f"
                    % (rectPercArea(radiusCircles, widthRectangle, heightRectangle))
                )

                PDmReal = np.append(areaElementsReal / areaAggregate, 0.0)
                PDReal = np.zeros(len(PDmReal))
                for i in range(len(PDmReal) - 2, -1, -1):
                    PDReal[i] = PDmReal[i] + PDReal[i + 1]

                # inclui as bolinhas aleatoriamente para distribuir os vários diametros em
                # todo cilindro.
                radiusCircles = np.random.permutation(radiusCircles)

                radiusCirclesOrig = np.zeros(len(radiusCircles), dtype=np.float64)
                np.copyto(radiusCirclesOrig, radiusCircles)

                display("depositing in rectangle...")
                display("    cirlces = %d" % len(radiusCircles))
                start_time = time.time()
                nb_remaining_particles = 0
                anotherDepositCount = 0
                # -
                (
                    nb_remaining_particles,
                    pointCircles,
                    radiusCircles,
                ) = depositInRectangle(
                    radiusCirclesOrig, widthRectangle, heightRectangle, perAgreggate
                )
                # tem q manter 99.5% das esferas para aceitar a distribuição.
                if ((nb_remaining_particles + 0.0) / len(radiusCirclesOrig)) < 0.995:
                    # -
                    anotherDepositCount += 1
                    if anotherDepositCount > 10:
                        break
                    # -
                    radiusCirclesOrig = np.random.permutation(radiusCirclesOrig)
                    radiusCircles = np.zeros(len(radiusCirclesOrig), dtype=np.float64)
                    np.copyto(radiusCircles, radiusCirclesOrig)
                    display(
                        "   finding another depositing (%d from %d)..."
                        % (nb_remaining_particles, len(radiusCirclesOrig))
                    )
                else:
                    break

            elapsed_time = time.time() - start_time
            display(
                "   Elements       = %d from %d"
                % (nb_remaining_particles, len(radiusCirclesOrig))
            )
            display("   Execution time = %.3f" % elapsed_time)
            display(
                "   particles %%   = %.3f"
                % (rectPercArea(radiusCircles, widthRectangle, heightRectangle))
            )

            # -
            radiusCircles = np.resize(radiusCircles, nb_remaining_particles)
            pointCircles = np.resize(pointCircles, (nb_remaining_particles, 2))
            circles = np.append(
                pointCircles, np.reshape(radiusCircles, (len(radiusCircles), 1)), axis=1
            )
            save_object(circles, os.path.join(dirData, ("%s-rawdep.bin" % fileName)))
            display("file %s-rawdep.bin saved" % fileName)
            display()

            savePDInfo(
                os.path.join(dirData, ("%s-gran.txt" % fileName)),
                PD,
                PDm,
                areaElements,
                elements,
            )


# =============================================================================
#
# Verifica e remove os círculos que estão fora do retângulo ou colidindo com
#    outro círculo.
#
# --

for perAgreggate in percents:
    globalPERCENT = perAgreggate

    perDescription = formatFilePercent(perAgreggate)

    for countAggregate in aggregateList:
        globalAGGREGATE = countAggregate

        aggrDescription = "A%d" % countAggregate

        for countSample in range(minSamples, maxSamples + 1):
            random.seed(randomSeed + int(countSample + perAgreggate * 100))
            globalSAMPLE = countSample

            fileName = "stones2D%sC%d-%s.dgibi" % (
                aggrDescription,
                countSample,
                perDescription,
            )

            # se o arquivo já existe, não precisa repetir o processo.
            if os.path.isfile(os.path.join(dirData, ("%s-dep.bin" % fileName))):
                continue

            # -
            circles = load_object(os.path.join(dirData, ("%s-rawdep.bin" % fileName)))
            pointCircles = circles[:, (0, 1)]
            radiusCircles = circles[:, 2]

            nb_remaining_particles = len(radiusCircles)

            # -
            minRadius = min(radiusCircles)
            maxRadius = max(radiusCircles)

            # **************************************
            # ****** Model De larrard **************

            # compacity of a sample
            #   > Compacity g is the ratio between the volume of aggregates
            #   > and the total volume of a sample.
            g = perAgreggate

            # virtual compacity
            #   > The virtual compacity is defined as the maximum density
            #   > for a given mixture, and its expression for rounded
            #   > aggregates, as lightweight aggregates, is defined as:
            gv = 1 - 0.47 * (minRadius / maxRadius) ** 0.22

            # MTT - Maximum Mortar Thickness
            #   > The distance MMT is depending on g; gv and maxRadius by
            #   > the mathematical relationship:
            mtt = maxRadius * ((gv / g) ** (1 / 3.0) - 1)
            # **************************************

            walkingMTT = mtt * percentMTT

            # verifica se tem alguma esfera fora do cilindro ou colidindo com outra.
            removeIdx = []
            progressTotal = nb_remaining_particles + 0.0
            for i in range(0, nb_remaining_particles):
                updateProgress(
                    i / progressTotal,
                    " checking circle %2d/%2d (%d) ... "
                    % (i, nb_remaining_particles, len(removeIdx)),
                )
                if i in removeIdx:
                    continue
                # -
                if (pointCircles[i, 1] - radiusCircles[i] < 0) or (
                    pointCircles[i, 1] + radiusCircles[i] > heightRectangle
                ):
                    removeIdx.append(i)
                elif (pointCircles[i, 0] - radiusCircles[i] < 0) or (
                    pointCircles[i, 0] + radiusCircles[i] > widthRectangle
                ):
                    removeIdx.append(i)
                else:
                    # procura os vizinhos que estão colidindo.
                    maxNeighbor = radiusCircles[i] + collisionOffset + maxRadius
                    # neighbors = KDTree(pointCircles, leaf_size=20).query_radius(pointCircles[i], r=maxNeighbor)[0]
                    neighbors = KDTree(pointCircles, leaf_size=20).query_radius(
                        np.reshape(pointCircles[i], [1, -1]), r=maxNeighbor
                    )[0]
                    for nb in neighbors:
                        if nb in removeIdx:
                            continue
                        if (i != nb) and (
                            np.sqrt(np.sum((pointCircles[i] - pointCircles[nb]) ** 2))
                            < (radiusCircles[i] + radiusCircles[nb] + collisionOffset)
                        ):
                            # tem colisão, vai tentar resolver.
                            countTry = 0
                            collisionDiff = (
                                radiusCircles[i]
                                + radiusCircles[nb]
                                - np.sqrt(
                                    np.sum((pointCircles[i] - pointCircles[nb]) ** 2)
                                )
                            )
                            walkingCollision = (
                                walkingMTT
                                if walkingMTT > collisionDiff
                                else collisionDiff * 2
                            )
                            while True:
                                if countTry < 4:
                                    newPoint = pointCircles[i] + np.choose(
                                        countTry,
                                        [
                                            collisionDiff,
                                            -collisionDiff,
                                            (-collisionDiff, collisionDiff),
                                            (collisionDiff, -collisionDiff),
                                        ],
                                    )
                                else:
                                    newPoint = pointCircles[i] + (
                                        walkingCollision * (np.random.rand(2) * 2 - 1)
                                    )
                                if (
                                    (newPoint[1] - radiusCircles[i] > 0)
                                    and (
                                        newPoint[1] + radiusCircles[i]
                                        <= heightRectangle
                                    )
                                    and (newPoint[0] - radiusCircles[i] > 0)
                                    and (
                                        newPoint[0] + radiusCircles[i] <= widthRectangle
                                    )
                                ):
                                    neighborsNew = KDTree(
                                        pointCircles, leaf_size=20
                                    ).query_radius(
                                        np.reshape(newPoint, [1, -1]), r=maxNeighbor
                                    )[
                                        0
                                    ]
                                    acceptPoint = True
                                    for nb2 in neighborsNew:
                                        if nb2 in removeIdx:
                                            continue
                                        if (i != nb2) and (
                                            np.sqrt(
                                                np.sum(
                                                    (newPoint - pointCircles[nb2]) ** 2
                                                )
                                            )
                                            < (
                                                radiusCircles[i]
                                                + radiusCircles[nb2]
                                                + collisionOffset
                                            )
                                        ):
                                            acceptPoint = False
                                            break
                                    if acceptPoint:
                                        pointCircles[i] = newPoint
                                        break
                                    else:
                                        countTry += 1
                                else:
                                    countTry += 1
                                if countTry > tryMOVEMAX:
                                    if radiusCircles[i] < radiusCircles[nb]:
                                        removeIdx.append(i)
                                    else:
                                        removeIdx.append(nb)
                                    break
                            if countTry > tryMOVEMAX:
                                break

            updateProgress(
                1,
                " checking circle %2d/%2d (%d) ... "
                % (nb_remaining_particles, nb_remaining_particles, len(removeIdx)),
            )

            if len(removeIdx) > 0:
                display(
                    "  removing %s ... " % np.array_str(np.sort(np.array(removeIdx)))
                )
                radiusCircles = np.delete(radiusCircles, removeIdx)
                pointCircles = np.delete(pointCircles, removeIdx, axis=0)
                nb_remaining_particles -= len(removeIdx)
                display(
                    "  particles %%   = %.3f"
                    % (rectPercArea(radiusCircles, widthRectangle, heightRectangle))
                )
            # ------------------------

            # -
            radiusCircles = np.resize(radiusCircles, nb_remaining_particles)
            pointCircles = np.resize(pointCircles, (nb_remaining_particles, 2))
            circles = np.append(
                pointCircles, np.reshape(radiusCircles, (len(radiusCircles), 1)), axis=1
            )
            save_object(circles, os.path.join(dirData, ("%s-dep.bin" % fileName)))
            display("file %s-dep.bin saved" % fileName)
            display()

# sys.exit('...')

# =============================================================================
#
# Redistribui os círculos no espaço livre em cima do retângulo.
#
# --

for perAgreggate in percents:
    globalPERCENT = perAgreggate

    perDescription = formatFilePercent(perAgreggate)

    for countAggregate in aggregateList:
        globalAGGREGATE = countAggregate

        aggrDescription = "A%d" % countAggregate

        for countSample in range(minSamples, maxSamples + 1):
            random.seed(randomSeed + int(countSample + perAgreggate * 100))
            globalSAMPLE = countSample

            fileName = "stones2D%sC%d-%s.dgibi" % (
                aggrDescription,
                countSample,
                perDescription,
            )

            # se o arquivo já existe, não precisa repetir o processo.
            if os.path.isfile(os.path.join(dirData, ("%s-shk.bin" % fileName))):
                continue

            # -
            circles = load_object(os.path.join(dirData, ("%s-dep.bin" % fileName)))
            pointCircles = circles[:, (0, 1)]
            radiusCircles = circles[:, 2]

            # -
            minRadius = min(radiusCircles)
            maxRadius = max(radiusCircles)

            # **************************************
            # ****** Model De larrard **************

            # compacity of a sample
            #   > Compacity g is the ratio between the volume of aggregates
            #   > and the total volume of a sample.
            g = perAgreggate

            # virtual compacity
            #   > The virtual compacity is defined as the maximum density
            #   > for a given mixture, and its expression for rounded
            #   > aggregates, as lightweight aggregates, is defined as:
            gv = 1 - 0.47 * (minRadius / maxRadius) ** 0.22

            # MTT - Maximum Mortar Thickness
            #   > The distance MMT is depending on g; gv and maxRadius by
            #   > the mathematical relationship:
            mtt = maxRadius * ((gv / g) ** (1 / 3.0) - 1)
            # **************************************

            # reposiciona os círculos de acordo com o espaço vazio em cima.
            maxY = max(pointCircles[:, 1])
            minY = min(pointCircles[:, 1])
            upperY = pointCircles[:, 1] + radiusCircles
            indexY = np.where(upperY == max(upperY))[0][0]
            newY = heightRectangle - radiusCircles[indexY] + 0.0
            offsetY = newY / pointCircles[indexY, 1] - 1
            # -
            pointCircles[:, 1] = pointCircles[:, 1] * (1 + offsetY)
            # pointCircles[:,1] = pointCircles[:,1] * (1 + offsetY * ((pointCircles[:, 1] - minY)/maxY))

            lowerCircles = np.where(pointCircles[:, 1] < maxRadius)[0]
            upperCircles = np.where(pointCircles[:, 1] > (heightRectangle - maxRadius))[
                0
            ]
            permuteNumber = abs(int(0.7 * (len(lowerCircles) - len(upperCircles))))

            if len(lowerCircles) > 0:
                swappedCount = 0
                count = 0.0
                for i in np.random.choice(lowerCircles, permuteNumber):
                    count += 1
                    updateProgress(
                        count / permuteNumber, " swapped = %d" % swappedCount
                    )
                    newPoint = pointCircles[i] + 0.0
                    newPoint[1] = heightRectangle - pointCircles[i][1]
                    if newPoint[1] + radiusCircles[i] <= heightRectangle:
                        maxNeighbor = radiusCircles[i] + collisionOffset + maxRadius
                        neighbors = KDTree(pointCircles, leaf_size=20).query_radius(
                            np.reshape(newPoint, [1, -1]), r=maxNeighbor
                        )[0]
                        acceptPoint = True
                        for nb in neighbors:
                            if (i != nb) and (
                                np.sqrt(np.sum((newPoint - pointCircles[nb]) ** 2))
                                < (
                                    radiusCircles[i]
                                    + radiusCircles[nb]
                                    + collisionOffset
                                )
                            ):
                                acceptPoint = False
                                break
                        if acceptPoint:
                            swappedCount += 1
                            pointCircles[i] = newPoint

                updateProgress(
                    1, " swapped = %d from %d" % (swappedCount, permuteNumber)
                )

            # faz os círculos "andarem" para os lados
            walkingMTT = mtt * percentMTT
            progressTotal = len(radiusCircles) + 0.0
            for shk in range(1, shakingNumber + 1):
                keepCount = 0
                for i in range(0, len(radiusCircles)):
                    updateProgress(
                        i / progressTotal,
                        " step %2d/%2d - keeping %d " % (shk, shakingNumber, keepCount),
                    )
                    newPoint = pointCircles[i] + (
                        walkingMTT * (np.random.rand(2) * 2 - 1)
                    )
                    if (
                        (newPoint[1] - radiusCircles[i] >= 0)
                        and (newPoint[1] + radiusCircles[i] <= heightRectangle)
                        and (newPoint[0] - radiusCircles[i] >= 0)
                        and (newPoint[0] + radiusCircles[i] <= widthRectangle)
                    ):
                        maxNeighbor = radiusCircles[i] + collisionOffset + maxRadius
                        neighbors = KDTree(pointCircles, leaf_size=20).query_radius(
                            np.reshape(newPoint, [1, -1]), r=maxNeighbor
                        )[0]
                        acceptPoint = True
                        for nb in neighbors:
                            if (i != nb) and (
                                np.sqrt(np.sum((newPoint - pointCircles[nb]) ** 2))
                                < (
                                    radiusCircles[i]
                                    + radiusCircles[nb]
                                    + collisionOffset
                                )
                            ):
                                keepCount += 1
                                acceptPoint = False
                                break
                        if acceptPoint:
                            pointCircles[i] = newPoint
                    else:
                        keepCount += 1
                updateProgress(
                    1,
                    " step %2d/%2d - keeping %d/%d"
                    % (shk, shakingNumber, keepCount, int(progressTotal)),
                )

            # verifica se ainda existe algum círculo colidindo com outro.
            collision = []
            progressTotal = len(pointCircles) + 0.0
            for i in range(0, len(pointCircles)):
                updateProgress(i / progressTotal, " collision = %d" % len(collision))
                # procura os vizinhos.
                maxNeighbor = radiusCircles[i] + collisionOffset + maxRadius
                neighbors = KDTree(pointCircles, leaf_size=20).query_radius(
                    np.reshape(pointCircles[i], [1, -1]), r=maxNeighbor
                )[0]
                for nb in neighbors:
                    if (i != nb) and (
                        np.sqrt(np.sum((pointCircles[i] - pointCircles[nb]) ** 2))
                        < (radiusCircles[i] + radiusCircles[nb] + collisionOffset)
                    ):
                        # tem colisão, vai tentar resolver.
                        countTry = 0
                        collisionDiff = (
                            radiusCircles[i]
                            + radiusCircles[nb]
                            - np.sqrt(np.sum((pointCircles[i] - pointCircles[nb]) ** 2))
                        )
                        walkingCollision = (
                            walkingMTT
                            if walkingMTT > collisionDiff
                            else collisionDiff * 2
                        )
                        while True:
                            if countTry < 4:
                                newPoint = pointCircles[i] + np.choose(
                                    countTry,
                                    [
                                        collisionDiff,
                                        -collisionDiff,
                                        (-collisionDiff, collisionDiff),
                                        (collisionDiff, -collisionDiff),
                                    ],
                                )
                            else:
                                newPoint = pointCircles[i] + (
                                    walkingCollision * (np.random.rand(2) * 2 - 1)
                                )
                            if (
                                (newPoint[1] - radiusCircles[i] >= 0)
                                and (newPoint[1] + radiusCircles[i] <= heightRectangle)
                                and (newPoint[0] - radiusCircles[i] >= 0)
                                and (newPoint[0] + radiusCircles[i] <= widthRectangle)
                            ):
                                neighborsNew = KDTree(
                                    pointCircles, leaf_size=20
                                ).query_radius(newPoint, r=maxNeighbor)[0]
                                acceptPoint = True
                                for nb2 in neighborsNew:
                                    if (i != nb2) and (
                                        np.sqrt(
                                            np.sum((newPoint - pointCircles[nb2]) ** 2)
                                        )
                                        < (
                                            radiusCircles[i]
                                            + radiusCircles[nb2]
                                            + collisionOffset
                                        )
                                    ):
                                        acceptPoint = False
                                        break
                                if acceptPoint:
                                    pointCircles[i] = newPoint
                                    break
                                else:
                                    countTry += 1
                            else:
                                countTry += 1
                            if countTry > tryMOVEMAX:
                                collision.append(i)
                                collision.append(nb)
                                break
                        if countTry > tryMOVEMAX:
                            break

            updateProgress(1, "  collision = %d" % len(collision))
            if len(collision) > 0:
                collision = np.array(collision)
                _, idx = np.unique(collision, return_index=True)
                collision = collision[np.sort(idx)]
                display("  collision index = %s " % np.array_str(np.sort(collision)))
                # remove os menores círculos.
                removeIdx = []
                for i in range(0, len(collision) / 2):
                    idx = i * 2
                    if (
                        radiusCircles[collision[idx]]
                        < radiusCircles[collision[idx + 1]]
                    ):
                        removeIdx.append(collision[idx])
                    else:
                        removeIdx.append(collision[idx + 1])
                display(
                    "  removing %s ... " % np.array_str(np.sort(np.array(removeIdx)))
                )
                radiusCircles = np.delete(radiusCircles, removeIdx)
                pointCircles = np.delete(pointCircles, removeIdx, axis=0)
                nb_remaining_particles -= len(removeIdx)
                display(
                    "  particles %%   = %.3f"
                    % (rectPercArea(radiusCircles, widthRectangle, heightRectangle))
                )

            shkCircles = np.append(
                pointCircles, np.reshape(radiusCircles, (len(radiusCircles), 1)), axis=1
            )
            save_object(shkCircles, os.path.join(dirData, ("%s-shk.bin" % fileName)))
            display("file %s-shk.bin saved" % fileName)
            display()


# =============================================================================
#
# Grava os arquivos dgibi com todos os círculos 2D.
#   cada linha contém: x y radius
#
# --

for perAgreggate in percents:
    globalPERCENT = perAgreggate

    perDescription = formatFilePercent(perAgreggate)

    dirData2 = os.path.join(os.getcwd(), "%sp" % formatFilePercent(perAgreggate))
    if not os.path.exists(dirData2):
        os.makedirs(dirData2)

    for countAggregate in aggregateList:
        globalAGGREGATE = countAggregate

        aggrDescription = "A%d" % countAggregate

        for countSample in range(minSamples, maxSamples + 1):
            random.seed(randomSeed + int(countSample + perAgreggate * 100))
            globalSAMPLE = countSample

            fileName = "stones2D%sC%d-%s-fit.dgibi" % (
                aggrDescription,
                countSample,
                perDescription,
            )
            fileNameShk = "stones2D%sC%d-%s.dgibi-shk.bin" % (
                aggrDescription,
                countSample,
                perDescription,
            )
            fileNamePng = "stones2D%sC%d-%s-fit.png" % (
                aggrDescription,
                countSample,
                perDescription,
            )

            # se o arquivo já existe, não precisa repetir o processo.
            if os.path.isfile(os.path.join(dirData2, fileName)):
                continue

            # -
            circles = load_object(os.path.join(dirData, fileNameShk))

            # --
            textFile = open(os.path.join(dirData2, fileName), "w")
            # textFile.write('%d\n' % len(circles))
            for i in range(0, len(circles)):
                # x y radius
                textFile.write(
                    "%.6f %.6f %.6f\n"
                    % (float(circles[i, 0]), float(circles[i, 1]), float(circles[i, 2]))
                )
            textFile.close()
            display("file %s created" % fileName)
            display()

            drawCircles(
                circles[:, (0, 1)],
                circles[:, 2],
                widthRectangle,
                heightRectangle,
                figsize=10,
                fname=os.path.join(dirData2, fileNamePng),
            )

display("done")
display()
