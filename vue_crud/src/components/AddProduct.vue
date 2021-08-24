<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="name">Name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="product.name"
          name="name"
        />
      </div>

      <div class="form-group">
        <label for="price">Price</label>
        <input
          class="form-control"
          id="price"
          required
          v-model="product.price"
          name="price"
        />
      </div>

      <div class="form-group">
        <label for="description">Description</label>
        <input
          class="form-control"
          id="description"
          required
          v-model="product.description"
          name="description"
        />
      </div>

      <button @click="saveProduct" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newProduct">Add</button>
    </div>
  </div>
</template>

<script>
import ProductDataService from "../services/ProductDataService";

export default {
  name: "add-product",
  data() {
    return {
      product: {
        id: null,
        title: "",
        description: "",
        price: '0',
      },
      submitted: false
    };
  },
  methods: {
    saveProduct() {
      var data = {
        name: this.product.name,
        price: this.product.price,
        description: this.product.description
      };


      ProductDataService.create(data)
        .then(response => {
          this.product.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newProduct() {
      this.submitted = false;
      this.product = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>