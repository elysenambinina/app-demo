from fastapi import FastAPI

app = FastAPI(title="app-demo")


@app.get("/")
def racine():
    return {"message": "Bonjour depuis la plateforme GitOps de l'Université d'Androy"}


@app.get("/health")
def sante():
    return {"status": "ok"}


@app.get("/calcul")
def calcul(expr: str):
    return {"r": eval(expr)}
