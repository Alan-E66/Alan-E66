#!/usr/bin/env python
# coding: utf-8

# In[76]:


# importing package
import numpy as np
import pandas as pd
data = pd.read_csv('polar.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]*0.001
y1 = data[1]
y2 = data[2]
y3 = data[3]

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y1,'o-',color='blue')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Protein PB energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Polar_protein_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y2,'x-',color='red')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Ligand PB energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Polar_ligand_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y3,'*-',color='green')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Total PB energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Polar_total_ener.png')
plt.show()


# In[77]:


# importing package
import numpy as np
import pandas as pd
data = pd.read_csv('apolar.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]*0.001
y1 = data[1]
y2 = data[2]
y3 = data[3]

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y1,'o-',color='blue')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Protein Surf-Ten energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Apolar_protein_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y2,'x-',color='red')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Ligand Surf-Ten energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Apolar_ligand_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y3,'*-',color='green')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Total Surf-Ten energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Apolar_total_ener.png')
plt.show()


# In[78]:


# importing package
import numpy as np
import pandas as pd
data = pd.read_csv('energy-mm.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]*0.001
y1 = data[5]
y2 = data[6]
y3 = data[7]

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y1,'o-',color='blue')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Vdw energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('Vdw_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y2,'x-',color='red')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Elec energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('PElec_ener.png')
plt.show()

plt.rcParams['figure.figsize'] = [12, 8]
plt.grid()
plt.plot(x, y3,'*-',color='green')
plt.xlabel('time(ns)',fontsize=20)
plt.ylabel('Total energy (KJ/mol)',fontsize=20)
plt.xlim([0,150])
plt.savefig('total_ener.png')
plt.show()


# In[ ]:



