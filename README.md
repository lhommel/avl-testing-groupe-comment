# Guide d'installation:

- Afin d'exécuter le fichier de test (test_avl.py), il est nécessaire d'avoir installé sur le machine pytest-quickcheck :
```
$ pip install pytest-quickcheck
```

- Un script est disponible pour exécuter le programme de tests sous Linux :
```
$ ./script_test.sh
```
- Il est tout de même possible d'exécuter manuellement les tests. Voici la commande : 
```
$ py.test -v test_avl.py
```