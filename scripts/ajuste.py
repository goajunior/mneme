from scipy.optimize import differential_evolution, fmin_powell, fmin, fmin_slsqp
import numpy as np
import os

def f(x):
	print 'Parametros: %f %f %f' % (x[0], x[1], x[2])
	cmdstr = 'abq2018 cae noGUI=mecanico.py -- %f %f %f' % (x[0], x[1], x[2])
	os.system(cmdstr)
	erro = 1.0
	curva_media = []
	if os.path.isfile("rms_erro.txt"):
		erro = np.loadtxt('rms_erro.txt')
		curva_media = np.loadtxt('curva_media.txt')
	else:
		erro = 1.0
	print 'Erro: ', erro
	
	arq = open("erro_historico.txt", "a+")
	arq.write('Parametros: %f %f %f \n' % (x[0], x[1], x[2]))
	arq.write('Erro: %f\n\n' % (erro))
	arq.close()
	
	print 'E: \n', curva_media

	return erro


print 'Ajuste rodando...\n'

#limites de cada parametro
#bounds mazars = [(0.7, 1.0), (1e4, 1e5), (1.0, 1.5), (1e3, 2e3), (0.5e-4, 1.5e-4), (1.0, 1.1)]
# bounds aldemon  = [(0.2, 1.0), (1e2, 1e5), (1e-5, 1e-3), (1.0, 1.1)]
#bounds = [(0.7, 1.0), (1e4, 1e5), (0.5e-4, 1.5e-4)]

#Ordem dos parametros
#'alpha_t', 'bheta_t', 'e_d0', 'bheta'
#fmin=1.701565 762.362778 0.000541 1.0

#result_media = fmin(f, [0.95, 1000.0, 0.001, 1.0])
result = fmin(f, [0.95, 1000.0, 0.001, 1.0])
#result_media = differential_evolution(f, bounds)

#print result_media.x, result_media.fun
#np.savetxt('parametros_ajustados_media', result_media.x)
#np.savetxt('resultado_erro_ajuste_media', [result_media.fun])

np.savetxt('parametros_ajustados.txt', result)
np.savetxt('resultado_erro_ajuste_media', [result_media[1]])


