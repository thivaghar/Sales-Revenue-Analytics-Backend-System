from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sales"
    )

# ---------- Total Revenue ----------
@app.route("/api/total-revenue", methods=["GET"])
def total_revenue():
    conn = cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT ROUND(COALESCE(SUM(total_price), 0), 2) FROM order_items"
        )
        total = cursor.fetchone()[0]

        return jsonify({"total_revenue": total}), 200

    except Error as e:
        return jsonify({"error": "Database error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---------- Monthly Revenue ----------
@app.route("/api/monthly-revenue", methods=["GET"])
def monthly_revenue():
    conn = cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                DATE_FORMAT(order_date, '%Y-%m') AS month,
                ROUND(SUM(total_price), 2) AS revenue
            FROM order_items
            GROUP BY month
            ORDER BY month
        """)

        data = [{"month": row[0], "revenue": row[1]} for row in cursor.fetchall()]

        return jsonify({"monthly_revenue": data}), 200

    except Error:
        return jsonify({"error": "Database error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---------- Average Order Value ----------
@app.route("/api/average-order-value", methods=["GET"])
def average_order_value():
    conn = cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT ROUND(COALESCE(AVG(total_price), 0), 2) FROM order_items"
        )
        avg_value = cursor.fetchone()[0]

        return jsonify({"average_order_value": avg_value}), 200

    except Error:
        return jsonify({"error": "Database error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---------- Revenue by Region ----------
@app.route("/api/revenue-by-region", methods=["GET"])
def revenue_by_region():
    conn = cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT region, ROUND(SUM(total_price), 2) AS revenue
            FROM order_items
            GROUP BY region
            ORDER BY revenue DESC
        """)

        data = [{"region": row[0], "revenue": row[1]} for row in cursor.fetchall()]

        return jsonify({"revenue_by_region": data}), 200

    except Error:
        return jsonify({"error": "Database error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---------- Revenue by Category ----------
@app.route("/api/revenue-by-category", methods=["GET"])
def revenue_by_category():
    conn = cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT category, ROUND(SUM(total_price), 2) AS revenue
            FROM order_items
            GROUP BY category
            ORDER BY revenue DESC
        """)

        data = [{"category": row[0], "revenue": row[1]} for row in cursor.fetchall()]

        return jsonify({"revenue_by_category": data}), 200

    except Error:
        return jsonify({"error": "Database error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---------- App Runner ----------
if __name__ == "__main__":
    app.run(debug=True)
