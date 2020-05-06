import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np



rho_283 = [0.000000, 0.4005204, 1.119462, 1.698629, 2.010136, 2.072919, \
           1.898872, 1.580587, 1.322490, 1.206897, 1.171350, 1.193990, \
           1.252900, 1.308722, 1.372691, 1.458393, 1.544730, 1.632884, \
           1.737451, 1.839542, 1.926015, 2.027550, 2.141893, 2.232498, \
           2.288891, 2.340017, 2.381759, 2.383409, 2.343025, 2.309382, \
           2.315281, 2.363291, 2.456813, 2.608183, 2.803355, 3.023636, \
           3.287621, 3.596284, 3.917294, 4.268025, 4.680325, 5.108988, \
           5.509916, 5.935525, 6.396799, 6.827404, 7.218567, 7.614806, \
           7.963608, 8.212350, 8.407257, 8.565375, 8.611701, 8.551322, \
           8.491609, 8.456424, 8.382308, 8.252262, 8.082789, 7.892225, \
           7.709093, 7.552676, 7.385949, 7.188253, 6.997005, 6.834275, \
           6.658732, 6.452670, 6.251437, 6.078947, 5.906580, 5.721030, \
           5.545298, 5.382871, 5.199881, 4.998420, 4.809347, 4.637318, \
           4.460711, 4.285237, 4.119970, 3.957456, 3.802720, 3.667038, \
           3.537688, 3.392823, 3.237844, 3.083621, 2.938483, 2.794379, \
           2.618337, 2.398675, 2.174743, 1.973006, 1.767542, 1.559136, \
           1.388105, 1.245415, 1.106893, 9.899717E-1, 9.134314E-1, \
           8.420908E-1, 7.698313E-1, 7.170319E-1, 6.787253E-1, 6.379317E-1, \
           6.056904E-1, 5.856277E-1, 5.618792E-1, 5.377198E-1, 5.222762E-1, \
           5.089940E-1, 4.943599E-1, 4.838341E-1, 4.732544E-1, 4.588599E-1, \
           4.485080E-1, 4.417946E-1, 4.331451E-1]
x_283 = [0.001265*i for i in range(len(rho_283))]
f = interp1d(x_283,rho_283)

x_283_coarse = np.linspace(0,x_283[-1],20)
rho_283_coarse = f(x_283_coarse)

#print(x_283_coarse[1]-x_283_coarse[0])
#print(rho_283_coarse)
#plt.plot(x_283_coarse,rho_283_coarse)
#plt.plot(x_283,rho_283)
#plt.show()





rho_350 = [
0.000000, 4.535200E-1, 1.157926, 1.668384, 1.911935, \
1.971881, 1.902048, 1.777212, 1.708871, 1.713483, \
1.728215, 1.758169, 1.817488, 1.882584, 1.952605, \
2.041241, 2.132688, 2.222225, 2.328803, 2.435869, \
2.534064, 2.646000, 2.765369, 2.857240, 2.942161, \
3.043550, 3.123609, 3.173809, 3.252655, 3.376228, \
3.510955, 3.659283, 3.838349, 4.036203, 4.256817, \
4.518922, 4.786487, 5.047358, 5.338229, 5.650585, \
5.921455, 6.175496, 6.463906, 6.740295, 6.946280, \
7.122550, 7.292629, 7.418746, 7.506886, 7.582684, \
7.608479, 7.574469, 7.560006, 7.563075, 7.507526, \
7.399013, 7.311152, 7.212945, 7.068417, 6.930299, \
6.827798, 6.684518, 6.501248, 6.354591, 6.245396, \
6.094145, 5.914076, 5.756520, 5.609180, 5.435743, \
5.258676, 5.095134, 4.933199, 4.770790, 4.615469, \
4.460757, 4.308500, 4.168480, 4.018265, 3.842684, \
3.667828, 3.522206, 3.385249, 3.244169, 3.114425, \
2.994159, 2.856150, 2.702938, 2.549948, 2.394326, \
2.230158, 2.068809, 1.911321, 1.752214, 1.602476, \
1.468369, 1.340868, 1.221843, 1.127424, 1.047925, \
9.693006E-1, 9.014253E-1, 8.542987E-1, 8.114617E-1, 7.669130E-1, \
7.315542E-1, 7.028326E-1, 6.701635E-1, 6.434350E-1, 6.276213E-1, \
6.099284E-1, 5.870101E-1, 5.731069E-1, 5.656145E-1, 5.539700E-1, \
5.410732E-1, 5.326189E-1, 5.246716E-1, 5.168530E-1 ]

#x_350 = [0.001265*i for i in range(len(rho_350))]
#f = interp1d(x_350,rho_350)

#x_350_coarse = np.linspace(0,x_350[-1],20)
#rho_350_coarse = f(x_350_coarse)

#print(x_350_coarse[1]-x_350_coarse[0])
#print(rho_350_coarse)
#plt.plot(x_350_coarse,rho_350_coarse)
#plt.plot(x_350,rho_350)
#plt.show()


rho_600 = [ 0.000000, 3.512322E-1, 1.176039, 1.934769, 2.451112, \
2.787652, 3.026583, 3.215558, 3.384392, 3.565888, \
3.735995, 3.902737, 4.128384, 4.357733, 4.603274, \
4.817475, 5.024236, 5.260817, 5.490342, 5.688838, \
5.967795, 6.090132, 6.214738, 6.395790, 6.546064, \
6.671589, 6.746786, 6.895744, 6.931128, 6.981107, \
7.045143, 7.066841, 7.060076, 7.043977, 6.989634, \
6.992917, 6.953450, 6.920568, 6.841614, 6.741639, \
6.626475, 6.509999, 6.463235, 6.339392, 6.213189, \
6.087860, 6.010342, 5.849333, 5.734992, 5.574687, \
5.494402, 5.368692, 5.221456, 5.050761, 4.932593, \
4.811791, 4.691059, 4.546802, 4.403873, 4.281869, \
4.155976, 4.022257, 3.890183, 3.752853, 3.636247, \
3.503662, 3.373830, 3.244275, 3.116750, 2.968686, \
2.846005, 2.719916, 2.599014, 2.450542, 2.325954, \
2.210769, 2.068659, 1.950751, 1.840472, 1.737284, \
1.629107, 1.546032, 1.455436, 1.367346, 1.295500, \
1.236567, 1.165624, 1.115392, 1.068302, 1.025691, \
9.795167E-1, 9.276404E-1, 8.968341E-1, 8.646120E-1, 8.363026E-1, \
8.053232E-1, 7.746023E-1, 7.509068E-1, 7.304269E-1, 7.039427E-1, \
6.865309E-1, 6.714130E-1, 6.551978E-1, 6.352331E-1, 6.237196E-1, \
6.110360E-1, 6.006606E-1, 5.871532E-1, 5.778642E-1, 5.719062E-1, \
5.642204E-1, 5.569704E-1, 5.530494E-1, 5.503502E-1, 5.455926E-1, \
5.443112E-1, 5.414833E-1, 5.423153E-1, 5.458042E-1 ]

x_600 = [0.001265*i for i in range(len(rho_600))]
f = interp1d(x_600,rho_600)

x_600_coarse = np.linspace(0,x_600[-1],19)
rho_600_coarse = f(x_600_coarse)

print(x_600_coarse[1]-x_600_coarse[0])
print(rho_600_coarse)
plt.plot(x_600_coarse,rho_600_coarse)
plt.plot(x_600,rho_600)
plt.show()


