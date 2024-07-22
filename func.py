import sqlite3
from datetime import datetime

def count_customers_on_date(db_path, date):
    """
    Conta o número de clientes cadastrados em uma data específica.

    Args:
        db_path (str): Caminho para o banco de dados SQLite.
        date (str): Data no formato 'YYYY-MM-DD'.

    Returns:
        int: Número de clientes cadastrados na data especificada.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
   
        query = "SELECT COUNT(*) FROM customers WHERE date(registered_at) = ?"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
  
        return result[0] if result else 0
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return 0
    finally:
        if conn:
            conn.close()

# utilização
if __name__ == "__main__":
    database_path = "path/to/your/database.db" 
    date_to_check = "2024-07-22" 
    
    total_customers = count_customers_on_date(database_path, date_to_check)
    print(f"Total de clientes cadastrados em {date_to_check}: {total_customers}")
