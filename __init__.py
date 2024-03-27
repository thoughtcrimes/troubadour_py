import random

random.seed()

class phonetic():
    def __init__(self,char,pow):
        self.char = char
        self.pow = pow
        
class phonetic_lib():

    def __init__(self):
        self.lib = []

    def add(self,char,pow):
        self.lib.append(phonetic(char,pow))

    def generate(self):
        return self.lib[random.randint(0,len(self.lib)-1)].char


        
class word_generator():

    def __init__(self):
        self.phonetic_lib = []
        self.phonetic_lib.append(phonetic_lib())
        self.phonetic_lib.append(phonetic_lib())
        
    def add(self,lib,char,pow):
        self.phonetic_lib[lib].add(char,pow)

    def generate(self,num,letters):
        random.seed()
        cursor = random.randint(0,1)
        
        for i in range(num):
            word = ""
            for l in range(letters):

                if(cursor==0):
                    cursor=1
                else:
                    cursor=0
                
                word+=self.phonetic_lib[cursor].generate()
            print(word)

        
        
    
wordgen = word_generator()
wordgen.add(0,'b',100)
wordgen.add(0,'c',100)
wordgen.add(0,'d',100)
wordgen.add(0,'f',100)
wordgen.add(0,'g',100)
wordgen.add(0,'h',100)
wordgen.add(0,'j',100)
wordgen.add(0,'k',100)
wordgen.add(0,'l',100)
wordgen.add(0,'m',100)
wordgen.add(0,'n',100)
wordgen.add(0,'p',100)
wordgen.add(0,'q',100)
wordgen.add(0,'r',100)
wordgen.add(0,'s',100)
wordgen.add(0,'t',100)
wordgen.add(0,'v',100)
wordgen.add(0,'w',100)
wordgen.add(0,'x',100)
wordgen.add(0,'y',100)
wordgen.add(0,'z',100)
wordgen.add(0,'bl',100)
wordgen.add(0,'br',100)
wordgen.add(0,'ch',100)
wordgen.add(0,'chr',100)
wordgen.add(0,'cht',100)
wordgen.add(0,'ck',100)
wordgen.add(0,'cl',100)
wordgen.add(0,'cr',100)
wordgen.add(0,'ct',100)
wordgen.add(0,'dr',100)
wordgen.add(0,'dt',100)
wordgen.add(0,'fl',100)
wordgen.add(0,'fr',100)
wordgen.add(0,'gh',100)
wordgen.add(0,'ght',100)
wordgen.add(0,'gl',100)
wordgen.add(0,'gr',100)
wordgen.add(0,'kl',100)
wordgen.add(0,'kn',100)
wordgen.add(0,'lb',100)
wordgen.add(0,'lc',100)
wordgen.add(0,'ld',100)
wordgen.add(0,'lf',100)
wordgen.add(0,'ll',100)
wordgen.add(0,'ln',100)
wordgen.add(0,'lph',100)
wordgen.add(0,'lt',100)
wordgen.add(0,'mn',100)
wordgen.add(0,'mp',100)
wordgen.add(0,'nb',100)
wordgen.add(0,'nd',100)
wordgen.add(0,'ndr',100)
wordgen.add(0,'ng',100)
wordgen.add(0,'ngh',100)
wordgen.add(0,'nk',100)
wordgen.add(0,'nt',100)
wordgen.add(0,'nth',100)
wordgen.add(0,'nk',100)
wordgen.add(0,'nn',100)
wordgen.add(0,'nz',100)
wordgen.add(0,'ph',100)
wordgen.add(0,'pl',100)
wordgen.add(0,'pp',100)
wordgen.add(0,'pr',100)
wordgen.add(0,'ps',100)
wordgen.add(0,'rb',100)
wordgen.add(0,'rc',100)
wordgen.add(0,'rd',100)
wordgen.add(0,'rg',100)
wordgen.add(0,'rh',100)
wordgen.add(0,'rj',100)
wordgen.add(0,'rk',100)
wordgen.add(0,'rm',100)
wordgen.add(0,'rn',100)
wordgen.add(0,'rp',100)
wordgen.add(0,'rr',100)
wordgen.add(0,'rt',100)
wordgen.add(0,'rv',100)
wordgen.add(0,'ry',100)
wordgen.add(0,'sc',100)
wordgen.add(0,'scr',100)
wordgen.add(0,'sch',100)
wordgen.add(0,'sh',100)
wordgen.add(0,'shr',100)
wordgen.add(0,'sk',100)
wordgen.add(0,'sl',100)
wordgen.add(0,'sm',100)
wordgen.add(0,'sn',100)
wordgen.add(0,'sp',100)
wordgen.add(0,'spl',100)
wordgen.add(0,'spr',100)
wordgen.add(0,'sq',100)
wordgen.add(0,'ss',100)
wordgen.add(0,'st',100)
wordgen.add(0,'str',100)
wordgen.add(0,'sw',100)
wordgen.add(0,'tch',100)
wordgen.add(0,'th',100)
wordgen.add(0,'thr',100)
wordgen.add(0,'tl',100)
wordgen.add(0,'tr',100)
wordgen.add(0,'tt',100)
wordgen.add(0,'ts',100)
wordgen.add(0,'tw',100)
wordgen.add(0,'vr',100)
wordgen.add(0,'wd',100)
wordgen.add(0,'wh',100)
wordgen.add(0,'wn',100)
wordgen.add(0,'wr',100)
wordgen.add(0,'xy',100)
wordgen.add(0,'yl',100)


wordgen.add(1,'a',100)
wordgen.add(1,'e',100)
wordgen.add(1,'i',100)
wordgen.add(1,'o',100)
wordgen.add(1,'u',100)
wordgen.add(1,'y',100)
wordgen.add(1,'ae',100)
wordgen.add(0,'aeu',100)
wordgen.add(1,'ai',100)
wordgen.add(1,'au',100)
wordgen.add(1,'io',100)
wordgen.add(1,'ia',100)
wordgen.add(1,'ea',100)
wordgen.add(1,'ee',100)
wordgen.add(1,'ei',100)
wordgen.add(1,'eia',100)
wordgen.add(1,'eu',100)
wordgen.add(1,'ie',100)
wordgen.add(0,'oa',100)
wordgen.add(0,'oe',100)
wordgen.add(0,'oi',100)
wordgen.add(0,'oo',100)
wordgen.add(0,'ou',100)
wordgen.add(0,'ioa',100)
wordgen.add(0,'aio',100)
wordgen.add(0,'aia',100)
wordgen.generate(40,3)