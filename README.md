# JbRistorant-
Apriori algorythme, delais programme, serveur min distance

<img src="https://user-images.githubusercontent.com/54853371/88558028-4d766f80-d02b-11ea-8b2e-18d1d886d285.png" width="1000px;">

<h3>Apriori algorythm: suggestion of other plates</h3>

c1 l1/c2 l2 and associate rules (by pairs of 2 of 100%) on 5000 simulates commands from 24 plates

<h3>Delais programme: delais service</h3>

a = time work * 0.9<br>
constante = 5 minutes

Delai cooker: (time all plates theoric / nb cooker) + a + constante <br>
Delai serveur: (nb menu / nb serveur) + (time distance * 2) + a + constante or  (nb menu / (nb serveur + (time distance * 2) + a + constante)

total delais = Delai cooker + Delai serveur

not only my fault if it wrong i got help


<h3>serveur min distance: serveur service</h3>

current pos (add closed list) -> min (all other table in command)
