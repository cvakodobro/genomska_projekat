# GenomicIT

Repository for the master course Genomic IT at the School of Electrical Engineering

## Zadatak 5
Implementirati na programskom jeziku Python algoritam za indeksirano pretraživanje stringova u zatadom tekstu koristeći Burrows-Wheeler transformaciju i FM index. Inicijalna verzija algoritma treba da bude realizovana na tradicionalan način opisan na predavanju, bez optimizicije memorije i vremena izvršavanja (10 poena).

Za svaku od funkcija u kodu, kao i za sam finalni algoritam napisati testove (5 poena).

Izvršiti optimizaciju koda iz aspekta zauzeća memorije i vremena izvršavanja. Pokrenuti prethodno definisane testove i proveriti da li i dalje svi prolaze (regresiono testiranje). Izmeriti unapređenje zauzeća memorije i vremena izvršavanja koristeći kao test podatke 3 seta (10 poena):
* Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA
* Tekst: Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA
* Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.

Pripremiti prezentaciju (Google slides ili power point) inicijalnog i optimizovanog algoritma, kao i samih rezultata (5 poena).

Pripremiti video prezentaciju projekta (3 - 5 minuta trajanja) koja će biti dostupna na YouTube ili drugom on-line video servisu (10 poena).

## Komande za pokretanje analize i pertraživanje

### Pripremanje fajlova sa sufiksnim nizom i BWT pomoću SAIS algoritma
```
usage: sais.py [-h] -g FILE -sa SA_FILE -bwt BWT_FILE

Run SAIS algorithm on the given genome file

optional arguments:
  -h, --help            show this help message and exit
  -g FILE, --genome FILE
                        Genome file
  -sa SA_FILE, --suffix_array SA_FILE
                        Output file for the suffix array
  -bwt BWT_FILE, --bwt BWT_FILE
                        Output file for the BWT
```

Ova skripta podrazumeva postojanje izvrnog fajla sa implementacijom SAIS algoritma čiji se izvorni kod nalazi u folderu sais. 

Primer kreiranja sufiksnog niza i BWT za genom iz fajla `Coffea arabica chromosome 1c.fasta`:

`python sais.py -g "puna\putanja\do\fajla\Coffea arabica chromosome 1c.fasta" -sa "puna\putanja\do\fajla\gde\ce\biti\sacuvan\sufiksni\niz" -bwt puna\putanja\do\fajla\gde\ce\biti\sacuvana\bwt"`

### Pretraživanje genoma
```
usage: main.py [-h] -a {s,o} [-sa_f {1,2,4,8,16,32,64,128,256,512}] [-t_f {1,2,4,8,16,32,64,128,256,512}] [-sa SUFFIX_ARRAY_FILE] [-bwt BWT_FILE] -g FILE -p PATTERNS [PATTERNS ...]

Search for patterns in the fasta file

optional arguments:
  -h, --help            show this help message and exit
  -a {s,o}, --algorithm {s,o}
                        Choose simple or optimized algorithm
  -sa_f {1,2,4,8,16,32,64,128,256,512}, --suffix_array_factor {1,2,4,8,16,32,64,128,256,512}
                        Suffix array factor. Default 128
  -t_f {1,2,4,8,16,32,64,128,256,512}, --tally_factor {1,2,4,8,16,32,64,128,256,512}
                        Tally matrix factor. Default 128
  -sa SUFFIX_ARRAY_FILE, --suffix_array SUFFIX_ARRAY_FILE
                        Suffix array file
  -bwt BWT_FILE, --bwt BWT_FILE
                        BWT file
  -g FILE, --genome FILE
                        Genome file
  -p PATTERNS [PATTERNS ...], --patterns PATTERNS [PATTERNS ...]
                        Patterns to be searched for in the genome
```

Primer pretraživanja stringova `ACACAC`, `ATGCATGC`, `ATTTTATAT` u okviru fajla `Coffea arabica chromosome 1c.fasta` pomoću optimizovanog algoritma uz pripremljeni fajl sa sufiksnim nizom i faktorima 32 za sufiksni niz i 64 za tally matricu:

`python main.py -a o -sa_f 32 -t_f 64 -sa "puna\putanja\do\fajla\sa\sufiksnim\nizom" -g "puna\putanja\do\fajla\Coffea arabica chromosome 1c.fasta" -p ACACAC, ATGCATGC, ATTTTATAT`

Skripta sa testovima se naziva `bwt_fm_test.py`. Ona zahteva fajlove koji sadrže sufiksni niz za svaki od tekstova koji se testira ("", "ABAABA", "MAMA", "BANANA", "ABRACADABRA") i jedan fajl koji sadrži BWT teksta "ABRACADABRA". Svi fajlovi treba da imaju naziv kao tekst na koji se odnose zapisan malim slovima osmi za prazan tekst gde se fajl zove "empty". Ektstenzije fajlova treba da budu .suffix ili .bwt. Fajlovi se očekuju u folderu test.

Video: https://youtu.be/TBygWAThzgk
