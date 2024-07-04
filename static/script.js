document.addEventListener("DOMContentLoaded", function() {
    const foodItems = document.querySelectorAll('.food-item');
    const cartItems = document.getElementById('cart-items');
    const totalPrice = document.getElementById('total-price');
    const checkoutBtn = document.getElementById('checkout-btn');
  
    let cart = [];
  
    foodItems.forEach(item => {
      const addToCartBtn = item.querySelector('.add-to-cart-btn');
      const quantityValue = item.querySelector('.quantity-value');
      const increaseBtn = item.querySelector('.increase-btn');
      const decreaseBtn = item.querySelector('.decrease-btn');
      const itemName = item.dataset.name;
      const itemPrice = parseFloat(item.dataset.price);
  
      addToCartBtn.addEventListener('click', () => {
        const quantity = parseInt(quantityValue.textContent);
        if (quantity > 0) {
          const existingItem = cart.find(cartItem => cartItem.name === itemName);
          if (existingItem) {
            existingItem.quantity += quantity;
          } else {
            cart.push({ name: itemName, price: itemPrice, quantity });
          }
          updateCartUI();
        }
      });
  
      increaseBtn.addEventListener('click', () => {
        let quantity = parseInt(quantityValue.textContent);
        quantity++;
        quantityValue.textContent = quantity;
      });
  
      decreaseBtn.addEventListener('click', () => {
        let quantity = parseInt(quantityValue.textContent);
        if (quantity > 0) {
          quantity--;
          quantityValue.textContent = quantity;
        }
      });
    });
  
    function updateCartUI() {
      cartItems.innerHTML = '';
      let total = 0;
      cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} x ${item.quantity} - $${(item.price * item.quantity).toFixed(2)}`;
        cartItems.appendChild(li);
        total += item.price * item.quantity;
      });
      totalPrice.textContent = total.toFixed(2);
    }
  
    checkoutBtn.addEventListener('click', () => {
      // Implement your checkout logic here
      alert('Checkout clicked!');
    });
  });
  