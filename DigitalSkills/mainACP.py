import acp.ACP as acp
import pandas as pd
import numpy as np
import seaborn as s
import matplotlib.pyplot as plt
import grafice as g


file=pd.read_csv('dataIN/DigitalSkillLevelCleaned.csv',index_col=0)
print("datele initiale")
print(file)

var=list(file.columns)[1:]
print("coloane")
print(var)

obs=list(file.index)
print("observatile")
print(obs)

cols= list(pd.read_csv("dataIN/DigitalSkillLevelCleaned.csv",nrows=1))
df=pd.read_csv("dataIN/DigitalSkillLevelCleaned.csv")

X=file[var].values
print("Matricea X")
print(X);

acp_model=acp.ACP(X)

Xstd=acp_model.getXstd()
Xstd_df=pd.DataFrame(data=Xstd,index=obs,columns=var)
Xstd_df.to_csv("dataOUT/outACP/Xstd.csv")

valProp=acp_model.getValProp()
g.componentePrincipale(valoriProprii=valProp)
#g.afisare()

#salvare in fisier csv a componentelor
compPrin = acp_model.getCompPrin()
compPrin_df = pd.DataFrame(data=compPrin, index=obs, columns=('C'+str(j+1) for j in range(len(var))))
compPrin_df.to_csv('dataOUT/outACP/ComponentePrincipale.csv')

#corelograma factorilor de corelatie
factori=acp_model.getFactoriCorelatie()
factori_df=pd.DataFrame(data=factori,index=var,columns=('C'+str(j+1) for j in range(len(var))))
factori_df.to_csv('dataOUT/outACP/FactoriCorelatie.csv')
g.corelagrama(matrice=factori_df,titlu='Corelograma factorilor de corelatie')
#g.afisare

#corelograma calitatii reprezentarii observatiilor pe axele componentelor
calitate=acp_model.getCalObs()
calitate_df=pd.DataFrame(data=calitate,index=obs,columns=('C'+str(j+1) for j in range(len(var))))
calitate_df.to_csv('dataOUT/outACP/CalitateaObservatiilor.csv')
g.corelagrama(matrice=calitate_df,titlu='Corelograma calitatii reprezentarii observatiilor pe axele componentelor')
#g.afisare()

#corelograma contributiei observatilor
betha=acp_model.getBetha()
betha_df=pd.DataFrame(data=betha, index=obs, columns=('C'+str(j+1) for j in range(len(var))))
betha_df.to_csv('dataOUT/outACP/ContributiiVarianta.csv')
g.corelagrama(matrice=betha_df, titlu='Corelograma contributiei observatiilor la varianta axelor componentelor')
#g.afisare()

#corelograma comunitatilor
com=acp_model.getComun()
com_df=pd.DataFrame(data=com,index=var,columns=('C'+str(j+1) for j in range(len(var))))
com_df.to_csv('dataOUT/outACP/Comunitati.csv')
g.corelagrama(matrice=com_df, titlu='Corelograma comunitatilor (componentele principale regasite in variabilele initale)')
#g.afisare()

#crearea cercului corelatiilor
g.cerculCorelatiilor(matrice=factori_df, titlu='Corelatia dintre variabilele initiale si C1, C2')
#g.afisare()

#corelograma scorurilor
scoruri = acp_model.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obs, columns=('C'+str(j+1) for j in range(len(var))))
scoruri_df.to_csv('dataOUT/outACP/Scoruri.csv')
g.corelagrama(matrice=scoruri_df, titlu='Corelograma scorurilor (componentele principale stadardizate)')
# g.afisare()
#crearea cercului corelatiilor pentru evidentierea legaturii dintre obervatii si C1,C2
maxim_scor = np.max(scoruri)
minim_scor = np.min(scoruri)
print('Maxim scor, folosit ca raza pentru cercul corelatiilor: ', maxim_scor)
g.cerculCorelatiilor(matrice=scoruri_df, raza=maxim_scor, valMin=minim_scor, valMax=maxim_scor,
                     titlu='Distributia observatiilor in spatiul C1, C2')

g.afisare()
