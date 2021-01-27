import xml.etree.ElementTree as ET

class Kursy:

    def __init__(self,source):
        mytree = ET.parse(source)
        myroot = mytree.getroot()
        self.Name = ['Polski Złoty']
        self.Converter = [1]
        self.Code = ['PLN']
        self.Course = ['1,0000']
        for x in myroot:
            if x.tag == 'pozycja':
                self.Name.append(x[0].text)
                self.Converter.append(x[1].text)
                self.Code.append(x[2].text)
                self.Course.append(x[3].text)

    def Kursy(self):
        print("Kursy: \n")
        print("Waluta", "Przelicznik", "Kod", "Kurs średni", sep="\t\t\t",end='\n\n')

        for x in range(0,len(self.Name)):
            print(self.Name[x],end="")
            for _ in range(0,(35-len(self.Name[x]))):
                print(' ',end='')
            if(int(self.Converter[x])>100):
                print(self.Converter[x], '{}\t'.format(self.Code[x]), self.Course[x], sep="\t\t")
            else:
                print(self.Converter[x],self.Code[x],self.Course[x],sep="\t\t\t")

    def PLNnaWalute(self,kwota,kod):
        kod = kod.upper()
        index = self.Code.index(kod)
        kwotawaluta = (kwota/float((self.Course[index]).replace(',','.')))*int(self.Converter[index])
        print("{} PLN to {} {}".format(kwota,kwotawaluta,kod))
        return kwotawaluta

    def WalutaNaWaluta(self,kwota,kod1,kod2):
        kod1 = kod1.upper()
        kod2 = kod2.upper()
        index1 = self.Code.index(kod1)
        index2 = self.Code.index(kod2)
        kwotawaluta = (kwota*float((self.Course[index1]).replace(',','.'))/float((self.Course[index2]).replace(',','.')))*(int(self.Converter[index2])/int(self.Converter[index1]))
        print("{} {} to {} {}".format(kwota,kod1,kwotawaluta,kod2))
        return kwotawaluta

kursy = Kursy('waluty.xml')
kursy.Kursy()
kursy.PLNnaWalute(43,"cad")
kursy.WalutaNaWaluta(99,'aud','hkd')