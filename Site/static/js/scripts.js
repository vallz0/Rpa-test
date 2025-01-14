document.getElementById("productForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const product = {
      code: document.getElementById("code").value,
      brand: document.getElementById("brand").value,
      type: document.getElementById("type").value,
      category: document.getElementById("category").value,
      price: parseFloat(document.getElementById("price").value),
      cost: parseFloat(document.getElementById("cost").value),
      notes: document.getElementById("notes").value,
    };
  
    // Envia o produto para o backend
    const response = await fetch("/api/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product),
    });
  
    if (response.ok) {
      alert("Produto cadastrado com sucesso!");
      fetchProducts();
    }
  });
  
  // Busca e exibe produtos cadastrados
  async function fetchProducts() {
    const response = await fetch("/api/products");
    const products = await response.json();
  
    const productList = document.getElementById("productList");
    productList.innerHTML = "<h2>Produtos Cadastrados</h2>";
  
    products.forEach((product) => {
      const div = document.createElement("div");
      div.className = "product";
      div.innerHTML = `
        <strong>Código:</strong> ${product.code}<br>
        <strong>Marca:</strong> ${product.brand}<br>
        <strong>Tipo:</strong> ${product.type}<br>
        <strong>Categoria:</strong> ${product.category}<br>
        <strong>Preço:</strong> R$ ${product.price.toFixed(2)}<br>
        <strong>Custo:</strong> R$ ${product.cost.toFixed(2)}<br>
        <strong>Observações:</strong> ${product.notes || "N/A"}
      `;
      productList.appendChild(div);
    });
  }
  
  // Carrega os produtos ao iniciar
  fetchProducts();
document.getElementById("clearButton").addEventListener("click", async () => {
  if (confirm("Tem certeza de que deseja remover todos os produtos?")) {
    const response = await fetch("/api/products", { method: "DELETE" });
    if (response.ok) {
      alert("Todos os produtos foram removidos!");
      fetchProducts(); // Atualiza a lista para exibir vazio
    } else {
      alert("Erro ao tentar limpar os produtos.");
    }
  }
});
    