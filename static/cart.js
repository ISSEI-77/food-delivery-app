const cartItemsContainer = document.getElementById('cart-items');
const cartTotal = document.getElementById('cart-total');

let cart = [];

function updateCartUI() {
  cartItemsContainer.innerHTML = '';
  let total = 0;
  cart.forEach(item => {
    const itemElement = document.createElement('div');
    itemElement.classList.add('cart-item');
    itemElement.innerHTML = `
      <img src="${item.image}" alt="${item.name}">
      <div class="item-details">
        <span>${item.name}</span>
        <span>${item.price}</span>
      </div>
      <div class="quantity">
        <button onclick="decreaseQuantity(${item.id})">-</button>
        <span>${item.quantity}</span>
        <button onclick="increaseQuantity(${item.id})">+</button>
      </div>
      <button onclick="removeItem(${item.id})">Remove</button>
    `;
    cartItemsContainer.appendChild(itemElement);
    total += item.price * item.quantity;
  });
  cartTotal.textContent = `$${total.toFixed(2)}`;
}

function addToCart(item) {
  const existingItem = cart.find(i => i.id === item.id);
  if (existingItem) {
    existingItem.quantity++;
  } else {
    cart.push({ ...item, quantity: 1 });
  }
  updateCartUI();
}

function removeItem(itemId) {
  cart = cart.filter(item => item.id !== itemId);
  updateCartUI();
}

function increaseQuantity(itemId) {
  const item = cart.find(i => i.id === itemId);
  if (item) {
    item.quantity++;
    updateCartUI();
  }
}

function decreaseQuantity(itemId) {
  const item = cart.find(i => i.id === itemId);
  if (item && item.quantity > 1) {
    item.quantity--;
    updateCartUI();
  }
}

// Sample usage
const sampleItems = [
  { id: 1, name: 'Item 1', price: 10.99, image: 'item1.jpg' },
  { id: 2, name: 'Item 2', price: 8.49, image: 'item2.jpg' },
  { id: 3, name: 'Item 3', price: 14.99, image: 'item3.jpg' }
];

sampleItems.forEach(item => addToCart(item));
