# -*- coding: utf-8 -*-

class Afangi(object):
      def __init__(self,nafn,ein,fj,sd,tafla): 
          self.heiti = nafn
          self.einingar = float(ein);
          self.vm = -1;
          self.synid = tafla[sd]
          self.fjoldi = max(float(fj),float(self.synid[u'lagmark']));
          if (self.synid[u'heiti'] == ('Starfsbraut (1/3)').decode('utf-8') or self.synid[u'heiti'] == ('Starfsbraut (4/6)').decode('utf-8') or self.synid['heiti'] == ('Starfsbraut (7/12)').decode('utf-8')):
              if self.fjoldi > self.synid[u'hamark_e']:
                 self.fjoldi = self.synid[u'hamark_e']
                 
      def setVinnumat(self,vmt):
          self.vm = vmt
          
      def vinnumat(self):
          if self.vm != -1:
             return self.vm;
          else:
              ein =float(self.einingar);
              if (ein == 2 and (self.synid[u'heiti'] == ('Stærðfræði, hægferð').decode('utf-8') or self.synid[u'heiti'] == ('Íslenska, hægferð').decode('utf-8') or self.synid[u'heiti'] == ('Enska, hægferð').decode('utf-8') or self.synid['heiti'] == ('Danska, hægferð').decode('utf-8'))):
                  ein +=1
              fast = (float(self.synid[u'timar_namsAetlun']) + float(self.synid[u'verkefnisgerd']) + float(self.synid[u'lokaprof']) + float(self.synid[u'onnur_vinna']))*ein/float(3);
              kennslustundir = (40 + float(self.synid[u'undirb_kennslu']))/float(60)*2*15*ein;
              per_nemandi = (float(self.synid[u'vinna_per_nemanda']) + float(self.synid[u'fragangur_namsmats']) + float(self.synid[u'onnur_vinna_per_nemanda']))/float(60)
              per_nemandi = per_nemandi*ein/float(3);
              nemendur = float(0); 
              total = float(0)
              
              if (self.fjoldi <= float(self.synid[u'hamark_n'])):
                  nemendur = max(float(self.fjoldi),float(self.synid[u'lagmark']))*per_nemandi;
                  total = fast + kennslustundir + nemendur;
              elif (float(self.synid[u'hamark_n']) < self.fjoldi and self.fjoldi <= float(self.synid[u'hamark_e'])):
                   nemendur = float(self.synid[u'hamark_n'])*per_nemandi;
                   
                   total = fast + kennslustundir + nemendur + (self.fjoldi-float(self.synid[u'hamark_n']))*float(self.synid[u'kostn_per_nem_yn'])*ein/float(3)
              else:
                  nemendur = float(self.synid[u'hamark_n'])*per_nemandi;
                  total = fast + kennslustundir + nemendur
                  total += (float(self.synid[u'hamark_e'])-float(self.synid[u'hamark_n']))*float(self.synid[u'kostn_per_nem_yn'])*ein/float(3)
                  total += (self.fjoldi-float(self.synid[u'hamark_e']))*float(self.synid[u'kostn_per_nem_ye'])*ein/float(3)
          
              return total
      def umfram_nem(self):
          return int(self.fjoldi)-int(self.synid[u'lagmark'])
      
      def active_students(self):
          if (self.fjoldi <= float(self.synid[u'hamark_n'])):
              return float(self.fjoldi)
          elif (float(self.synid[u'hamark_n']) < self.fjoldi and self.fjoldi <= float(self.synid[u'hamark_e'])):
                return (float(self.fjoldi) -  float(self.synid[u'hamark_n']))*1.2 + float(self.synid[u'hamark_n'])   
          else:
              return 2*(float(self.fjoldi) -  float(self.synid[u'hamark_e'])) + 1.2*(float(self.synid[u'hamark_e']) -  float(self.synid[u'hamark_n'])) + float(self.synid[u'hamark_n'])             
      def active_hours(self):
          per_nemandi = (float(self.synid[u'vinna_per_nemanda']) + float(self.synid[u'fragangur_namsmats']) + float(self.synid[u'onnur_vinna_per_nemanda']))/float(60)
          return per_nemandi*self.active_students()
      def __str__(self):
          r = ('Nafn: ').decode('utf-8')
          r += self.heiti
          r += (' Sýnidæmi: ').decode('utf-8')
          r += self.synid['heiti']
          r += (' Fjöldi: ').decode('utf-8')
          r +=  (str(self.fjoldi)).decode('utf-8')
          r += (' Vinnumat: ').decode('utf-8')
          r += (str(self.vinnumat())).decode('utf-8')
          return r.encode('utf-8')
      
