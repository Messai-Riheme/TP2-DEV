# TP3 - Intégration Continue (FastAPI)

## Travail réalisé
- Création de la branche `feature/soustraction-with-unit-tests` à partir de `TP2-DEV`.
- Ajout de l'endpoint `GET /soustraction` dans `main.py`.
- Développement des tests unitaires dans `test_main.py` avec `TestClient` (`pytest`).
- Calcul de la couverture de code (`pytest --cov`) avec génération des rapports XML et HTML pour dépasser **90 %** de couverture.
- Analyse de la qualité du code avec **Pylint** (score visé : **10/10**).
- Mise en place du pipeline CI dans `.gitlab-ci.yml` avec les stages `code_quality` (`pylint`) et `test` (`run-test` avec rapport JUnit XML en artefact et `calculate-coverage` avec rapport de couverture).

## Commandes locales
```bash
pytest -v
pytest -v test_main.py --cov=. --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html
pylint main.py test_main.py