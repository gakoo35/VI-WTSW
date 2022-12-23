from dash import dcc, html
concepts_layout = html.Div([
    dcc.Markdown("""
# Concepts du cours MA-VI appliqués

## Description du projet
La définition de l'indépendance financière est subjective, elle dépend de nos objectifs, de notre mode de vie, de 
notre lieu de résidence etc... Dans le cadre de ce projet, nous l'a définissons comme suit : L'indépendance financière 
c'est le fait de posséder un patrimoine suffisant pour subvenir à ces besoins sans devoir avoir une activité salariale. 
Pour le commun des mortels, celle-ci ne paraît pas atteignable à moins d'hériter beaucoup d'argent ou de gagner au 
loto… Cependant, il est possible de faire croître son capital de manière considérable sur le long terme en 
investissement régulièrement de petits montants en bourse. En effet, lors d'un investissement des intérêts sont 
touchés par les investisseurs. En accumulant ceux-ci au fil du temps, ils représentent alors une source de revenus 
considérable. L'interface de visualisation permet ainsi d'une part de présenter la puissance des intérêts composés 
mais également d'avoir un aperçu du temps qu'il faudra afin d'atteindre l'indépendance dans les différents pays du 
monde, à l'aide d'une carte interactive.

## Publique cible
Le publique cible de notre projet est assez ouvert mais reste tout de même ciblé pour les débutants en investissement. 
En effet, notre projet permet d'avoir une vue assez global de l'évolution de ses propres investissement. Il y a donc 
plusieurs aspects qui ont dû être mis de côté dans le domaine de la bourse, notamment concernant le taux 
d'intérêt changeant au fil des années. Ces simplifications permettent aux utilisateurs de plus facilement comprendre 
comment utiliser l'outil et qu'est-ce qu'il fait. Cela permet également très bien à des utilisateurs plus expérimentés dans 
le domaine de l'utiliser bien qu'il utilisent sûrement d'autres outils plus complets et plus complexes. 

## Données
Nous pensions initialement utiliser 2 set de données. Le premier, que nous n'avons pas utilisé, 
concerne le [SP500](https://www.kaggle.com/datasets/camnugent/sandp500). Il contient les informations concernant le 
prix des actions des entreprises comprise dans le SP500. Cet indice boursier regroupe les 500 plus grandes entreprises 
du monde et est très populaire. Ces informations concernent les dernières 5 années. Nous pensions l'utiliser pour 
définir le taux d'intérêt dans nos calcul mais, au fil du projet, nous avons trouvé plus pertinent de permettre 
à l'utilisateur de définir lui-même ce taux. En effet, le taux d'intérêt dépend grandement du type d'investissement de 
l'utilisateur et donc l'utilisation de ce dataset n'avait plus vraiment de sens.

Le deuxième dataset, [cost of living](https://www.kaggle.com/datasets/ankanhore545/cost-of-living-index-2022), regrouppe 
des informations concernant le coût de la vie dans différents pays. Ce coût est calculé en associant différentes 
informations tel que le prix des courses, des restaurants, des transports, du loyer, etc. Toutes ces informations là ne 
sont malheureusement que des indices, ce ne sont pas les prix réels. Afin de pouvoir avoir tout de même une idée du prix 
de la vie dans les différents pays, le dataset se base sur le prix de la vie à New York. Cela signifie que, si 
un pays à un indice de 120, le prix de la vie sera donc 20% plus cher qu'à New York. C'est donc ce dataset qui nous 
permet de déterminer si une personne est capable de vivre dans un pays ou non en fonction de son capital. 

Ce dataset, bien que très complet, a tout de même quelques blancs concernant certains pays (principalement en Afrique). 
Nous avons donc décidé de tout de même l'utiliser mais de ne pas ajouter valeur fictive pour ces pays manquants afin de 
ne pas induire l'utilisateur en erreur. Il y aura donc quelques pays pour lequels il est impossible de savoir le prix 
pour pouvoir y vivre. De plus, le dataset contient des indices, cela signifie que la valeur pour New York est de 
100%. Nous avons donc dû estimer le coût réel pour vivre à New York à 5'500$. Cette valeur est donc la base sur 
quoi repose toute notre application. C'est donc important de noter que cette valeur est propre à nous et n'est pas 
une information certifié. 

## Technologies
Concernant les technologies, nous avions prévu au départ de travailler avec [Observable](https://observablehq.com/). 
Cette technologie est un framework Javascript qui permet d'explorer et de visualiser de l'information. Nous 
avons tout de même pas retenu cette technologies pour plusieurs raisons. La première étant le fait que l'on doivent 
coder notre application en Javascript. Bien que cette technologie soit largement répandu dans le monde du Web, elle 
possède tout de même un grand nombre de défauts. Une deuxième raison est le fait que la surcouche ajouté par Observable 
paraissait assez complexe et pas très intuitif. C'est donc pour ces raisons que nous avons choisis d'utiliser une autre 
technologie. 

[Dash](https://dash.plotly.com/) est un framework Python, R, Julia et F# qui est construit sur la base de 
[Plotly.js](https://plotly.com/). Bien que cela soit basé sur un framework Javascript, cette surcouche Dash nous permet 
de travailler en Python. Ceci implique plusieurs avantages, notamment liés à la simplicité de ce langage. De plus, 
cette technologie nous permet de créer immédiatement une interface web qui contient nos différentes visualisations ainsi 
que d'une interface pour permettre à l'utilisateur de manipuler les données.

### Critique
Dash est un outil très complet et qui est très puissant pour être personnalisable. En effet, il permet très rapidement 
d'avoir un site web fonctionnel avec différents représentation visuels. Il permet aussi assez simplement de mettre 
en place des inputs pour permettre à l'utilisateur de manipuler les données. Il y a tout de même quelque concepts à 
"apprendre", notamment concernant les callbacks, mais cela reste dans l'ensemble assez intuitif d'utilisation. Un autre 
point important à noter est le fait que cette technologie est vraiment spécialisée dans la visualisation des données. 
Si le produit final voulu s'éloigne quelque peut de ce domaine, Dash devient limité dans ses fonctionnalités. 
Toutes les représentations que nous désirions implémenter était disponible avec Dash et tout cela dans le langage Python, 
avec lequel nous sommes familier et qui est assez simple d'utilisation. Nous sommes donc ravis de l'utilisation de cette 
outil dans le cadre de ce projet et nous avons encore beaucoup de fonctionnalités a explorer. 

## Choix des visualisations

### Stacked bar chart
![](assets/stacked1.png)
*Figure 1 : Stack bar chart montrant la puissance des intérêts composés*

Notre première visualisation est un « stacked bar chart ». En règle générale, un tel graphique ne devrait être constitué 
que de 4 à 8 colonnes et non 50, comme dans notre application. Cependant, ce choix est justifiable par le fait que 
le but principale de notre graphique est de montrer, à l'utilisateur, la puissance des intérêts composés. Ces 
derniers respectant une loi exponentielle, il ne serait pas judicieux de se contenter d'afficher les résultats des 8 
premières années. 

![](assets/stacked2.png)
*Figure 2 : survol d'une colonne avec son curseur*

Lorsque l'on souhaite obtenir plus de détails sur une valeur du graphique en particulier, il suffit de passer notre 
souris sur celle-ci, afin d'afficher les informations suivantes :  

- Le type de montant dont il s'agit (montant initial, ajout mensuel ou intérêt) 

- L'année à laquelle on se situe 

- La valeur du montant en question 

### Pie chart
Notre deuxième visualisation est un complément de la première. En effet, le désavantage d'un diagramme en colonne 
contenant des valeurs exponentielles est que les premières colonnes se compressent face à l'énorme poids des dernières 
(voir figure 1 ci-dessus). Bien qu'il suffit de placer son curseur sur une colonne pour en obtenir des informations 
précises, nous avons décidé d'ajouter un pie chart à notre application pour faciliter la lecteur des valeurs d'une 
colonne/d'une année en particulier.

![](assets/pie.png)
*Figure 3 : Pie Chart représentant une année d'investissement*

Le curseur permet également d'afficher des informations supplémentaires sur ce graphique. En effet, il permet 
d'afficher un rappel sur le type d'investissement survolé (investissement initial, mensuel ou intérêt) ainsi 
que la valeur de la part.

Ce graphique contient trois parts qui représentent chacune un des types d'investissements cités précédemment. Nous 
respectons donc la contrainte théorique spécifiant qu'un pie chart doit contenir entre 3 et 8 parts et qu'il doit 
commencer à midi.

Bien qu'il est conseillé d'utiliser des couleurs à fort contraste, nous avons opté pour un choix plus sobre et 
n'affichons que du vert. Ce choix s'explique part le fait que nous souhaitons garder une cohérence entre les 
différentes visualisations de notre application. De plus, étant donné que nous n'avons que 3 part différentes, 
il est facile de les différencier, même si nous ne jouons que sur la saturation d'une même couleur. Le fait de ne 
différencier que la saturation peut même s'avérer être un avantage pour les personnes atteintes de daltonisme.


### World map
![](assets/map.png)
*Figure 4 : Map de la Terre indiquant dans quel pays on peut vivre de nos rentes passives*

Notre dernière visualisation est une représentation de la Terre en 3D (ou carte choroplèthe), permettant de facilement distinguer tous 
les pays du monde. Les pays affichés en vert foncé sont ceux pour lesquels nos rentes passives (que l'on peut 
dégager de notre capital actuel) suffisent pour y vivre. En contrepartie, les pays affichés en vert clair (presque 
blanc), sont les pays qui nous sont momentanément financièrement inaccessibles.

En plaçant notre curseur sur un pays, on peut connaître le montant mensuel exact qui est nécessaire pour y vivre.

### Choix des couleurs
En ce qui concerne le choix de nos couleurs, nous en avons définis 2 principales. Voici le raisonnement derrière nos 
choix : 
- Vert comme couleur de l'année sélectionnée. Le vert permet de rappeler la nature et est donc cohérent pour nous de 
représenter des pays sur une carte du monde. 
- Bleu comme couleur des autres années. Le bleu est une couleur avec comme symbole la vérité et la sériosité. Cela nous 
permet de mettre en confiance l'utilisateur sur les informations que nous lui présentons. 

Nous avons également choisie ces 2 couleurs car, pour un daltoniens, elles sont souvent bien différenciables, même 
en noir et blanc. 

Nous avons décidé de conserver la couleur verte sur l'ensemble de nos représentation visuels afin de démontrer l'année 
sélectionné sur l'ensemble de nos visualisations.

Finalement, nous avons choisi un changement dans la saturation de la couleur pour séparé les différentes informations 
que l'on représente (investissement initial, investissements, intérêts). Le changement de saturation nous permet 
de conserver la distinction entre les 2 couleurs principales mais également de permettre aux daltoniens de pouvoir 
discerner les différentes informations. 

Voici un example des couleurs choisis : 

##### #A4BE7B
##### #5F8D4E
##### #285430
##### #14397d
##### #77b5d9
##### #d7eaf3


## Fonctionnement de l'application
Notre application fonctionne comme suit. 

Premièrement, l'utilisateur rempli les divers champs concernant ses investissement, à savoir :

- Son investissement initial
- Son investissement mensuel
- Le taux d'intérêt moyen qu'il pense atteindre
- La durée de l'indépendance financière souhaitée
    - Soit 30 ans (la durée moyenne d'une retraite)
    - Soit de manière indéterminée (sous-entendu : infinie)

![](assets/func1.png)
*Figure 5 : divers champs concernant les investissement de l'utilisateur*

Ensuite, il utilise le slider du haut de page pour simuler l'évolution de ses investissement en fonction 
des années (sur une échelle de 0 à 50 ans).

![](assets/func2.png)
*Figure 6 : Slider permettant de simuler l'évolution temporel d'un investissement*

Le déplacement du curseur du slider ajustera automatiquement les valeurs des divers visualisations présentées 
précédemment.

Enfin, en plus de pouvoir switcher entre 3 visualisations, l'utilisateur a également la possibilité de 
connaître la somme théorique de ses rentes mensuelles et de son capital total pour l'année sélectionnée, grâce aux 
champs suivant, affichés en bas à gauche de la page :

![](assets/func3.png)
*Figure 7 : montants théoriques du capital total et des rentes passives mensuelles*



""")
])