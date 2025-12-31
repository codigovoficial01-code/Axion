const API_URL = window.location.origin;

async function insertSale() {
  const sale = {
    product_name: product.value,
    category: category.value,
    revenue: Number(revenue.value),
    quantity: Number(quantity.value)
  };

  const res = await fetch(`${API_URL}/sales/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(sale)
  });

  if (res.ok) {
    alert("Venda inserida com sucesso!");
  } else {
    alert("Erro ao inserir venda");
  }
}

async function loadDecision() {
  const res = await fetch(`${API_URL}/analysis/weekly-decisions`);
  const data = await res.json();
  decision.innerText = data.decision;
}
