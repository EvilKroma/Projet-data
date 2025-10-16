# Le projet data — Documentation E3-FI-3-S1-UPM-Python-visualisation-données 
Objectif[](#objectif "Lien vers cette rubrique")
-------------------------------------------------

L’objectif du mini projet est d’éclairer un sujet d’intérêt public (météo, environnement, politique, vie publique, finance, transports, culture, santé, sport, économie, agriculture, écologie, etc…) que vous choisissez librement. Vous utiliserez des données publiques Open Data, accessibles et non modifiées.

_l’open data (ou donnée ouverte) est une donnée numérique d’origine publique ou privée. Elle peut être notamment produite par une collectivité, un service public (éventuellement délégué) ou une entreprise. Elle est diffusée de manière structurée selon une méthode et une licence ouverte garantissant son libre accès et sa réutilisation par tous, sans restriction technique, juridique ou financière._ [Wikipedia](https://fr.wikipedia.org/wiki/Open_data).

**Le choix du sujet est libre** mais doit satisfaire les livrables ci dessous. Il est soumis à validation de l’enseignant.

Remise du travail[](#remise-du-travail "Lien vers cette rubrique")
-------------------------------------------------------------------

Votre travail doit être déposé sur une plateforme de dépôt delon les modalités précisées sur la page de l’unité.

Les livrables[](#les-livrables "Lien vers cette rubrique")
-----------------------------------------------------------

Votre travail sera accessible sous la forme d’un dépôt Git public.

Vous devez produire un dashboard présentant a minima un histogramme et une représentation géolocalisée. Au moins un des graphiques doit être dynamique. Le dashboard s’exécute votre dans un navigateur web standard.

Le dashboard est construit avec du code Python structuré. Le code devra recueillir et nettoyer les données, les sélectionner et les organiser pour les représentations graphiques interactives illustrant votre point de vue sur le sujet. Le code devra être documenté.

A minima, le dépôt contiendra les éléments ci dessous :

*   [Les fichiers](#les-fichiers) nécessaires à l’exécution du dashboard ;
    
*   [Le fichier README](#le-fichier-readme) ;
    
*   [Le fichier requirements.txt](#le-fichier-requirements-txt) ;
    
*   [La vidéo](#la-video) de démonstration du dashboard.
    

### Les fichiers[](#les-fichiers "Lien vers cette rubrique")

Le dépôt contiendra l’ensemble des fichiers nécessaires à l’exécution du dashboard, structurés dans différents répertoires.

Un fichier `main.py` sera placé à la racine du dépôt, de telle sorte que le dashboard se lance avec la commande

Un jeu de données initial nécessaire à l’exécution du dashboard sera stocké localement de telle sorte que le dashboard puisse s’exécuter a minima sans connexion internet.

Les fichiers du projet doivent être structurés dans différents répertoires. Par exemple:

```
data_project
|-- .gitignore
|-- .venv
|   |-- *
|-- config.py                                   # fichier de configuration
|-- main.py                                     # fichier principal permettant de lancer le dashboard
|-- requirements.txt                            # liste des packages additionnels requis
|-- README.md
|-- data                                        # les données
│   |-- cleaned
│   │   |-- cleaneddata.csv
│   |-- raw
│       |-- rawdata.csv
|-- images                                      # images utilisées dans le README
|-- src                                         # le code source du dashboard
|   |-- components                              # les composants du dashboard
|   |   |-- __init__.py
|   |   |-- component1.py
|   |   |-- component2.py
|   |   |-- footer.py
|   |   |-- header.py
|   |   |-- navbar.py
|   |-- pages                                   # les pages du dashboard
|   |   |-- __init__.py
|   |   |-- simple_page.py
|   |   |-- more_complex_page
|   |   |   |-- __init__.py
|   |   |   |-- layout.py
|   |   |   |-- page_specific_component.py
|   |   |-- home.py
|   |   |-- about.py
|   |-- utils                                   # les fonctions utilitaires
|   |   |-- __init__.py
|   |   |-- common_functions.py
|   |   |-- get_data.py                         # script de récupération des données
|   |   |-- clean_data.py                       # script de nettoyage des données
|-- video.mp4

```


### Le fichier README[](#le-fichier-readme "Lien vers cette rubrique")

Le dépôt contient à sa racine un fichier `README` formatté en [Markdown](https://www.markdownguide.org/) renseigné avec :

*   une section `User Guide` qui fournit les instructions pour déployer et utiliser votre dashboard sur une autre machine ;
    
*   une section `Data` qui renseigne sur les données utilisées ;
    
*   une section `Developer Guide` qui renseigne sur l’architecture du code et qui permet en particulier d’ajouter simplement une page ou un graphique ;
    
*   une section `Rapport d'analyse` qui met en avant les principales conclusions extraites des données ;
    
*   une section `Copyright` qui atteste de l’originalité du code fourni. Par exemple :
    
    > *   je déclare sur l’honneur que le code fourni a été produit par moi/nous même, à l’exception des lignes ci dessous ;
    >     
    > *   pour chaque ligne (ou groupe de lignes) empruntée, donner la référence de la source et une explication de la syntaxe utilisée ;
    >     
    > *   toute ligne non déclarée ci dessus est réputée être produite par l’auteur (ou les auteurs) du projet. L’absence ou l’omission de déclaration sera considéré comme du plagiat.
    >     
    

Astuce

Pour la section « Developper Guide », utiliser [mermaid](https://docs.gitlab.com/ee/user/markdown.html#mermaid) pour fournir l’architecture du code sous forme de graphique. Le graphique est décrit par du texte selon la syntaxe suivante :

*   [programmation impérative](https://mermaid-js.github.io/mermaid/#/flowchart) : le code est structuré en fonctions appelées depuis le programme principal ;
    
*   [programmation orientée objet](https://mermaid-js.github.io/mermaid/#/classDiagram), : le code est structuré en classes.
    

Cet [éditeur en ligne](https://mermaid-js.github.io/mermaid-live-editor/#) permet une visualisation rapide.

### Le fichier `requirements.txt`[](#le-fichier-requirements-txt "Lien vers cette rubrique")

Le fichier `requirements.txt` doit contenir la liste des **seuls packages additionnels requis** tel que la commande ci dessous installe l’ensemble des dépendances nécessaires (et uniquement celles là):

```
$ python -m pip install -r requirements.txt

```


Avertissement

Le fichier `requirements.txt` doit être construit manuellement. La commande

```
$ python -m pip freeze > requirements.txt

```


construit la liste de tous les packages présents dans l’installation et ne doit pas être utilisée.

### La vidéo[](#la-video "Lien vers cette rubrique")

Vous devez fournir une vidéo de démonstration de votre dashboard (3 minutes max). Cette vidéo doit montrer l’ensemble des fonctionnalités et des interactions du dashboard.

Astuce

[OBS Studio](https://obsproject.com/fr) est une solution open source performante pour réaliser des vidéos de démonstration.

Setup[](#setup "Lien vers cette rubrique")
-------------------------------------------

Créer un répertoire de travail local et initialiser un dépôt git:

```
$ mkdir data_project
$ cd data_project
$ git init

```


Configurer git. Les champs `user.name` et `user.email` doivent impérativement être ceux du système d’information de l’ESIEE. Ils doivent être définis sur toutes les machines utilisées pour le développement

```
$ git config --local user.name "Lazare Garcin"
$ git config --local user.email "lazare.garcin@esiee.fr"

```


Astuce

Vous pouvez vous assurer du paramétrage avec

Sur la plateforme de dépôt, créer un nouveau dépôt public. Son adresse est nécessaire pour établir la relation entre le répertoire local et le dépôt distant

```
$ git remote add origin git@github.com:LazareGarcin/DataProject.git

```


Sur la machine locale, après avoir créé/modifié/supprimé un ou plusieurs fichiers

```
$ git add .
$ git commit -m "Initial commit"
$ git branch -M main
$ git push -u origin main

```


Contexte du développement[](#contexte-du-developpement "Lien vers cette rubrique")
-----------------------------------------------------------------------------------

Le dashboard sera développé avec les versions les plus récentes disponibles au 1er septembre de l’année universitaire :

*   du langage [Python](https://www.python.org/doc/versions) ;
    
*   de [pandas](https://pandas.pydata.org/), [dash](https://github.com/plotly/dash/releases) et [plotly](https://github.com/plotly/plotly.py/releases) ;
    
*   et plus généralement des autres packages utilisés dans le mini projet.
    

Avertissement

Bien qu’il existe d’autres alternatives, les technologies explicitement citées ci dessus sont performantes, customisables et largement répandues dans la communauté. Elles sont imposées.

Les données[](#les-donnees "Lien vers cette rubrique")
-------------------------------------------------------

### Accès[](#acces "Lien vers cette rubrique")

Les données doivent être accessibles publiquement, de façon reproductible, via une ressource statique ou une API publique. Dans tous les cas, le(s) pointeur(s) vers les ressources doi(ven)t être fourni(s) dans la section « Data » du fichier `README.md`.

Les données seront récupérées sur le web avec `get_data.py`. Ce script devra être capable de stocker les données dans le répertoire `data/raw/` du projet. Dans ce répertoire, les données seront stockées dans un format brut, sans modification.

Les données seront dites « statiques » si elles sont récupérées sous la forme d’un fichier au format quelconque (CSV, Excel, JSON, etc.)

Les données seront dites « dynamiques » si :

*   elles sont accessibles sur une page web statique via un processus de scraping ;
    
*   elles sont accessibles sur une page web dynamique (les données sont générées à la volée par un serveur). On les obtient alors généralement par l’utilisation d’un browser headless, [Selenium](https://selenium-python.readthedocs.io/) par exemple ;
    
*   elles sont accessibles via une API. Dans ce cas, `get_data.py` devra être capable de récupérer les données via cette API et de les stocker dans le répertoire `data/raw/` du projet.
    

Dans le cas de données dynamiques, le dashboard mettra en cache une partie des données avec un mécanisme de rafraichissement.

Si besoin, les données brutes recueillies, pourront être nettoyées avec `clean_data.py`. Ce script devra être capable de stocker les données nettoyées dans le répertoire `data/cleaned/` du projet. Dans ce répertoire, les données seront stockées dans un format exploitable par le dashboard.

### Structure[](#structure "Lien vers cette rubrique")

Dans la très grande majorité des cas, l’ensemble des données (dataset) est présenté sous la forme d’une (ou plusieurs) page de tableur, dont les lignes sont les `OBS` observations et les colonnes, les `VAR` variables (numériques, ordinales ou catégorielles) de ces observations.

Ce dataset doit impérativement posséder les propriétés suivantes:

*   il doit posséder un nombre suffisamment grand d’observations `OBS` pour que le tracé d’un histogramme ait du sens (typiquement plusieurs centaines). Ainsi :
    
    > *   les statistiques sur les communes françaises sont éligibles (`OBS` > 36000)
    >     
    > *   celles concernant les pays conviennent (~ 200, variable selon les sources)
    >     
    > *   mais celles concernant les département français ne conviennent pas (`OBS` < 100) ;
    >     
    
*   parmi l’ensemble des données `VAR` disponibles sur chacune des lignes, l’une au moins doit être numérique et non catégorielle. Une donnée non catégorielle posséde une relation d’ordonnancement (plus petit que, plus grand que). Exemple : la pression atmosphérique, le poids, le coût, le nombre, etc… Attention à l’utilisation de l’année comme donnée numérique, le plus souvent cette dernière est utilisée comme donnée catégorielle ;
    
*   les observations devront pouvoir être géolocalisées. Exemple : la température mesurée pour plusieurs stations météo, la taille relevée dans des zones géographiques différentes, le point de chute de météorites, etc.. Soit directement si les coordonnées géographiques sont incluses dans les observations, soit indirectement en faisant appel à une autre ressource.
    

Si le nombre `OBS` d’observations est très grand, les observations peuvent être sous catégorisées pour donner du sens à l’analyse. Exemple : la température mesurée pour différentes heures du jour et de la nuit, la taille relevée pour chacun des deux sexes, les dépenses de fonctionnement des villes de moins de 5000 habitants, etc…

En résumé, pour vérifier que le jeu de données choisi convient, vous devrez donc vous assurer que:

*   le nombre `OBS` d’observations est suffisamment grand ;
    
*   la donnée à représenter sous forme d’histogramme n’est pas catégorielle ;
    
*   une géolocalisation est possible.
    

Pour la géolocalisation, il est accepté qu’elle soit construite à partir d’un dataset différent de celui utilisé pour l’histogramme, du moment que le contexte des deux jeux de données est le même.

Evaluation du travail[](#evaluation-du-travail "Lien vers cette rubrique")
---------------------------------------------------------------------------

Le projet à évaluer sera déployé avec la commande:

```
$ git clone adresse_publique_de_votre_projet

```


Le dashboard sera lancé avec la commande:

Avertissement

Gardez à l’esprit que votre travail sera déployé dans un contexte différent de celui de votre machine de développement. L’exécution du dashboard :

> *   ne doit pas produire de warnings dans la console ;
>     
> *   ne pas produire d’erreur de call back dans le navigateur web.
>     

Le dashboard doit être fonctionnel à la première tentative. Chaque interaction supplémentaire avec l’évaluateur sera assortie d’un point de pénalité. Les causes les plus fréquentes :

*   référence à un fichier local à la machine de développement ;
    
*   utilisation d’un package obsolète ;
    
*   utilisation d’un package non recensé dans `requirements.txt`.
    

Votre code doit être structuré en fonctions, classes, modules et packages et documenté :

*   par des noms de variables explicites ;
    
*   avec des commentaires précisant **pourquoi** on exécute les principales instructions ;
    
*   avec des [docstrings](https://peps.python.org/pep-0257/), voire du [typing](https://docs.python.org/3/library/typing.html) pour les fonctions/classes utilisées.
    

Les structures de données doivent être adaptées et les « bonnes pratiques » du langage mises en oeuvre. L’utilisation d’un linter tel que [ruff](https://docs.astral.sh/ruff//) est fortement recommandée.

### Grille évaluation[](#grille-evaluation "Lien vers cette rubrique")

Ci dessous, une liste non limitative des critères pouvant être utilisés pour l’évaluation. Ces critères ne sont pas d’égale importance.

*   Le dépôt
    
    *   montre une utilisation régulière de git et une contribution équilibrée de tous les membres ;
        
    *   le `README` est renseigné conformément au paragraphe [Le fichier README](#le-fichier-readme);
        
    
*   Le dashboard
    
    *   l’instruction pour le produire est présente dans le `README` et il se lance sans erreur ;
        
    *   contient les représentations graphiques décrites dans le paragraphe [Les livrables](#les-livrables) ;
        
    *   les graphiques sont correctement documentés (titre, label des axes, etc.) ;
        
    *   est dynamique et fluide ;
        
    *   est de façon générale de bonne qualité.
        
    
*   Le code
    
    *   est structuré en packages, modules, classes, fonctions ;
        
    *   est lisible et commenté ;
        
    *   met en oeuvre les bonnes pratiques du langage ;
        
    *   utilise des structures de données et des packages/modules adaptés.
        
    
*   Les données
    
    *   adressent un problème d’intérêt général ;
        
    *   sont stockées de façon structurée : cf [Les fichiers](#les-fichiers) ;
        
    *   sont riches et abondantes ;
        
    *   `get_data.py` est présent.
        
    

A chaque item, un grade est attribué:

*   4 : tout à fait d’accord
    
*   3 : plutôt d’accord
    
*   2 : ni vraiment d’accord, ni vraiment en désaccord
    
*   1 : plutôt en désaccord
    
*   0 : tout à fait en désaccord
    

Ces critères garantissent un projet complet, structuré et développé selon les bonnes pratiques.

FAQ[](#faq "Lien vers cette rubrique")
---------------------------------------

**Je suis assez familière avec Pycharm, est-ce que je peux l’utiliser à la place de Visual Studio Code ?**

oui vous pouvez utiliser PyCharm si vous le maitrisez.

**Je rencontre des difficultés pour installer geopandas sous Windows ? Y a t-il une démarche particulière à faire ?**

Vous pouvez suivre ce lien : [https://geoffboeing.com/2014/09/using-geopandas-windows/](https://geoffboeing.com/2014/09/using-geopandas-windows/).

**Quelle est la bonne pratique pour détecter les packages manquants avant l’exécution ?**

Une bonne façon de faire est d’utiliser [importlib](https://docs.python.org/3/library/importlib.html) et en particulier la fonction [find\_spec](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec)

```
import importlib

name = "an_unknown_package"
spec = importlib.util.find_spec(name)
if spec is None:
    print(f"can't find {name!r}")

```


**Je souhaite structurer mon projet en plusieurs répertoires, comment se passent les imports ?**

Il faut utiliser des [packages](https://docs.python.org/3/tutorial/modules.html#packages) en créant un fichier `__init__.py` à l’intérieur des sous répertoires. En considérant l’exemple suivant

```
mon_projet/
    __init__.py
    main.py
    data/
        __init__.py
        get_data.py
    dashboard/
        __init__.py
        app.py
        layout.py
        callbacks.py
    README.md
    requirements.txt

```


Depuis `main.py` les imports se font alors avec la syntaxe

```
from data.get_data import get_data
from dashboard.app import app
from dashboard.layout import layout
from dashboard.callbacks import register_callbacks

```


Pour les imports intra package, lire le paragraphe [Intra-package References](https://docs.python.org/3/tutorial/modules.html#intra-package-references) de la documentation. [Cet article](Intra-packageReferences) donne un exemple détaillé.