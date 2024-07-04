<script>
  document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            // Get the restaurant name or any unique identifier
            const restaurantName = this.previousElementSibling.textContent.trim();
            // Get the quantity
            const quantity = parseInt(this.nextElementSibling.querySelector('input').value);
            // You can perform further actions like adding to cart or updating UI here
            console.log(`Added ${quantity} of ${restaurantName} to cart`);
        }
        );
    }
    );

  document.querySelectorAll('.plus').forEach(button => {
        button.addEventListener('click', function () {
            const input = this.parentNode.querySelector('input');
            input.value = parseInt(input.value) + 1;
        });
  });

  document.querySelectorAll('.minus').forEach(button => {
        button.addEventListener('click', function () {
            const input = this.parentNode.querySelector('input');
            if (parseInt(input.value) > 1) {
                input.value = parseInt(input.value) - 1;
            }
        });
  });
</script>
