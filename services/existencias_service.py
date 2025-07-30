from infrastructure.odoo_rpc import execute_kw


def get_existencias():
    result = execute_kw("stock.quant", "existencias_agencia")

    # Normalizar: cambiar None por string vacío o por valores seguros
    for r in result:
        r["nombreProducto"] = r.get("nombreProducto") or ""
        r["sku"] = r.get("sku") or ""
        r["codigoBodega"] = r.get("codigoBodega") or ""
        r["Bodega"] = r.get("Bodega") or ""
        r["cantidad"] = r.get("cantidad") or 0.0
        r["reserved_quantity"] = r.get("reserved_quantity") or 0.0

    return result
