function addToCart(productId) {
    fetch("/add_to_cart", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: productId })
    }).then(() => {
        alert("Товар добавлен в корзину!");
    });
}

function changeTheme() {
    const theme = document.getElementById("theme").value;
    fetch("/settings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ theme: theme })
    }).then(() => {
        document.body.className = theme;
    });
}
