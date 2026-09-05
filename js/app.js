// Core Application State & UI logic

// --- Local Storage Wrappers ---
const storage = {
  get: (key, defaultValue = null) => {
    try {
      const item = localStorage.getItem(`booknook_${key}`);
      return item ? JSON.parse(item) : defaultValue;
    } catch (error) {
      console.warn(`Error reading ${key} from localStorage`, error);
      return defaultValue;
    }
  },
  set: (key, value) => {
    try {
      localStorage.setItem(`booknook_${key}`, JSON.stringify(value));
    } catch (error) {
      console.warn(`Error saving ${key} to localStorage`, error);
    }
  }
};

// --- Layout Injection ---
const injectLayout = () => {
  const headerHtml = `
    <header class="navbar">
      <div class="container nav-container">
        <a href="index.html" class="logo">BOOKNOOK</a>
        <nav class="nav-links desktop-nav">
          <a href="index.html">Home</a>
          <a href="shop.html?category=books">Books</a>
          <a href="shop.html?category=stationery">Stationery</a>
          <a href="about.html">About</a>
          <a href="contact.html">Contact</a>
        </nav>
        <div class="nav-actions">
          <button class="nav-icon-btn" aria-label="Search" onclick="toggleSearchModal()"><i data-lucide="search"></i></button>
          <a href="wishlist.html" class="nav-icon-btn" aria-label="Wishlist"><i data-lucide="heart"></i><span class="wishlist-badge" id="nav-wishlist-count">0</span></a>
          <a href="account.html" class="nav-icon-btn" aria-label="Account"><i data-lucide="user"></i></a>
          <a href="cart.html" class="nav-icon-btn" aria-label="Cart"><i data-lucide="shopping-bag"></i><span class="cart-badge" id="nav-cart-count">0</span></a>
          <button class="nav-icon-btn mobile-menu-trigger" aria-label="Menu" onclick="toggleMobileMenu()"><i data-lucide="menu"></i></button>
        </div>
      </div>
    </header>
    <div class="mobile-menu-overlay" onclick="toggleMobileMenu()"></div>
    <div class="mobile-menu">
      <div class="mobile-menu-header">
        <span class="logo">BOOKNOOK</span>
        <button class="nav-icon-btn" onclick="toggleMobileMenu()"><i data-lucide="x"></i></button>
      </div>
      <nav class="mobile-nav-links">
        <a href="index.html">Home</a>
        <a href="shop.html?category=books">Books</a>
        <a href="shop.html?category=stationery">Stationery</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
        <a href="account.html">My Account</a>
      </nav>
    </div>
    <!-- Search Modal -->
    <div id="search-modal" class="modal-container">
      <div class="modal-overlay" onclick="toggleSearchModal()"></div>
      <div class="modal-content" style="max-width: 600px; margin-top: 100px; padding: 32px;">
        <button class="btn-icon modal-close" onclick="toggleSearchModal()"><i data-lucide="x"></i></button>
        <h3 class="font-serif" style="font-size: 1.5rem; margin-bottom: 24px;">Search BookNook</h3>
        <form onsubmit="handleSearch(event)" style="display: flex; gap: 12px;">
          <input type="text" id="search-input" class="form-control" placeholder="Search for books, authors, stationery..." required>
          <button type="submit" class="btn btn-primary">Search</button>
        </form>
      </div>
    </div>
  `;

  const footerHtml = `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <h3>BOOKNOOK</h3>
            <p>Stories, knowledge & little things that inspire. An independent bookstore experience curated for curious minds.</p>
            <div class="footer-socials">
              <a href="#"><i data-lucide="instagram"></i></a>
              <a href="#"><i data-lucide="twitter"></i></a>
              <a href="#"><i data-lucide="facebook"></i></a>
            </div>
          </div>
          <div>
            <h4>Shop</h4>
            <ul class="footer-links">
              <li><a href="shop.html?category=books">All Books</a></li>
              <li><a href="shop.html?subcategory=fiction">Fiction</a></li>
              <li><a href="shop.html?subcategory=non-fiction">Non-Fiction</a></li>
              <li><a href="shop.html?subcategory=children">Children's</a></li>
              <li><a href="shop.html?category=stationery">Stationery</a></li>
            </ul>
          </div>
          <div>
            <h4>Help</h4>
            <ul class="footer-links">
              <li><a href="contact.html">Contact Us</a></li>
              <li><a href="#">Shipping Information</a></li>
              <li><a href="#">Returns & Exchanges</a></li>
              <li><a href="#">FAQs</a></li>
            </ul>
          </div>
          <div>
            <h4>Account</h4>
            <ul class="footer-links">
              <li><a href="account.html">My Account</a></li>
              <li><a href="wishlist.html">Wishlist</a></li>
              <li><a href="account.html">Order History</a></li>
              <li><a href="cart.html">Shopping Cart</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2026 BookNook. All rights reserved.</p>
          <p>Created for Web Development Internship.</p>
        </div>
      </div>
    </footer>
  `;

  const headerEl = document.getElementById('layout-header');
  if (headerEl) headerEl.innerHTML = headerHtml;

  const footerEl = document.getElementById('layout-footer');
  if (footerEl) footerEl.innerHTML = footerHtml;

  // Set active nav link
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.desktop-nav a').forEach(link => {
    if (link.getAttribute('href') === currentPath || 
       (currentPath === 'shop.html' && link.getAttribute('href').includes(window.location.search))) {
      link.classList.add('active');
    }
  });
};

