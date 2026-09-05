html_files = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BookNook | Stories that stay with you</title>
    <meta name="description" content="Discover thoughtfully selected books, inspiring reads, and beautiful stationery.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main>
      <section class="hero-section">
        <div class="container hero-split fade-in">
          <div class="hero-content">
            <span class="hero-label">Your next great read awaits</span>
            <h1 class="hero-title">Stories that stay with you.</h1>
            <p class="hero-desc">Discover thoughtfully selected books, inspiring reads, and beautiful stationery for curious minds. Welcome to your new favorite independent bookstore.</p>
            <div class="flex gap-4">
              <a href="shop.html?category=books" class="btn btn-primary">Explore Books</a>
              <a href="shop.html?category=stationery" class="btn btn-outline">Shop Stationery</a>
            </div>
          </div>
        </div>
      </section>
      
      <section class="trust-section">
        <div class="container trust-grid">
          <div class="trust-item"><div class="trust-icon"><i data-lucide="truck"></i></div><h4>Free Shipping</h4><p>On orders above ₹999</p></div>
          <div class="trust-item"><div class="trust-icon"><i data-lucide="book-open"></i></div><h4>Curated Collection</h4><p>Chosen for curious readers</p></div>
          <div class="trust-item"><div class="trust-icon"><i data-lucide="shield-check"></i></div><h4>Secure Checkout</h4><p>Safe shopping experience</p></div>
          <div class="trust-item"><div class="trust-icon"><i data-lucide="refresh-cw"></i></div><h4>Easy Returns</h4><p>Simple 14-day policy</p></div>
        </div>
      </section>
      
      <section class="bestsellers" style="padding: 60px 0;">
        <div class="container">
          <h2 style="margin-bottom: 32px; font-family: 'Playfair Display', serif; font-size: 2rem;">Featured Bestsellers</h2>
          <div id="bestsellers-grid" class="products-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 32px;"></div>
        </div>
      </section>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const bestsellersContainer = document.getElementById('bestsellers-grid');
        const featured = getFeaturedProducts().slice(0, 8);
        if (bestsellersContainer) {
          bestsellersContainer.innerHTML = featured.map(createProductCard).join('');
          lucide.createIcons();
        }
      });
    </script>
</body>
</html>''',
    
    'shop.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shop | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 40px 0;">
      <div style="display: flex; gap: 32px;">
        <aside style="width: 250px;">
           <h3 style="margin-bottom:16px;">Categories</h3>
           <!-- basic filter UI placeholder -->
           <ul style="list-style:none; padding:0;">
             <li style="margin-bottom:8px;"><a href="?category=books">Books</a></li>
             <li style="margin-bottom:8px;"><a href="?category=stationery">Stationery</a></li>
           </ul>
        </aside>
        <div style="flex:1;">
           <h1 style="margin-bottom:16px; font-family:'Playfair Display', serif;">Shop</h1>
           <div id="results-count" style="margin-bottom:24px; color:var(--muted);"></div>
           <div id="products-grid" class="products-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 32px;"></div>
           <div id="empty-state" style="display:none; text-align:center; padding: 40px;">No products found.</div>
        </div>
      </div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      let currentProducts = [...products];
      
      const renderGrid = () => {
        const grid = document.getElementById('products-grid');
        const empty = document.getElementById('empty-state');
        const count = document.getElementById('results-count');
        
        if (currentProducts.length === 0) {
          grid.style.display = 'none';
          empty.style.display = 'block';
          count.textContent = '0 results';
        } else {
          grid.style.display = 'grid';
          empty.style.display = 'none';
          grid.innerHTML = currentProducts.map(createProductCard).join('');
          count.textContent = `Showing ${currentProducts.length} product${currentProducts.length > 1 ? 's' : ''}`;
        }
        lucide.createIcons();
      };
      document.addEventListener('DOMContentLoaded', renderGrid);
    </script>
</body>
</html>''',

    'product.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0;">
      <div id="product-container" style="display:flex; gap: 40px;">
        <!-- Hydrated by JS -->
      </div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      let currentProduct = null;
      let qty = 1;
      
      const updateQty = (change) => {
        qty = Math.max(1, qty + change);
        document.getElementById('qty-input').value = qty;
      };
      
      const doAddToCart = () => {
        addToCart(currentProduct.id, qty);
      };
      
      document.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const productId = urlParams.get('id') || 'b1'; // default to b1 if none provided
        
        currentProduct = getProductById(productId);
        const container = document.getElementById('product-container');
        
        if (!currentProduct) {
           container.innerHTML = '<p>Product not found.</p>';
           return;
        }
        
        container.innerHTML = `
          <div style="flex:1;">
            <img src="${currentProduct.image}" style="width:100%; border-radius:8px;" alt="${currentProduct.title}">
          </div>
          <div style="flex:1;">
            <h1 style="font-family:'Playfair Display',serif;">${currentProduct.title}</h1>
            <p style="color:var(--muted); font-size:1.2rem; margin-bottom:16px;">${currentProduct.author}</p>
            <h2 style="margin-bottom:24px;">₹${currentProduct.price}</h2>
            <p style="line-height:1.6; margin-bottom:24px;">${currentProduct.description || 'A wonderful read.'}</p>
            <div style="display:flex; gap:16px; margin-bottom:24px; align-items:center;">
              <button onclick="updateQty(-1)" class="btn btn-outline" style="padding:8px 16px;">-</button>
              <input id="qty-input" type="text" value="1" readonly style="width:40px; text-align:center; border:none;">
              <button onclick="updateQty(1)" class="btn btn-outline" style="padding:8px 16px;">+</button>
            </div>
            <button class="btn btn-primary" onclick="doAddToCart()" style="width:100%; padding:16px;">Add to Cart</button>
          </div>
        `;
        lucide.createIcons();
      });
    </script>
