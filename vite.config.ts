import { viteStaticCopy } from 'vite-plugin-static-copy';
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'js',
          dest: '',
        },
      ],
    }),
  ],

  resolve: {
    alias: {
      '@': path.resolve(__dirname, '.'),
    },
  },

  build: {
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'index.html'),
        shop: path.resolve(__dirname, 'shop.html'),
        about: path.resolve(__dirname, 'about.html'),
        account: path.resolve(__dirname, 'account.html'),
        cart: path.resolve(__dirname, 'cart.html'),
        checkout: path.resolve(__dirname, 'checkout.html'),
        contact: path.resolve(__dirname, 'contact.html'),
        login: path.resolve(__dirname, 'login.html'),
        product: path.resolve(__dirname, 'product.html'),
        register: path.resolve(__dirname, 'register.html'),
        wishlist: path.resolve(__dirname, 'wishlist.html'),
      },
    },
  },

  server: {
    hmr: process.env.DISABLE_HMR !== 'true',
    watch: process.env.DISABLE_HMR === 'true' ? null : {},
  },
});