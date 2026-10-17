
import mysql.connector
from db import get_connection


def view_products():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute("""
            SELECT product_id, product_name, price, stock
            FROM PRODUCTS
            WHERE is_active = TRUE
        """)

        products = cursor.fetchall()

        if not products:
            print("No active products found.")
        else:
            print("\n--- PRODUCT INVENTORY ---")
            for product in products:
                print(
                    f"ID: {product[0]} | "
                    f"Name: {product[1]} | "
                    f"Price: ₹{product[2]} | "
                    f"Stock: {product[3]}"
                )

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def add_product():
    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        if price <= 0:
            print("Price must be greater than 0.")
            return

        stock = int(input("Enter stock quantity: "))
        if stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Enter a valid price and whole-number stock.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            INSERT INTO PRODUCTS (product_name, category, price, stock)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, category, price, stock))
        connection.commit()

        print("Product added successfully!")

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()
        print("Database error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def update_product():
    try:
        product_id = int(input("Enter product ID: "))
        if product_id <= 0:
            print("Product ID must be greater than 0.")
            return

        new_price = float(input("Enter new price: "))
        if new_price <= 0:
            print("Price must be greater than 0.")
            return

        new_stock = int(input("Enter new stock quantity: "))
        if new_stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Please enter numbers in the correct format.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            UPDATE PRODUCTS
            SET price = %s, stock = %s
            WHERE product_id = %s AND is_active = TRUE
        """

        cursor.execute(query, (new_price, new_stock, product_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Product updated successfully!")
        else:
            print("Active product ID not found.")

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()
        print("Database error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def delete_product():
    try:
        product_id = int(input("Enter product ID to deactivate: "))
        if product_id <= 0:
            print("Product ID must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid numeric product ID.")
        return

    confirm = input("Deactivate this product? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Operation cancelled.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            UPDATE PRODUCTS
            SET is_active = FALSE
            WHERE product_id = %s AND is_active = TRUE
        """

        cursor.execute(query, (product_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Product deactivated successfully!")
        else:
            print("Product not found or already inactive.")

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()
        print("Database error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def low_stock_alert():
    connection=get_connection()
    cur=connection.cursor()
    try:
     query="SELECT product_id,product_name,stock FROM PRODUCTS WHERE stock<=5 and is_active=True"
    
     cur.execute(query)
     products=cur.fetchall()
    
     if products :
        print("----Low Stock Alert")
        for product in products:
            print(f"Price: {product["price"]}"
                  f"Id : {product["product_id"]} |",
                  f"Name : {product["product_name"]}|",
                  f"stock : {product["stock"]}")
     else:
        print("No low stock found")
        
    except Exception as e:
      print("ERROR",e)
      
    finally:
        cur.close()
        connection.close()
        
def search_product():
        connection=get_connection()
        cur=connection.cursor()
        
        try:
            product_name=input("Enter product name you wan to search")
            
            query ="SELECT * FROM PRODUCTS WHERE product_name='{}' and is_active=True".format(product_name)
            
            cur.execute(query)
            products=cur.fetchall()
            
            if products:
                for product in products:
                    print(f"Id : {product["product_id"]} |",
                  f"Name : {product["product_name"]}|",
                  f"stock : {product["stock"]}")
            else:
                print("No product Found")
                
        except Exception as e:
            print("ERROR :",e)
            
        finally:
            cur.close()
            connection.close()
            
        