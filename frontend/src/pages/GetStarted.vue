<template>
  <div class="d-flex flex-column min-vh-100 bg-light text-center px-3">
    <main class="flex-grow-1 d-flex flex-column justify-content-center align-items-center">
      <h1 class="mb-3 display-5 fw-bold text-dark">Selamat Datang di Aplikasi</h1>
      <p class="mb-4 fs-5 text-dark bg-opacity-25 px-3 py-2 rounded-3 shadow-sm">
        Tugas Pengembangan Aplikasi Backend
      </p>
      <button class="btn btn-start btn-lg fw-semibold px-5 py-2 mt-2" @click="goToLogin">
        🚀 Mulai Sekarang
      </button>
    </main>

    <footer class="py-3 text-muted small text-center">
      <hr class="my-3" />
      <p class="mb-1">5220411181 - Agus Purwanto</p>
      <p class="mb-0">5220411184 - Ariyo Aziz Pratama</p>
    </footer>
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
