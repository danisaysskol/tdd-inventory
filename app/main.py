from fastapi import FastAPI, HTTPException
from app.schemas import Product
from app.database import initialize_db, get_db_connection

app = FastAPI()

initialize_db()

@app.post('/products/', status_code=201)
def create_product(product: Product):
    """"
    Create a new product and return a new product intance
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO PRODUCTS (name, description, price, quantity) 
        VALUES (?,?,?,?)
''',(product.name, product.description, product.price, product.quantity))
    
    conn.commit()
    conn.close()
    return product


@app.get('/products/{product_id}', status_code=200)
def get_product(product_id : int):
    """"
    Get information of an specfic product
    """

    conn = get_db_connection()
    cursor = conn.cursor()
    db_response = cursor.execute('''
            Select *  from PRODUCTS where id = ?
    ''', (product_id,) )
    
    product = db_response.fetchone()
    conn.commit()
    conn.close()

    if product is None:
        raise HTTPException(status_code=404, detail="PRODUCT NOT FOUND")

    return dict(product)


@app.get('/products/', status_code=200)
def get_all_products():
    """"
    Get information of an specfic product
    """

    conn = get_db_connection()
    cursor = conn.cursor()
    db_response = conn.execute('''Select * from PRODUCTS''' )
    
    products = db_response.fetchall()
    conn.commit()
    conn.close()

    return [dict(product) for product in products]