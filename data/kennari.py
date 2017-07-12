# -*- coding: utf-8 -*-
from afangi import Afangi

class Kennari(object):
      def __init__(self,name,tafla):
          self.heiti = name;
          self.heiti
          self.afangar = [];
          self.originalAfangar = [];
          self.ryrnun = float(0);
          self.fjoldi = float(0);
          self.units = int(0)
          self.students = int(0)
          self.tafla = tafla
          
      def add_class(self, afangi):
          self.afangar.append(afangi);
          self.originalAfangar.append(afangi);
          self.fjoldi += 1;
          self.units += int(afangi.einingar)
          self.students += int(afangi.fjoldi)
          
      def total_units(self):
          return self.units
      
      def total_students(self):
          return self.students
      
      def umfram_nem(self):
          s = 0
          for afangi in self.originalAfangar:
              s += int(afangi.umfram_nem())
          return s
      def discount(self):
          self.sort()
          i = 0
          while (i < len(self.afangar)):
                j = i;
                while (j < len(self.afangar) and self.afangar[i].heiti == self.afangar[j].heiti): 
                      j += 1
                if i == j:
                    i += 1
                    continue
                else:
                    nfj = float(0);
                    for s  in range(i,j):
                        nfj += float(self.afangar[s].fjoldi)
      
                    neFjAv = float(nfj)/float(j-i);
                    shadow = Afangi(self.afangar[i].heiti,self.afangar[i].einingar,neFjAv,self.afangar[i].synid['heiti'],self.tafla)
                    for k in range(len(self.originalAfangar)):
                        if ((j-i) == 2 and self.originalAfangar[k].heiti == self.afangar[i].heiti):
                              diff = float(self.originalAfangar[k].vinnumat())-float(0.04)*float(shadow.vinnumat())
                              self.originalAfangar[k].setVinnumat(diff)
                              self.ryrnun += float(0.04)*float(shadow.vinnumat());
                        elif ((j-i) == 3 and self.originalAfangar[k].heiti == self.afangar[i].heiti):
                              self.originalAfangar[k].setVinnumat(float(self.originalAfangar[k].vinnumat())-0.16/float(3)*float(shadow.vinnumat()))
                              self.ryrnun += 0.16/float(3)*float(shadow.vinnumat());
                        elif ((j-i) > 3 and self.originalAfangar[k].heiti == self.afangar[i].heiti):
                              ryrnunpr = 0.08*(j-i-2)/float(j-i)
                              self.originalAfangar[k].setVinnumat(float(self.originalAfangar[k].vinnumat())-float(ryrnunpr)*float(shadow.vinnumat()))
                              self.ryrnun += float(ryrnunpr)*float(shadow.vinnumat());
                    i = j;
  

      def sort(self):
          self.afangar = sorted(self.afangar, key=lambda afangi: afangi.heiti);

      def active_students(self):
          n = 0
          for afangi in self.originalAfangar:
              n += int(afangi.active_students())
          return n
      
      def active_hours(self):
          n = 0
          for afangi in self.originalAfangar:
              n += float(afangi.active_hours())
          return n

      def vinnumat(self):
          s  = 0
          for afangi in self.originalAfangar:
              s += afangi.vinnumat()
        
          return s
        
      def afangar_allir(self):
          return self.originalAfangar
        
      def __str__(self):
          return self.heiti.encode('utf-8')
          
      
