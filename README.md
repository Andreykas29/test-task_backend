# Spy Cat Agency Backend

## How to run

1. Create and activate a virtual environment:


for windows

```bash
python -m venv venv
venv\Scripts\activate    
```

for linux/Mac

```bash
python -m venv venv
source venv/bin/activate  
```


2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
uvicorn app.main:app --reload
```


**API Documentation**

Cats API Collection

https://api.postman.com/collections/31180018-faea257c-6e5c-441b-82cf-ff13a0ecbfe4?access_key=PMAT-01JY4XYESWSBQ7FXXCHHSXDG52

Missions API Collection

https://api.postman.com/collections/31180018-5f592b0f-ad1b-4a7e-9317-f70dc8cbaf44?access_key=PMAT-01JY4Y06CMWZNKF5K74W92E66B

**Swagger**

http://127.0.0.1:8000/docs