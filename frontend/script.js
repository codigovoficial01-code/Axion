// ====== TEMA ======
function toggleTheme() {
  const body = document.body;
  const btn = document.querySelector(".theme-toggle");

  const theme = body.getAttribute("data-theme") === "dark" ? "light" : "dark";
  body.setAttribute("data-theme", theme);

  btn.textContent = theme === "dark" ? "🌙" : "🌞";
  localStorage.setItem("axion-theme", theme);
}

(function initTheme() {
  const saved = localStorage.getItem("axion-theme") || "dark";
  document.body.setAttribute("data-theme", saved);
  document.querySelector(".theme-toggle").textContent =
    saved === "dark" ? "🌙" : "🌞";
})();

// ====== VENDAS ======
function openSaleForm() {
  saleModal.style.display = "flex";
}

function closeSaleForm() {
  saleModal.style.display = "none";
}

async function submitSale() {
  const data = {
    product: product.value,
    category: category.value,
    revenue: revenue.value,
    quantity: quantity.value
  };

  await fetch("/sales/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  closeSaleForm();
  loadSales();
}

async function loadSales() {
  const res = await fetch("/sales/");
  const data = await res.json();
  output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

async function generateDecisions() {
  const res = await fetch("/sales/decisions");
  const data = await res.json();

  output.innerHTML = `
    <h3>Total faturado: R$ ${data.total_sales.toFixed(2)}</h3>
    <p>${data.decision}</p>
  `;
}

async function resetDatabase() {
  if (!confirm("Apagar TODAS as vendas?")) return;

  const res = await fetch("/dev/reset-database", { method: "DELETE" });
  const data = await res.json();
  output.innerHTML = `<b>${data.status}</b>`;
}
