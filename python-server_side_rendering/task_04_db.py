from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_file():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error="Wrong source")

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv_file()
    else:  
        data = read_sqlite()
        if data is None:
            return render_template('product_display.html',
                                   error="Database error")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")

        filtered = [p for p in data if p['id'] == product_id]

        if not filtered:
            return render_template('product_display.html',
                                   error="Product not found")

        data = filtered

    return render_template('product_display.html',
                           products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
