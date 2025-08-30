echo "Aplicando migraciones..."
alembic upgrade head

echo "Iniciando servidor FastAPI..."
uvicorn main:app --host=0.0.0.0 --port=10000