</body>
</html>''',

    'cart.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px;">Shopping Cart</h1>
      <div id="empty-cart" style="display:none; text-align:center; padding: 40px;">
         <p>Your cart is empty.</p>
         <a href="shop.html" class="btn btn-primary" style="margin-top:16px;">Continue Shopping</a>
      </div>
      <div id="cart-content" style="display:flex; gap:40px;">
         <div id="cart-items-container" style="flex:2; display:flex; flex-direction:column; gap:24px;"></div>
         <div style="flex:1; background:var(--cream); padding:24px; border-radius:8px; height:fit-content;">
            <h3>Order Summary</h3>
            <div id="cart-total" style="font-size:1.5rem; font-weight:600; margin:24px 0;"></div>
            <a href="checkout.html" class="btn btn-primary" style="display:block; text-align:center;">Proceed to Checkout</a>
         </div>
      </div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      const updateItemQty = (id, change) => {
        const cart = storage.get('cart', []);
        const item = cart.find(i => i.id === id);
        if(item) {
          item.quantity = Math.max(1, item.quantity + change);
          storage.set('cart', cart);
          renderCart();
          updateBadges();
        }
      };
      
      const removeItem = (id) => {
        let cart = storage.get('cart', []);
        cart = cart.filter(i => i.id !== id);
        storage.set('cart', cart);
        renderCart();
        updateBadges();
      };
      
      const renderCart = () => {
        const cart = storage.get('cart', []);
        const container = document.getElementById('cart-items-container');
        const emptyState = document.getElementById('empty-cart');
        const cartContent = document.getElementById('cart-content');
        
        if (cart.length === 0) {
          emptyState.style.display = 'block';
          cartContent.style.display = 'none';
          return;
        }
        
        emptyState.style.display = 'none';
        cartContent.style.display = 'flex';
        
        let subtotal = 0;
        let totalItems = 0;
        
        container.innerHTML = cart.map(item => {
          const product = getProductById(item.id);
          subtotal += product.price * item.quantity;
          return `
            <div style="display:flex; gap:16px; align-items:center; border-bottom:1px solid var(--border); padding-bottom:16px;">
              <img src="${product.image}" style="width:80px; height:80px; object-fit:cover; border-radius:4px;">
              <div style="flex:1;">
                <h4 style="margin:0;">${product.title}</h4>
                <p style="margin:0; color:var(--muted);">₹${product.price}</p>
              </div>
              <div style="display:flex; gap:8px; align-items:center;">
                 <button onclick="updateItemQty('${product.id}', -1)" class="btn btn-outline" style="padding:4px 8px;">-</button>
                 <span>${item.quantity}</span>
                 <button onclick="updateItemQty('${product.id}', 1)" class="btn btn-outline" style="padding:4px 8px;">+</button>
              </div>
              <button onclick="removeItem('${product.id}')" class="btn btn-outline" style="color:red; border:none;"><i data-lucide="trash-2"></i></button>
            </div>
          `;
        }).join('');
        
        document.getElementById('cart-total').textContent = `Total: ₹${subtotal}`;
        lucide.createIcons();
      };
      document.addEventListener('DOMContentLoaded', renderCart);
    </script>
</body>
</html>''',

    'checkout.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px;">Checkout</h1>
      <div style="display:flex; gap:40px;">
        <div style="flex:2;">
           <form id="checkout-form" onsubmit="event.preventDefault(); placeOrder();">
             <h3 style="margin-bottom:16px;">Shipping Details</h3>
             <input type="text" placeholder="Full Name" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
             <input type="text" placeholder="Address" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
             <input type="text" placeholder="City" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
             <button class="btn btn-primary" type="submit" style="width:100%;">Place Order</button>
           </form>
        </div>
        <div style="flex:1; background:var(--cream); padding:24px; border-radius:8px;" id="checkout-summary">
           <!-- Hydrated by JS -->
        </div>
      </div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      let cartItems = [];
      let totalAmount = 0;
      
      const renderCheckoutSummary = () => {
        cartItems = storage.get('cart', []);
        if (cartItems.length === 0) {
          window.location.href = 'cart.html';
          return;
        }
        
        let subtotal = 0;
        const itemsHtml = cartItems.map(item => {
          const p = getProductById(item.id);
          subtotal += p.price * item.quantity;
          return `
            <div class="order-item" style="display:flex; gap:12px; margin-bottom:12px; align-items:center;">
              <img src="${p.image}" class="order-item-img" style="width:50px; height:50px; border-radius:4px;">
              <div class="order-item-info">
                <div style="font-weight: 500; font-size:0.9rem;">${p.title}</div>
                <div style="color: var(--muted); font-size: 0.8rem;">Qty: ${item.quantity}</div>
              </div>
            </div>
          `;
        }).join('');
        
        document.getElementById('checkout-summary').innerHTML = `
          <h3 style="margin-bottom:16px;">Order Summary</h3>
          ${itemsHtml}
          <div style="margin-top:24px; font-weight:bold; font-size:1.2rem;">Total: ₹${subtotal}</div>
        `;
      };
      
      const placeOrder = () => {
        const orders = storage.get('orders', []);
        orders.push({ id: Math.floor(Math.random()*10000), date: new Date().toISOString(), items: cartItems });
        storage.set('orders', orders);
        storage.set('cart', []);
        showToast('Order placed successfully!', 'success');
        setTimeout(() => window.location.href = 'account.html', 1500);
      };
      
      document.addEventListener('DOMContentLoaded', renderCheckoutSummary);
    </script>
