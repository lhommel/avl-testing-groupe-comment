# Rapport AVL
### Equipe "Comment": AIT KHEDDACHE Nouria, LHOMME Lucien, LAURENT Louis.

## Simple ToDo List

- Nous avons décidé comme sujet de faire une simple liste de tâches dans un fichier au format CSV, le tout programmé en Python. Pour ce faire, nous avons fait en sorte que des listes Python soient directement liées au fichier csv. Lorsqu'on décide d'ajouter, supprimer, vider une liste, le même traitement s'applique au fichier à l'appel de la fonction 'writeToCSVFile()'.

- Pour ce qui est du testing, nous avons décidé de tester toutes les fonctionnalités basiques des listes grâce à des tests unitaires. Il est possible de trouver différents tests correspondant à la même fonction :
    - C'est le cas de la fonction permettant de supprimer une donnée d'une liste. En effet, cette dernière possède un comportement différent dans le cas où l'on essaie de supprimer un élément d'une liste vide.
    - Cela s'applique également à la fonction permettant de tester l'appartenance d'une donnée à une liste: on peut obtenir plusieurs résultats, vrai lorsque l'élement est présent et faux sinon. Nous avons tester les deux cas.
    - Nous avons ensuite tester la fonction permettant d'inverser une liste de trois manières différentes: dans le cas basique, dans le cas où la liste ne comporte qu'un seul élément et dans le cas où la liste est vide.
    - Dans le même cheminement de pensées, nous avons tester de trouver la taille d'une liste lorsque celle-ci est vide.
    - Cela fonctionne de la même manière pour trouver le nombre d'occurences d'un élément dans une liste, nous avons tester que la fonction ait le bon comportement même dans le cas d'une liste vide.
    - Nous avons aussi tester que notre parser fonctionnait bien, même dans le cas où l'on cherche à parser une chaine de caractères vide.

- Nous avons également décidé d'utiliser des techniques de tests plus avancés. Nous avons utilisé la librairie QuickCheck implémentée en Python pour tester différents comportements sur des listes générées de manière aléatoire. C'est ainsi que nous avons testé notre fonction permettant d'appliquer l'état de la liste au fichier csv. Grâce à QuickCheck, nous générons une liste de caractères aléatoires, on la sérialise dans le fichier, puis on s'assure que le contenu du fichier soit bien identique avec la liste générée aléatoirement au début. Dans un souci de vouloir mettre en pratique ce que l'on avait appris du papier sur QuickCheck, nous avons voulu mettre en pratique la fonction reverse avec des listes aléatoires. C'est pourquoi nous avons réalisé d'avantages de tests pour cette dernière. On a observé son comportement dans le cas où l'on inverse deux fois la liste, dans le cas où l'on inverse deux listes identiques pour voir si les listes sont les mêmes à la fin et enfin dans le cas où l'on supprime un élément parmi la liste, on s'assure que la taille de la liste a bien diminué par rapport à la liste initiale. 

- Nous tenons à préciser que la librairie pytest-quickcheck semble quelque peu capricieuse en fonction de la machine sur laquelle on l'utilise. C'est pourquoi voici une capture d'écran qui atteste du bon fonctionnement de cette dernière.

![exécution_des_test](/Tests_avl.png "QuickCheck")

## V2 du Projet

- Suite à vos retours concernant notre première implémentation, nous avons décidé d'appliquer quelques changements au projet. Nous sommes passés de simples listes python à des objets, qui ont pour attribut un nom, une date ainsi qu'un état: FAIT ou A_FAIRE. Il est également possible de définir une priorité en tant qu'entier, le nombre le plus important étant la tâche la plus prioritaire. Cet attribut n'est pas obligatoire, si on ne le précise pas il est de base à 1.
Nous avons fait le choix de ne pas imposer de format pour la date, pour que l'utilisateur puisse indiquer une tâche à long terme sans forcément de date de fin. 
Cela a nécessité de faire un peu de refactoring sur nos tests, mais également d'ajouter des fonctionnalités et donc des cas à tester. 
- Nous avons implémenté un moyen de filtrer nos objets: il est possible de retrouver des tâches portants un certain nom, une certaine date ou qui sont dans l'état que l'on cherche. Il est également possible de trier les tâches selon leur priorité.
Tous ces cas ont été testés. 
- Nous avons pris la décision de laisser un utilisateur insérer plusieurs tâches portants le même nom dans sa liste de tâches à faire, à condition qu'elles soient datées différement. 
- A la place de simples chaînes de caractères, nous avons rajouté des exceptions que nous pouvons récupérer lors des tests. 
- Nous avons également pris la décision de mieux tester notre système de fichiers, en vérifiant que le fichier soit dans le bon format, c'est-à-dire avec 3 colonnes correspondants aux attributs, que le fichier ait la bonne extension (csv), que le fichier existe. 

- Encore une fois, voilà une capture d'écran de l'exécution des tests.

![exécution_des_test](/tests_avlV2.png "QuickCheck")


