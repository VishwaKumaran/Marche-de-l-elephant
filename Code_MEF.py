######################################################################
# des packages : il y en a qui seront utile pour la suite
######################################################################

import math
from random import*
from math import*
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import scipy.stats as st
######################################################################
# parametre a definir
######################################################################
n = 1000
k = 1000
i = 2
j = 1
q = 1/2
p = 0

######################################################################
# Texts 
######################################################################


D = int(input("pour le cas ou p > 3/4 appuyez sur 1 \n et 0 sinon: "))
print("--\n--")
while not (D == 0 or D ==1):
    D = int(input("pour le cas ou p > 3/4 appuyez sur 1 \net 0 sinon: "))
    print("--\n--")
    


if D == 1:
    Cas2 = True
    k = 2
else:
    Cas2 = False

print("--\n--")
if Cas2 == True:
    Rademacher = 0
    NormalGraphe = 0
    p = float(input("Choisissez un parametre p entre 3/4 et 1: \n(Exemple : 0.75 et non pas 3/4) : "))
    print("--\n--")
    while not 3/4 <= p <=1:
        p = float(input("Choisissez un parametre p entre 3/4 et 1: "))
    print("--\n--")
    Estimateur = int(input("appuyez sur 1 pour voir le comportement dun estimateur \n de vraisemblance qui ne fonctionne pas encore , 0 sinon"))
    print("--\n--")
    while not (Estimateur == 1 or Estimateur == 0):
        Estimateur = int(input("appuyez sur 1 pour voir le comportement de l'estimateur \n de vraisemblance du Rademacher , 0 sinon"))
        print("--\n--")
    

if Cas2 == False:
    Estimateur = 0
    p = float(input("Choisissez un parametre p entre 0 et 3/4: \n (Exemple : 0.5 et non pas 1/2) : "))
    print("--\n--")
    while not 0 < p < 3/4:
        p = float(input("Choisissez un parametre p entre 0 et 3/4: "))
    print("--\n--")

    NormalGraphe = int(input("appuyez sur 1 pour voir la normalite asymptotique \n de SN/n^1/2, 0 sinon"))
    print("--\n--")
    while not (NormalGraphe == 1 or NormalGraphe == 0):
        NormalGraphe = int(input("appuyez sur 1 pour voir la normalite aysmptotique \n de SN/n^1/2, 0 sinon"))
        print("--\n--")
    

    Rademacher = int(input("appuyez sur 1 pour voir le comportement de l'estimateur \nde vraisemblance du Rademacher , 0 sinon"))
    print("--\n--")
    while not (Rademacher == 1 or Rademacher == 0):
        Rademacher = int(input("appuyez sur 1 pour voir le comportement de l'estimateur \nde vraisemblance du Rademacher , 0 sinon"))
        print("--\n--")
    print("Attendez quelques secondes")

if Estimateur == 1 :
    q = 1
        

if NormalGraphe == 1:
    Normal = True
else:
    Normal = False 


V = uniform(0,1)
if V < q:
    X1 = 1
else:
    X1 = -1

SN = [0,X1]
XN_Vec = [X1]
SN_n = []
SN_sqrt_n = []
SN_traj = []
SN_sqrt_n_traj = []
SN_Normal = []
Pn = []
Tn = []
Tn1 = []
XN_Tn = [1]

######################
#autres listes a definir
######################

XN_Somme = []
XN_Bar = [1]
XN_Bar_carre = [1]
XN_Spec = [1]
XN_Spec2 = [1]


######################################################################
# La Marche
######################################################################
while j < k:
    V = uniform(0,1)
    if V < q:
        X1 = 1
    else:
        X1 = -1

    SN = [0,X1]
    XN_Vec = [X1]
    SN_n = []
    SN_sqrt_n = []
    
    i = 2
