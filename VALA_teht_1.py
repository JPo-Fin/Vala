# VALA_teht_1.py
import sys
import re


monikerrat_a = []
monikerrat_b = []
luku_x = 0
luku_a = 0
luku_b = 0  


    # luetaa luvut A, B ja X tiedostosta Vala_input.txt rivi kerrallaan ja käsitellään jokainen rivi erikseen jatkossa
    # lasketaan monikerta X:stä luvulla A ja luvulla B
    # ja tulostetaan jokaiset monikerrat X:stä jotka ovat PIENEMPIÄ kuin X
    # Tulostetaan X ja monikerrat (A ja B) muodossa X:A1 A2 A3 ... An , X:B1 B2 B3 ... Bn
    # X:A ja X:B pitää olla pienempiä kuin X
    # lisätty tarkastuksia avattavaa tiedostoon liittyen (mm. tiedoston olemassaolo, ei numeeriset arvot ja tietueiden min määrä per rivi)

if __name__ == "__main__":
        Lue_avattava_tiedosto = sys.argv[1] if len(sys.argv) > 1 else exit (print(f'Virhe: Luettavan tiedoston nimi puuttuu'))
        try:
            f = open(Lue_avattava_tiedosto, 'rb')
        except FileNotFoundError:
            print("Virhe: Tiedostoa {} ei löydy".format(Lue_avattava_tiedosto))
            exit()  

        Tallenna_tiedosto = sys.argv[2] if len(sys.argv) > 2 else exit (print(f'Virhe: Tallennettavan tiedoston nimi puuttuu') )

        with open(Lue_avattava_tiedosto, 'r') as file:
            lines = file.readlines()
            # Poistetaan  ylimääräiset välilyönnit ja rivit ja muutetaan string muotoon
            poista = [rivi.strip() for rivi in lines]
            #muutetaan string -muotoon
            res = ''.join(poista)
            #Poistetaan välilyönnit
            res2 = res.replace(' ','')  # saadaan muuttuja res2, jossa ei ole välilyöntejä ja sen arvo on esim. "537284958166"
            # Tarkistetaan löytyykö ei-numeerisia arvoja 
            if not res2.isdigit():
                exit(print(f'Virhe: Avattavassa tiedostossa on EI numeerisia arvoja. Suoritus pysäytetty.'))
            else:
                 pass
            
        for line in lines:
            numbers = line.split()
            # tarkastetaan että listassa ei ole virheellisiä arvoja -1, 0, None tai tyhjiä arvoja
            for arvo in numbers:
                if arvo in ('-1', '0', '', 'None'):
                    print(f"Virhe: listassa virheellinen arvo ({arvo})")
                    sys.exit(1)  # Lopettaa ohjelman virhekoodilla 1
                else:
                    pass    
            #tarkastetaan että listan rivillä on vähintään kolme tietuetta
            virheelliset = [r for r in numbers if len(numbers) < 3]
            if virheelliset:
                exit(print("Virhe: Tiedoston riveissä on liian vähän tietueita:"))
            else:
                pass

            luku_a = int(numbers[0])
            luku_b = int(numbers[1])
            luku_x = int(numbers[2])

        #järjestellään data list "lines", viimeisen luvun_X:n perusteella (index [2]) nousevaan järjestykseen   
        lines = sorted(lines, key=lambda x: int(x.split()[2]))

        # Käydään läpi järjestetty data list "lines" ja käsitellään jokainen rivi erikseen
        for line in lines:
            numbers = line.split()
            luku_a = int(numbers[0])
            luku_b = int(numbers[1])
            luku_x = int(numbers[2]) 

            # lasketaan monikerrat A:sta ja B:stä X:ään asti    
            monikerrat_a = [luku_a * ia for ia in range(1, luku_x // luku_a + 1)]
            monikerrat_b = [luku_b * ib for ib in range(1, luku_x // luku_b + 1)]

            #käydään läpi listat ja poistetaan ne jotka ovat suurempia kuin X tai yhtäsuuret kuin X
            monikerrat_a = [ia for ia in monikerrat_a if ia < luku_x]
            monikerrat_b = [ib for ib in monikerrat_b if ib < luku_x]
            print(f'{luku_x}: {monikerrat_a} {monikerrat_b}')
            
            # tallennetaan tulokset tiedostoon Vala_output.txt (append mode, jatketaan tiedoston kirjoitusta viimeisen rivin jälkeen)
            with open(Tallenna_tiedosto, 'a') as file:       
                file.write(f'{luku_x}: {monikerrat_a} {monikerrat_b}\n')    