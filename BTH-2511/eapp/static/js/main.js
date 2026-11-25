function addToCart(id, name, price){
    fetch('api/carts', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': name,
            'price': price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        let carts = document.getElementsByClassName('cart-counter');
        for(let c of carts)
            c.innerText = data.total_quantity;
    })
}