######################################################################
    while i < n+1:
        V = uniform(0,1)
        U = uniform(0,1)
        if V < p:
            EPSILON = 1
        else:
            EPSILON = -1
        
        m = len(XN_Vec)
        
        X_numero = math.floor(m*U) ## loi uniform discrete sur {1,..,k}
        
        XN = XN_Vec[X_numero]*EPSILON ## On prend la valeur de X ayant l'indice k et on multiplie par EPSILON
        XN_Vec.append(XN)
        SN.append(SN[len(SN)-1]+ XN)
        SN_n.append(SN[len(SN)-1]/i)
        SN_sqrt_n.append(SN[len(SN)-1]/sqrt(i))
        if j == 1:
            if Rademacher == 1:
                Pn.append(1/2*(1+ (sum(XN_Vec,-X1))/(i-1)))
            #Tn.append((XN_Somme-2*(i-1)*(XN_bar)**2+(i-1)*XN_bar-(i-1))/(4*(i-1)*XN_bar-4*(i-1)*(XN_bar)**2-(i-1)))
            if XN == -1:
                XN_Tn.append(0)
            else:
                XN_Tn.append(1)
            XN_Bar.append((sum(XN_Tn))/(i))
            XN_Bar_carre.append((sum(XN_Tn)/(i))**2)
            XN_Spec.append(XN_Tn[i-1]*XN_Bar[i-1])
            XN_Spec2.append(XN_Vec[i-1]*XN_Bar[i-1])  
            Tn.append((3*sum(XN_Bar)-2*sum(XN_Bar_carre)-2*sum(XN_Spec)+sum(XN_Tn)-i)/
                      (4*sum(XN_Bar)-4*sum(XN_Bar_carre)-n))
            Tn1.append((2*sum(XN_Bar)-2*sum(XN_Bar_carre)-sum(XN_Spec2)+(1/2)*sum(XN_Vec)-i/2)/(4*sum(XN_Bar)-4*sum(XN_Bar_carre)-i))
     
        i = i+1
    SN_Normal.append(SN_sqrt_n[len(SN_sqrt_n)-1])
    if j == 1:
        SN_traj = SN
        SN_sqrt_n_traj = SN_sqrt_n
        SN_n_traj = SN_n
    j = j+1

########################################################################
# Graphiques
########################################################################


if Cas2 == False:
    red_line = mlines.Line2D([], [], color='red', label='Trajectoire de la Marche')
    plt.legend(handles=[red_line])
    plt.title('Marche de lelephant')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(SN_traj[0:n],'r') 
    plt.show()


    green_line = mlines.Line2D([], [], color='green', label='Comportememnt asymptotique de SN/n^1/2')
    plt.legend(handles=[green_line])
    plt.title('')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(SN_sqrt_n_traj[0:n],'g') 
    plt.show()

    yellow_line = mlines.Line2D([], [], color='yellow', label='Comportememnt asymptotique de SN/n')
    plt.legend(handles=[yellow_line])
    plt.title('')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(SN_n[0:n],'y') 
    plt.show()   

    #blue_line = mlines.Line2D([], [], color='red', label='Marche de lelephant')
    green_line = mlines.Line2D([], [], color='green', label='Convergence en loi vers une Gaussiene de SN/n^1/2')
    yellow_line = mlines.Line2D([], [], color='yellow', label='Convergence p.s de SN/n vers 0')


    plt.legend(handles=[yellow_line,green_line,red_line])
    plt.title('graphiques relatives aux autres')
    plt.xlabel('Temps')
    plt.ylabel('parcours')

    plt.plot(SN_traj[0:n], 'r',SN_sqrt_n_traj[0:n],'g',SN_n[0:n],'y') 
    plt.show()

if Cas2 == True:
    yellow_line = mlines.Line2D([], [], color='yellow', label='Comportememnt asymptotique de SN/n')
    plt.legend(handles=[yellow_line])
    plt.title('')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(SN_n[0:n],'y') 
    plt.show()   


if Normal == True:
    import scipy.stats as st
    plt.hist(SN_Normal, density=True, bins=35, label="Gaussiene (0,1/(3-4p)",ec='black')
    plt.xlim([min(SN_Normal)-0.5, max(SN_Normal)+0.5])
    kde_xs = np.linspace(min(SN_Normal)-0.5, max(SN_Normal)+0.5, 301)
    kde = st.gaussian_kde(SN_Normal)
    plt.plot(kde_xs, kde.pdf(kde_xs), label="Normalite asymptotique de SN/n^1/2")
    plt.legend(loc="upper left")
    plt.ylabel('densite')
    plt.xlabel('')
    plt.title("");
    plt.show()

if Rademacher == 1:
    green_line = mlines.Line2D([], [], color='green', label='Comportememnt asymptotique de Max de Vrai du rademacher')
    plt.legend(handles=[green_line])
    plt.title('')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(Pn[0:n],'g') 
    plt.show()   

if Estimateur == 1:
    brown_line = mlines.Line2D([], [], color='brown', label='Comportememnt asymptotique dun autre estimateur qui ne fonctionne pas encore')
    plt.legend(handles=[brown_line])
    plt.title('')
    plt.xlabel('Temps')
    plt.ylabel('Parcours')
    plt.plot(Tn1[0:n],'b') 
    plt.show() 
    

    
    
