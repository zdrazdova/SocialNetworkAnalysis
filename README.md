# SocialNetworkAnalysis

Nápady:


TODO

- [ ] napsat mrázovi znovu, ale co?

 - diametr sítě - chceme ukázat, že je malý, ale je trochu tricky jak říct, co už znamená malý. 
   - Nejspíš by to chtělo vygenerovat něčím podobný náhodný graf a říct, jaký je poloměr tam... Koukala jsem na náhodné grafy v networkx a nenarazila jsem na nic rozumného.. Ale myslím, že něco jako np.sample(všechny_dvojice_vrcholů, počet_hran_v_opravdické_síti), tyhle hrany dát do grafu a změřit vlastnosti.. Nebo udělat graf tak, že pro každou hranu platí, že je v tom grafu s pravděpodobností #počet_hran_v_opravdové_síti/#počet_možných_hran.
   - můžeme pak říct, že to teda je sociální sít strukturou

 - vykreslit graf, který ukáže, jestli je tam power degree distribution
   - můžeme pak říct, že to teda je sociální sít strukturou
   - pokud byhcom byly schopné nějak doplnit k těm letištím, z jakého roku jsou, tak by to mohla být cool animace a mohlo by tam být vidět, jak se právě připojují nody k těm "bohatším" a "rich get richer"

 - pustit na tom page rank, vykreslit výsledky
 - pustit na tom HITS - pokud ho jde najít někde
 - communities - pokud jde někde najít hotový nějaký algoritmus na to. 
   - ale zrovna u tohohle si nemyslím, že to něco najde.. přeci jen spíš než komunity tam dává smysl něco jako "core-periphery"
