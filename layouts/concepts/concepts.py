from dash import dcc, html
concepts_layout = html.Div([
    dcc.Markdown("""
# Concepts du cours MA-VI appliqués

## Description du projet

## Publique cible
Le publique cible de notre projet est assez ouvert mais reste tout de même cibler pour les débutants en investissement. 
En effet, notre projet permet d'avoir une vue assez global de l'évolution de ses propres investissement. Il y a donc 
plusieurs aspects qui ont dû être mis de côté dans le domaine de la bourse, notamment concernant le taux 
d'intérêt changeant au fil des années. Ces simplifications permettent aux utilisateurs de plus facilement comprendre 
comment utiliser l'outil et qu'est-ce qu'il fait. Cela permet très bien aussi à des utilisateurs plus expérimenté dans 
le domaine de l'utiliser bien qu'il utilisent sûrement d'autres outils plus complet et plus complexe. 

## Données
Pour les données, nous pensions initialement utiliser 2 set de données. Le premier, que nous n'avons pas utilisé, 
concerne le [SP500](https://www.kaggle.com/datasets/camnugent/sandp500). Il contient les informations concernant le 
prix des actions des entreprises comprise dans le SP500. Cet indice boursier regroupe les 500 plus grandes entreprises 
du monde et est très populaire. Ces informations concerne les dernières 5 années. Nous pensions l'utiliser pour 
définir le taux d'intérêt dans nos calcul, mais, au fil du projet, nous avons trouvé plus pertinent de permettre 
à l'utilisateur de définir lui-même ce taux. En effet, le taux d'intérêt dépend grandement du type d'investissement de 
l'utilisateur et donc l'utilisation de ce dataset n'a plus vraiment de sens.

Le deuxième dataset, [cost of living](https://www.kaggle.com/datasets/ankanhore545/cost-of-living-index-2022), regroupe 
des informations concernant le coût de la vie dans différents pays. Ce coût est calculé en associant différentes 
informations tel que le prix des courses, des restaurants, des transports, du loyer, etc. Toutes ces informations là ne 
sont malheureusement que des indices, ce ne sont pas les prix réels. Afin de pouvoir avoir tout de même une idée du prix 
de la vie dans les différents pays, le dataset se base sur le prix de la vie à New York. Cela signifie que, si 
un pays à un indice de 120, le prix de la vie sera donc 20% plus cher qu'à New York. C'est donc ce dataset qui nous 
permet de déterminer si une personne est capable de vivre dans un pays ou non en fonction de son capital. 

## Technologies
Concernant les technologies, nous avions prévu au départ de travailler avec [Observable](https://observablehq.com/). 
Cette technologie est un framework Javascript qui permet d'explorer et de visualiser de l'information. Nous 
avons tout de même pas retenu cette technologies pour plusieurs raisons. La première étant le fait que l'on doivent 
coder notre application en Javascript. Bien que cette technologie soit largement répandu dans le monde du Web, elle 
possède tout de même un grand nombre de défaut. Une deuxième raison est le fait que la surcouche ajouté par Observable 
paraissait assez complexe et pas très intuitif. C'est donc pour ces raisons que nous avons choisis d'utiliser une autre 
technologie. 

[Dash](https://dash.plotly.com/) est un framework Python, R, Julia et F# qui est construit sur la base de 
[Plotly.js](https://plotly.com/). Bien que cela soit basé sur un framework Javascript, cette surcouche Dash nous permet 
de travailler en Python. Ceci implique plusieurs avantages, notamment lié à la simplicité de ce langage. De plus, 
cette technologie nous permet de créer immédiatement une interface web qui contient nos différentes visualisations ainsi 
que d'une interface pour permettre à l'utilisateur de manipuler les données.

## Choix des visualisations

### Column chart

### Pie chart

### World map

### Choix des couleurs

## Fonctionnement de l'application
""")
])