</body>
</html>''',

    'account.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Account | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px;">My Account</h1>
      
      <div style="display:flex; gap:24px; margin-bottom:40px;">
         <div style="background:var(--cream); padding:24px; border-radius:8px; flex:1; text-align:center;">
            <h2 id="stat-orders" style="font-size:2rem; margin-bottom:8px;">0</h2>
            <p style="color:var(--muted);">Total Orders</p>
         </div>
         <div style="background:var(--cream); padding:24px; border-radius:8px; flex:1; text-align:center;">
            <h2 id="stat-wishlist" style="font-size:2rem; margin-bottom:8px;">0</h2>
            <p style="color:var(--muted);">Wishlist Items</p>
         </div>
      </div>
      
      <h3>Order History</h3>
      <div id="no-orders" style="display:none; color:var(--muted); margin-top:16px;">You haven't placed any orders yet.</div>
      <div class="orders-table-wrap" style="margin-top:16px;">
         <table style="width:100%; border-collapse:collapse;">
           <thead>
             <tr style="border-bottom:1px solid var(--border); text-align:left;">
               <th style="padding:12px 0;">Order ID</th>
               <th>Date</th>
               <th>Status</th>
             </tr>
           </thead>
           <tbody id="orders-tbody">
           </tbody>
         </table>
      </div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const orders = storage.get('orders', []);
        const wishlist = storage.get('wishlist', []);
        
        document.getElementById('stat-orders').textContent = orders.length;
        document.getElementById('stat-wishlist').textContent = wishlist.length;
        
        if (orders.length === 0) {
          document.querySelector('.orders-table-wrap').style.display = 'none';
          document.getElementById('no-orders').style.display = 'block';
        } else {
          document.getElementById('orders-tbody').innerHTML = orders.map(o => {
            return `
              <tr style="border-bottom:1px solid var(--border);">
                 <td style="padding:12px 0;">#${o.id}</td>
                 <td>${new Date(o.date).toLocaleDateString()}</td>
                 <td style="color:green;">Processing</td>
              </tr>
            `;
          }).join('');
        }
      });
    </script>
</body>
</html>''',

    'wishlist.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wishlist | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px;">My Wishlist</h1>
      <div id="empty-wishlist" style="display:none; text-align:center; padding: 40px;">Your wishlist is empty.</div>
      <div id="wishlist-grid" class="products-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 32px;"></div>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      const renderWishlist = () => {
        const wishlist = storage.get('wishlist', []);
        const grid = document.getElementById('wishlist-grid');
        const empty = document.getElementById('empty-wishlist');
        
        if (wishlist.length === 0) {
          empty.style.display = 'block';
          grid.style.display = 'none';
        } else {
          empty.style.display = 'none';
          grid.style.display = 'grid';
          
          const itemsHtml = wishlist.map(id => {
            const product = getProductById(id);
            if (!product) return '';
            return createProductCard(product);
          }).join('');
          
          grid.innerHTML = itemsHtml;
          lucide.createIcons();
        }
      };
      document.addEventListener('DOMContentLoaded', renderWishlist);
    </script>
