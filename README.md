# Cluster Server

## server
django + rest framework

```
poetry install
python manage.py runserver 0.0.0.0:8001
```

## ui
vite + react

url for server is hardcoded to localhost:8001 in `App.tsx`

```
cd ui
yarn install
yarn dev
```