// --- Mobile Menu & Search ---
window.toggleMobileMenu = () => {
  document.querySelector('.mobile-menu').classList.toggle('active');
  document.querySelector('.mobile-menu-overlay').classList.toggle('active');
};

window.toggleSearchModal = () => {
  const modal = document.getElementById('search-modal');
  modal.classList.toggle('active');
  if (modal.classList.contains('active')) {
    setTimeout(() => document.getElementById('search-input').focus(), 100);
  }
};

window.handleSearch = (e) => {
  e.preventDefault();
  const query = document.getElementById('search-input').value.trim();
  if (query) {
    window.location.href = `shop.html?q=${encodeURIComponent(query)}`;
  }
};

// --- Toast Notifications ---
const showToast = (message, type = 'success') => {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  
  const icon = type === 'success' ? 'check-circle' : 'alert-circle';
  
  toast.innerHTML = `
    <div class="toast-icon"><i data-lucide="${icon}"></i></div>
    <div class="toast-content">${message}</div>
  `;
  
  container.appendChild(toast);
  lucide.createIcons({ root: toast });
  
  // Trigger animation
  setTimeout(() => toast.classList.add('show'), 10);
  
  // Auto remove
  setTimeout(() => {
    toast.classList.remove('show');
    toast.classList.add('hiding');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
};

// --- Global State Updaters ---
const updateBadges = () => {
  const cart = storage.get('cart', []);
  const wishlist = storage.get('wishlist', []);
  
  const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
  const wishlistCount = wishlist.length;
  
  const cartBadge = document.getElementById('nav-cart-count');
  const wishlistBadge = document.getElementById('nav-wishlist-count');
  
  if (cartBadge) {
    cartBadge.textContent = cartCount;
    cartBadge.classList.add('badge-bump');
    setTimeout(() => cartBadge.classList.remove('badge-bump'), 200);
  }
  if (wishlistBadge) {
    wishlistBadge.textContent = wishlistCount;
    wishlistBadge.classList.add('badge-bump');
    setTimeout(() => wishlistBadge.classList.remove('badge-bump'), 200);
  }
};

// --- Cart Actions ---
window.addToCart = (productId, quantity = 1, silent = false) => {
  const cart = storage.get('cart', []);
  const product = products.find(p => p.id === productId);
  if (!product) return;
  
  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.quantity += quantity;
  } else {
    cart.push({ id: productId, quantity });
  }
  
  storage.set('cart', cart);
  updateBadges();
  
  if (!silent) {
    showToast(`<strong>${product.title}</strong> added to cart.`);
  }
};

// --- Wishlist Actions ---
window.toggleWishlist = (productId, event) => {
  if (event) {
    event.preventDefault();
    event.stopPropagation();
  }
  
  let wishlist = storage.get('wishlist', []);
  const product = products.find(p => p.id === productId);
  if (!product) return;
  
  const index = wishlist.indexOf(productId);
  if (index > -1) {
    wishlist.splice(index, 1);
    showToast(`<strong>${product.title}</strong> removed from wishlist.`);
    if(event) event.currentTarget.classList.remove('active');
  } else {
    wishlist.push(productId);
    showToast(`<strong>${product.title}</strong> added to wishlist.`);
    if(event) event.currentTarget.classList.add('active');
  }
  
  storage.set('wishlist', wishlist);
  updateBadges();
};

window.isInWishlist = (productId) => {
  const wishlist = storage.get('wishlist', []);
  return wishlist.includes(productId);
};

// --- Format Currency ---
const formatPrice = (price) => {
  return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(price);
};

// --- Generate Product Card ---
const createProductCard = (product) => {
  const isWished = isInWishlist(product.id);
  const discountHtml = product.discount ? `<div class="discount-badge">${product.discount}% OFF</div>` : '';
  const origPriceHtml = product.originalPrice ? `<span class="original-price">${formatPrice(product.originalPrice)}</span>` : '';
  
  return `
    <div class="product-card fade-in">
      ${discountHtml}
      <button class="btn-icon wishlist-btn ${isWished ? 'active' : ''}" onclick="toggleWishlist('${product.id}', event)" aria-label="Toggle Wishlist">
        <i data-lucide="heart"></i>
      </button>
      <div class="product-image-container" onclick="window.location.href='product.html?id=${product.id}'">
        <img src="${product.image}" alt="${product.title}" class="product-image" loading="lazy">
      </div>
      <div class="product-info">
        <div class="product-category">${product.category} &bull; ${product.subcategory}</div>
        <h3 class="product-title"><a href="product.html?id=${product.id}">${product.title}</a></h3>
        <div class="product-author">${product.author}</div>
        <div class="product-rating">
          <i data-lucide="star" class="fill-current"></i> ${product.rating} <span>(${product.reviews})</span>
        </div>
        <div class="product-price-row">
          <div class="price-wrap">
            <span class="price">${formatPrice(product.price)}</span>
            ${origPriceHtml}
          </div>
          <button class="btn btn-primary btn-add-cart" onclick="addToCart('${product.id}')">Add</button>
        </div>
      </div>
    </div>
  `;
};

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
  injectLayout();
  lucide.createIcons();
  updateBadges();
});
