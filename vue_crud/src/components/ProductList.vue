<template>
  <div class="list row">
    <!-- <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title"
          v-model="title"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchTitle"
          >
            Search
          </button>
        </div>
      </div>
    </div> -->
    <div class="col-md-6">
      <h4>Products List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(product, index) in products"
          :key="index"
          @click="setActiveProduct(product, index)"
        >
          {{ product.name }}
        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllProducts">
        Remove All
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentProduct">
        <h4>Product</h4>
        <div>
          <label><strong>name:</strong></label> {{ currentProduct.name }}
        </div>
        <div>
          <label><strong>price:</strong></label> {{ currentProduct.price }}
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentProduct.description }}
        </div>
    

        <router-link :to="'/products/' + currentProduct.id" class="badge badge-warning">Edit</router-link>
      </div>
      <div v-else>
        <br />
        <p>Please click on a Product...</p>
      </div>
    </div>
  </div>
</template>

<script>
import ProductDataService from "../services/ProductDataService";

export default {
  name: "products-list",
  data() {
    return {
      products: [],
      currentProduct: null,
      currentIndex: -1,
      name: ""
    };
  },
  methods: {
    retrieveProducts() {
      ProductDataService.getAll()
        .then(response => {
          this.products = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveProducts();
      this.currentProduct = null;
      this.currentIndex = -1;
    },

    setActiveProduct(product, index) {
      this.currentProduct = product;
      this.currentIndex = product ? index : -1;
    },

    removeAllProducts() {
      ProductDataService.deleteAll()
        .then(response => {
          console.log(response.data);
          this.refreshList();
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  mounted() {
    this.retrieveProducts();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>