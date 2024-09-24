<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <b-nav>
      <b-nav-item><router-link to="/">Porcinos</router-link></b-nav-item>
      <b-nav-item><router-link to="/clientes">Clientes</router-link></b-nav-item>
      <b-nav-item><router-link to="/alimentaciones">Alimentacion</router-link></b-nav-item>
    </b-nav>
    <RouterView />
  </header>
</template>

<style></style>
