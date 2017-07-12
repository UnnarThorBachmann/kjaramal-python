# -*- coding: utf-8 -*-
import os
import codecs

from kennari import Kennari
from afangi import Afangi
from synidaemi import d
import math
import sys
from launatoflur import toflur

def skrifa(sd,launaflokkur,threp,aldur,kennsluskylda,skertur,vinnumat,ryrnun,fjoldi,einingar,nemfjoldi,vinnuskylda,laun,f):
    uttak = sd
    uttak += "\t".decode(encoding='UTF-8')
    uttak += launaflokkur.decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += threp.decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += aldur.decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(kennsluskylda).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(skertur).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(vinnumat).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(ryrnun).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(fjoldi).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(einingar).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(nemfjoldi).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(vinnuskylda).decode(encoding='UTF-8')
    uttak += "\t".decode(encoding='UTF-8')
    uttak += str(laun).decode(encoding='UTF-8')
    uttak += "\n".decode(encoding='UTF-8')

    f.write(uttak)
    
#reload(sys)  # Reload is a hack
#sys.setdefaultencoding('UTF8')
aldursflokkar = {'30 ára-': [{'launaflokkur': '5','threp': '4'}, {'launaflokkur': '6','threp': '4'}],
'30-37 ára': [{'launaflokkur': '7','threp': '4'}, {'launaflokkur': '8','threp': '4'}],
'38-54 ára':  [{'launaflokkur': '9','threp': '4'}, {'launaflokkur': '10','threp': '4'}],
'55-59 ára': [{'launaflokkur': '10','threp': '4'}],
'60 ára+': [{'launaflokkur': '10','threp': '4'}]}

kennsluskylda = {'30 ára-': 24,
'30-37 ára': 24,
'38-54 ára':  24,
'55-59 ára': 23,
'60 ára+': 19}

vinnuskylda = {'30 ára-': 720,
'30-37 ára': 708,
'38-54 ára':  696,
'55-59 ára': 667,
'60 ára+': 551}

f = codecs.open('nidurstodur.txt','a', encoding='utf-8')  
f.write("synidaemi\tlaunaflokkur\tthrep\taldursflokkur\tkennsluskylda\tskertur\tvinnumat\tryrnun\tafangafjoldi\teiningar\tnemendafjoldi\tvinnuskylda\tlaun\n")

for aldur in aldursflokkar.keys():
    for lfthrep in aldursflokkar[aldur]:
        des = float(toflur[u'desemberuppbót'][u'2013'])
        orlof = float(toflur[u'orlofsuppbót'][u'2013'])
        laun = des + orlof
        laun /= 12
        grunn = float(toflur[u'2013'][lfthrep["launaflokkur"].decode(encoding='UTF-8')][lfthrep["threp"].decode(encoding='UTF-8')])
        yfirvinnutimar = 1.3*18*(2*4*3-kennsluskylda[aldur])
        laun += grunn
        laun + yfirvinnutimar*0.010385*grunn
        
        
        skrifa(u'2013',lfthrep["launaflokkur"],lfthrep["threp"], aldur, kennsluskylda[aldur],u'false',yfirvinnutimar,0,4,4*3,0,0,laun,f)
        
            
for nemfjoldi in range(15,33):
    for sd in d.keys():
        for aldur in aldursflokkar.keys():
            for lfthrep in aldursflokkar[aldur]:
                for skertur in [True,False]:
                    kennari = Kennari('Unnar',d)
                    for i in range(4):
                        if skertur:
                            kennari.add_class(Afangi("a",3,nemfjoldi,sd,d))           
                        else:
                            kennari.add_class(Afangi(str(i),3,nemfjoldi,sd,d))
                    if skertur:
                        kennari.discount()
                   
                    des = float(toflur[u'desemberuppbót'][u'2016'])
                    orlof = float(toflur[u'orlofsuppbót'][u'2016'])                                          
                    grunn = float(toflur[u'2016'][lfthrep["launaflokkur"].decode(encoding='UTF-8')][lfthrep["threp"].decode(encoding='UTF-8')])
                    
                    laun = float(des)
                    laun += float(orlof)
                    laun /= 12
                    laun += grunn
                    laun += 0.010385*float(max(0,kennari.vinnumat()-vinnuskylda[aldur]))*grunn/6
                    skrifa(sd,
                           lfthrep["launaflokkur"],
                           lfthrep["threp"],
                           aldur,
                           kennsluskylda[aldur],
                           skertur,
                           kennari.vinnumat(),
                           kennari.ryrnun,
                           4,
                           4*3,
                           nemfjoldi,
                           vinnuskylda[aldur],
                           laun,
                           f)
f.close()
