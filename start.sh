echo "🔧 Ejecutando migraciones con Alembic..."
python -m alembic upgrade head

echo "🚀 Iniciando FastAPI..."
uvicorn main:app --host=0.0.0.0 --port=10000