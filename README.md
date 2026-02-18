`uvicorn <folder>.<filename>:<FastAPI_instance>`

```
uvicorn api.index:app --reload --port 3001
```

default port : 8000
```
uvicorn api.index:app --reload
```

<hr>

(if main.py in root)

```
uvicorn main:app --reload
```
(change port if want)

```
uvicorn main:app --reload --port 5000
```