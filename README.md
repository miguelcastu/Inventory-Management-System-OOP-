# Python Inventory — Object-Oriented Programming Exercise

A small in-memory console application for adding products, searching by name,
listing inventory and calculating stock value. It demonstrates class boundaries,
basic validation and exception handling.

[Engineering portfolio](https://github.com/miguelcastu/miguelcastu) · [Project directory](https://github.com/miguelcastu/miguelcastu/blob/main/PROJECTS.md)

## Implementation

The source uses Spanish identifiers:

- `Producto`: name, price and quantity validation; price/quantity updates and
  `calcular_valor_total()`.
- `Inventario`: `agregar_producto()`, `buscar_producto()`,
  `calcular_valor_inventario()` and `listar_productos()`.
- `menu_principal()`: interactive console loop.

With Python 3, from the repository root:

```shell
python sistema_inventario.py
```

The interface is Spanish and values live only in process memory. Exiting loses
the inventory. There is no database, API, user authentication or automated suite.
This is a foundational learning exercise; the portfolio's detection platforms
demonstrate the larger engineering work.
