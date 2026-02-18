## Go check it out live: [shubhpy.vercel.app](https://shubhpy.vercel.app)

`uvicorn <folder>.<filename>:<FastAPI_instance>`

(if main.py or app.py in root)

```
uvicorn app:app --reload
```
(change port if want)

```
uvicorn app:app --reload --port 3001
```

if under api/....
### For localdevelopment: better to install uvicorn manually: `pip install uvicorn`, then:

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
