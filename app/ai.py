from typing import List, Dict

def generate_sales_insights(sales: List[Dict]) -> Dict:
    if not sales:
        return {
            "summary": "Nenhuma venda registrada ainda.",
            "top_products": [],
            "decisions": ["Comece registrando suas vendas para gerar insights."]
        }

    total_revenue = sum(s["revenue"] for s in sales)
    category_revenue = {}
    product_sales = {}

    for sale in sales:
        category_revenue[sale["category"]] = category_revenue.get(sale["category"], 0) + sale["revenue"]
        product_sales[sale["product_name"]] = product_sales.get(sale["product_name"], 0) + sale["quantity"]

    top_category = max(category_revenue, key=category_revenue.get)
    top_products = sorted(product_sales, key=product_sales.get, reverse=True)[:3]

    decisions = [
        f"Aumentar investimento na categoria {top_category}",
        "Criar promoções para produtos com menor giro",
        f"Priorizar anúncios dos produtos: {', '.join(top_products)}"
    ]

    return {
        "summary": f"A categoria {top_category} representa a maior parte da receita.",
        "top_products": top_products,
        "decisions": decisions
    }
