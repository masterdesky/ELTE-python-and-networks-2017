#Erdős-Rényi hálózat
#N csúcs (nodes, vertex)
#E él (edges, links)
# <k> = 2E/N (average degree of nodes)
#p =~ 2E/(N^2) (edge density)
#hálózati alapmennyiségek (mérőszámok)
#klaszterezettségi együttható (egy csúcsé):
# c_i, de figyelni kell mert lehet hogy csúcsokra átlagolt
#klaszterezettségi együttható

#klaszterezettségi együttható egy csúcsra:
#Példa: Legyen Sven és Olaf, Sven fokszáma 5
# c_i = n / (k_i*(k_i-1)/2) = 2n / (k_i*(k_i-1))
# a nevező a szomszédai között max. lehetséges élek száma
# ha véletlenszerűen kiválasztom két szomszédját, akkor
# mekkora a valószínűség hogy köztük él lesz (ez a klasz. e.ható)

#Gráfomponens1: Azon csúcsok maxim. halmaza,
#amelyek esetén bármelyik kettő elérhető a gráf élein keresztül

#Grákkomponens2: Súlyos és irányítatlan hálózat esetén
#------------------------------------------------------------
#Erdős-Rényi hálózat (modell) def.:
#(Classical random graph / Uncorrelated random graph):

#Gilbert definíciója:
#N csúcsok közé E élt dobálunk be random módon.
#N nodes, E edges randomly. 1959

#Erdős-Rényi definíciója:
#N nodes, p edge density. 1960

#Legyen k_i csúcs, akihez az i csúcs hozzá van kötve
#Legyen ekkor N-1-k_i akikhez nincs
#Az elsőknél p lesz a valószínűség, a többinél 1-p. (Ez az edge prob.)
#Prob(p) (k_i = k) = (N-1 C k) p^k * (1-p)^(N-1-k) =~ (N C k)*p^k*(1-p)^(N-k)
#Ha N -> inf
#Ha <k> -> cnst:
# e^(-<k>)*(<k>^k / k!) (vagy hasonló)

#p = cnst / N = <k> / N
# <k> -> cnst = p*N

#Prob(k_i = k) = Prob(k) -> (Ha N -> inf & <k> ->cnst) -->
#                        -> Poisson_<k> (k) = (e^(-<k>))*(<k>^k / k!)

#In Prob(k) =~ k*ln(<k>) - k*ln(k) + ... -> k*ln(k)


#Svel és Olaf megint: A klaszterezettségi együttható = p, mert
#Erdős-Rényi hálózat és minden él valószínűsége p. Így ha kettő nodes-ot
#random kiválasztunk, a köztük levő él valószínűse mideen esetben p.
# c = p = <k> / N