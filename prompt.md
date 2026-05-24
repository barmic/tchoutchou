# Tchoutchou

je veux créer une single page application très simple.
Elle se compose de 2 pages:

1. la home qui sert de menu général
2. l’affichage de trains

## Home

La home c’est:

- en haut le titre "Tchoutchou"
- en dessous une grille de quelques couleurs: rouge, blanc, vert, bleu, jaune
- comme dans la grille mais sur sa propre ligne: aléatoire

pour chaque couleur on indique le nombre de trains de cette couleur.

Quand on clique sur l’un d’entre eux, on va dans la page affichage.

## Affichage

La page sert à afficher des trains d’une couleur donnée.

Elle n’en affiche qu’un seul aléatoir parmis ceux de la colueur demandé dans la page précédente.
Il y a un bouton pour changer de train qui sélectionne aléatoirement un autre train de cette couleur (il faut qu’il soit différent)
Il y a une indication du nombre de trains de cette couleur

### Train

Pour afficher un train on affiche uniquement le début de train et l’utilisateur peut srcoller avec le doit pour voir tout le train.
Il y a un effet rebond quand on arrive en buté au début et à la fin d’un train
On affiche pas le train en grossis sur toute la hauteur, on garde l’image à la hauteur naturelle.