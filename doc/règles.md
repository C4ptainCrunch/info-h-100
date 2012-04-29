# Manuel d'utilisation

Voici le déroulement d'une partie-type du jeu de Scrabble simplifié.
Les règles du jeu diffèrent quelque peu des règles officielles du Scrabble.

Le but du jeu est de poser des mots les plus longs possible, à partir des lettres situées dans le chevalet du joueur.

Chaque lettre valant un certain nombre de points, il peut être intéressant de placer des lettres à plus fortes valeurs.
(Les détails pratiques du calcul des points sont affichés plus bas)

## Déroulement du jeu

Commencez par spécifier au programme le **nombre de joueurs** qui participent. (Maximum 4)

### Premier tour

Le plateau de jeu est affiché, ainsi que le chevalet du joueur.


![plateau](images/debut.png)

Au premier tour, le premier joueur est **obligé** de placer le mot tel qu'une des lettres soit positionnée au centre du plateau. Il peut également choisir de ne rien placer, et de se débarrasser de certaines lettres. (Il peut aussi choisir de ne se débarrasser d'aucune lettre.)

Une fois qu'il a choisi le(s) lettre(s) dont il veut se débarrasser , le chevalet est re-rempli à partir du sac et c'est au tour du joueur suivant.

#### Tours suivants

Une fois qu'un premier mot est placé sur le plateau de jeu, chaque nouveau mot doit avoir un point de contact avec les lettres déjà présentes sur le plateau.

Les joueurs peuvent aussi se baser sur les lettres déjà posées pour construire leurs nouveau mots.
Par exemple, si `jour` est déjà présent en jeu, il est possible de former `bonjour` en ayant uniquement `b` `o` `n` dans son chevalet.

Les joueurs peuvent aussi choisir de ne rien placer, et de se débarrasser de certaines lettres ou de passer leur tour, de la même manière qu'au premier tour


### Fin de la partie

Le jeu continue jusqu'à ce que le sac soit vide.
Dès que cela arrive, le joueur qui a le plus de points gagne la partie.

## Calcul des points

### Points par lettre

Chaque lettre posée vaut un certain nombre de points :
E, 1; A, 1; I, 1; N, 1; O, 1; R, 1; S, 1; T, 1; U, 1; L, 1; D, 2; G, 2; M, 2; B, 3; C, 3; P, 3; F, 4; H, 4; V, 4; J, 8; Q, 8; K, 10; W, 10; X, 10; Y, 10 et Z. 10 points

### Cases multiplicatrices

#### Mot compte double

Lorsqu'un joueur pose une lettre sur une case "mot compte double" ( `#2` sur le plateau de jeu), le total des points engendré par la pose du mot est doublé.

#### Mot compte triple

Lorsqu'un joueur pose une lettre sur une case "mot compte triple" ( `#3` sur le plateau de jeu), le total des points engendré par la pose du mot est triplé.

#### Lettre compte double

Lorsqu'un joueur pose une lettre sur une case "lettre compte double" ( `%2` sur le plateau de jeu), les points pour cette lettre sont doublés.

#### Lettre compte triple

Lorsqu'un joueur pose une lettre sur une case "lettre compte triple" ( `%3` sur le plateau de jeu), les points pour cette lettre sont triplés.

### Scrabble

Si un joueur pose toutes les lettres de son chevalet (7) d'un seul coup, il obtient un bonus de 50 points.

### Mots engendrés

Lors de la pose d'un mot sur le plateau, il est possible (et même probable) que certaines lettres du mot complètent ou forment un autre mot sur le plateau. Auquel cas, les points pour ce mot sont ajoutés au joueur.

En reprenant l'exemple ci-dessus, si `jour` est déjà présent en jeu, il est possible de poser `bon` et d'obtenir les points pour `bonjour`.