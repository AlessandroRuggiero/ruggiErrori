from ruggiErrori.Misure import Misura,radice,arrotonda

torricelli = lambda h: arrotonda(radice (h*9.81*2),3)
v_da_sistema = lambda h,G: arrotonda(G/(tempo_caduta(h)),3)
tempo_caduta = lambda h:arrotonda(radice(h*2/9.81),3)