# Imagen base con Python
FROM python:3.13-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias del ETL
RUN pip install --no-cache-dir -r etl/requirements.txt

# Crear la carpeta de salida si no existe
RUN mkdir -p output

# Comando por defecto al ejecutar el contenedor
CMD ["python", "etl/main.py"]