</body>
</html>''',

    'login.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0; max-width:400px; margin: 0 auto;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px; text-align:center;">Login</h1>
      <form onsubmit="handleLogin(event)">
        <input type="email" placeholder="Email" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <input type="password" placeholder="Password" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <button class="btn btn-primary" type="submit" style="width:100%;">Sign In</button>
        <p style="text-align:center; margin-top:16px; color:var(--muted);">Don't have an account? <a href="register.html">Register</a></p>
      </form>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      const handleLogin = (e) => {
        e.preventDefault();
        showToast('Login successful! Redirecting...', 'success');
        setTimeout(() => {
          window.location.href = 'account.html';
        }, 1500);
      };
    </script>
</body>
</html>''',

    'register.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0; max-width:400px; margin: 0 auto;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:32px; text-align:center;">Register</h1>
      <form onsubmit="handleRegister(event)">
        <input type="text" placeholder="Full Name" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <input type="email" placeholder="Email" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <input type="password" id="password" placeholder="Password" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <input type="password" id="confirm-password" placeholder="Confirm Password" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <button class="btn btn-primary" type="submit" style="width:100%;">Create Account</button>
        <p style="text-align:center; margin-top:16px; color:var(--muted);">Already have an account? <a href="login.html">Login</a></p>
      </form>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
    <script>
      const handleRegister = (e) => {
        e.preventDefault();
        const pwd = document.getElementById('password').value;
        const confirm = document.getElementById('confirm-password').value;
        
        if (pwd !== confirm) {
          showToast('Passwords do not match', 'error');
          return;
        }
        
        showToast('Account created successfully! Redirecting...', 'success');
        setTimeout(() => {
          window.location.href = 'account.html';
        }, 1500);
      };
    </script>
</body>
</html>''',

    'contact.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0; max-width:600px; margin: 0 auto;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:16px; text-align:center;">Contact Us</h1>
      <p style="text-align:center; color:var(--muted); margin-bottom:40px;">We'd love to hear from you. Send us a message.</p>
      <form onsubmit="event.preventDefault(); showToast('Message sent successfully!'); this.reset();">
        <input type="text" placeholder="Your Name" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <input type="email" placeholder="Your Email" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px;">
        <textarea rows="5" placeholder="Your Message" required style="width:100%; padding:12px; margin-bottom:16px; border:1px solid var(--border); border-radius:4px; resize:vertical;"></textarea>
        <button class="btn btn-primary" type="submit" style="width:100%;">Send Message</button>
      </form>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
</body>
</html>''',

    'about.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | BookNook</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <div id="layout-header"></div>
    <main class="container" style="padding: 60px 0; max-width:800px; margin: 0 auto; line-height:1.8;">
      <h1 style="font-family:'Playfair Display',serif; margin-bottom:24px; text-align:center;">Our Story</h1>
      <img src="https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&q=80&w=1000" style="width:100%; border-radius:8px; margin-bottom:32px;" alt="Library">
      <p>Welcome to BookNook, your independent haven for carefully curated literature and fine stationery. We believe that a good book is a companion for life.</p>
      <p>Founded in 2026, our mission is to create a digital sanctuary where book lovers can discover new stories and find the perfect tools to write their own.</p>
    </main>
    <div id="layout-footer"></div>
    <div id="toast-container" class="toast-container"></div>
    <script src="js/data.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''
}

for filename, content in html_files.items():
    with open(filename, 'w') as f:
        f.write(content)
