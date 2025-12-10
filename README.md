# 📦 Inventory Management System (Python OOP)

This project implements a basic inventory system using **Object-Oriented Programming** in Python.

---

## 🧱 Project Structure

### Class `Product`
- Attributes: `name`, `price`, `quantity`
- Input validation
- Methods:
  - `update_price()`
  - `update_quantity()`
  - `calculate_total_value()`
  - `__str__()`

### Class `Inventory`
- Stores a list of `Product` objects
- Methods:
  - `add_product()`
  - `search_product()`
  - `calculate_inventory_value()`
  - `list_products()`

### Interactive Console Menu
The user can:
- Add new products  
- Search by name  
- List all products  
- Calculate total inventory value  
- Exit the system  

---

## ▶️ Run the Program
```bash
python sistema_inventario.py
