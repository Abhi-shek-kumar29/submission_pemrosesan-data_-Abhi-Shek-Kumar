from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_postgresql


DATABASE_URL = "postgresql://postgres:ABhi290805.@localhost:5432/products"


def main():
    try:
        raw_data = scrape_main()
        print(f"Jumlah data mentah: {len(raw_data)}")
        clean_data = transform_data(raw_data)
        print(f"Jumlah data bersih: {len(clean_data)}")
        save_to_csv(clean_data, "products.csv")

        # Aktifkan jika PostgreSQL sudah dibuat
        save_to_postgresql(
            clean_data,
            table_name="products",
            db_url=DATABASE_URL
        )

        print("ETL pipeline berhasil dijalankan.")
        print(clean_data.info())
        print(clean_data.head())

    except Exception as error:
        print(f"Error running ETL pipeline: {error}")

if __name__ == "__main__":
    main()