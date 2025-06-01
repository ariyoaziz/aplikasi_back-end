<template>
  <div class="login-wrapper d-flex align-items-center justify-content-center">
    <div class="card-content text-center p-4 p-md-5 shadow-lg rounded-4 bg-white">
      <h1 class="mb-3 fw-bold text-primary">Login</h1>
      <form @submit.prevent="handleLogin" class="w-100" style="max-width: 400px; margin: 0 auto;">
        <div class="mb-3 text-start">
          <label for="email" class="form-label fw-semibold">Email</label>
          <input
            v-model="email"
            type="email"
            id="email"
            class="form-control"
            placeholder="Masukkan email"
            required
          />
        </div>
        <div class="mb-3 text-start">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            class="form-control"
            placeholder="Masukkan password"
            required
          />
        </div>
        <button type="submit" class="btn btn-primary btn-lg w-100 fw-semibold">
          Login
        </button>
      </form>
      <p class="mt-3 text-muted">
        Belum punya akun?
        <router-link to="/" class="text-decoration-none">Kembali ke Mulai</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"

const email = ref("")
const password = ref("")
const router = useRouter()

const handleLogin = () => {
  if (email.value && password.value) {
    alert(`Login berhasil dengan email: ${email.value}`)
    router.push("/dashboard")
  } else {
    alert("Email dan password wajib diisi")
  }
}
</script>

<style scoped>
.login-wrapper {
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #74ebd5, #acb6e5);
  padding: 2rem;
  display: flex;
}

.card-content {
  max-width: 480px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: transform 0.3s ease;
}

.card-content:hover {
  transform: scale(1.02);
}
</style>
