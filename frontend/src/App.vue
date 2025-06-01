
<script setup>


</script>

<template>
  <router-view />
</template>

<style>
/* Global styles tanpa scoped agar berlaku di body dan html */
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
}

#app {
  height: 100vh;  /* viewport height */
  display: flex;
  justify-content: center; /* horizontal center */
  align-items: center;     /* vertical center */
  overflow: hidden;        /* hilangkan scroll */
  background-color: #f8f9fa;
}

</style>
