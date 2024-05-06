# Playground of SEM

- Partial Least Square Structural Equation Modeling

## Environment setup

Create virtual environment:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Prepare dependencies:

```shell
pip install -r requirements.txt
python3 -m ipykernel install --user --name=.venv
```

## Corporate reputation

![Corporate reputation structure](https://i.imgur.com/NWbhsWw.png)

- CUSA, customer satisfaction
- CUSL, customer loyalty
- COMP, company's competence
- LIKE, company's likeability
