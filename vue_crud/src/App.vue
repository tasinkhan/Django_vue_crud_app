<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">Shop</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/products" class="nav-link">Products</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/add" class="nav-link">Add Product</router-link>
        </li>
      </div>
    </nav>

    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>