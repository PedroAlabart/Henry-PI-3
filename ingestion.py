import s3_conn
import pandas as pd

def main():
    # cargo csv de precios de propiedades
    productos = pd.read_csv('data/productos.csv')
    productos.to_parquet('productos.parquet', index=True)

    # Parámetros de configuración
    bucket_name = "bronze-pi3-bucket-530923036953"
    file_name = "productos.csv"  # archivo local a subir
    s3_key = "productos.parquet"  # ruta destino en el bucket


    
    s3_conn.s3.upload_file(file_name, bucket_name, s3_key)

    print(f"✅ Archivo subido a s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    main()