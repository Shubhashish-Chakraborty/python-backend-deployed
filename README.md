`uvicorn <folder>.<filename>:<FastAPI_instance>`

```
uvicorn api.index:app --reload --port 3001
```

default port : 8000
```
uvicorn api.index:app --reload
```
<hr/>

Refered Vercel Official Doc: [FastAPI on Vercel](https://vercel.com/docs/frameworks/backend/fastapi)
> Vercel Python (ASGI) deployment

<p align='center'>
  <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/407b7be5-e555-42df-bb55-77029f965d6a" />
</p>


<hr>

(if main.py in root)

```
uvicorn main:app --reload
```
(change port if want)

```
uvicorn main:app --reload --port 5000
```
