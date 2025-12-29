const API_URL = "http://127.0.0.1:8000";

function openSaleForm() {
  const sale = {
    product_name: "Produto Teste",
    category: "Categoria A",
    revenue: 150,
    quantity: 1
  };

  fetch(`${API_URL}/sales/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(sale)
  })
  .then(res => res.json())
  .then(data => {
    alert("Venda inserida com sucesso!");
    console.log(data);
  })
  .catch(err => alert("Erro ao inserir venda"));
}

function loadSales() {
  fetch(`${API_URL}/sales/`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerText =
        "📊 Vendas cadastradas:\n\n" + JSON.stringify(data, null, 2);
    });
}

function generateDecisions() {
  fetch(`${API_URL}/analysis/weekly-decisions`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerText =
        "💡 Decisões do AXION:\n\n" + JSON.stringify(data, null, 2);
    });
}
