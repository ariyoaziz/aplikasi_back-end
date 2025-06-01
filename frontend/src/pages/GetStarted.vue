<template>
  <div class="d-flex flex-column align-items-center justify-content-center min-vh-100 text-center px-3">
    <h1 class="mb-3 display-5 fw-bold text-drak">Selamat Datang di Aplikasi</h1>
    <p class="mb-4 fs-5 text-drak  bg-opacity-25 px-3 py-2 rounded-3 shadow-sm">
      Tugas Pengembangan Aplikasi Backend
    </p>
     <button class="btn btn-start btn-lg fw-semibold  px-5 py-2 mt-2" @click="goToLogin">
    🚀 Mulai Sekarang
  </button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToLogin = () => {
  router.push('/login')
}
</script>

<style scoped>
.btn-start {
  background-color: #0d6efd; /* biru bootstrap */
  color: white;
  border: none;
  border-radius: 12px;
  transition: all 0.3s ease-in-out;
  box-shadow: 0 4px 12px rgba(13, 110, 253, 0.4);
}

.btn-start:hover {
  background-color: #0b5ed7;
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(13, 110, 253, 0.6);
}
</style>
