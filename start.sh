echo "🔧 Ejecutando migraciones con Alembic..."
alembic upgrade head

echo "🚀 Iniciando FastAPI..."
uvicorn main:app --host=0.0.0.0 --port=10000