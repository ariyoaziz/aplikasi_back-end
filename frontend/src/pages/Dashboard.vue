<template>
  <div class="dashboard-wrapper container py-5">
    <!-- HEADER -->
    <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap">
      <div>
        <h1 class="display-5 fw-bold text-primary mb-1">🎓 Dashboard Mahasiswa</h1>
        <p class="text-secondary fs-6 mb-0">Kelola data mahasiswa dengan mudah dan cepat.</p>
      </div>
      <button
        class="btn btn-outline-danger d-flex align-items-center gap-2 mt-3 mt-md-0"
        @click="handleLogout"
      >
        <i class="bi bi-box-arrow-right fs-5"></i> Logout
      </button>
    </header>

    <!-- MAIN -->
    <main>
      <!-- INFO CARDS -->
      <div class="row g-4 mb-5">
        <div class="col-12 col-md-4">
          <div class="info-card shadow-sm rounded-4 p-4 d-flex align-items-center gap-3 bg-primary text-white">
            <i class="bi bi-database-fill fs-1 info-icon"></i>
            <div>
              <h6 class="mb-1 fw-semibold text-uppercase">Total Data</h6>
              <h2 class="fw-bold mb-0">{{ totalData }}</h2>
              <small class="opacity-75">Semua data mahasiswa yang tercatat</small>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-4">
          <div class="info-card shadow-sm rounded-4 p-4 d-flex align-items-center gap-3 bg-success text-white">
            <i class="bi bi-person-check-fill fs-1 info-icon"></i>
            <div>
              <h6 class="mb-1 fw-semibold text-uppercase">Data Aktif</h6>
              <h2 class="fw-bold mb-0">{{ activeData }}</h2>
              <small class="opacity-75">Data mahasiswa yang masih aktif</small>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-4">
          <div class="info-card shadow-sm rounded-4 p-4 d-flex align-items-center gap-3 bg-danger text-white">
            <i class="bi bi-person-x-fill fs-1 info-icon"></i>
            <div>
              <h6 class="mb-1 fw-semibold text-uppercase">Data Terhapus</h6>
              <h2 class="fw-bold mb-0">{{ deletedData }}</h2>
              <small class="opacity-75">Data yang sudah dihapus</small>
            </div>
          </div>
        </div>
      </div>

      <!-- CARD CRUD -->
      <div class="card border-0 shadow-sm mb-5 rounded-4">
        <div class="card-header bg-white border-bottom fw-semibold fs-5">
          📋 Aksi CRUD Mahasiswa
        </div>
        <div class="card-body">
          <div class="row g-3">
            <div v-for="btn in crudButtons" :key="btn.action" class="col-12 col-md-6 col-lg-3">
              <button
                class="btn btn-primary w-100 py-3 rounded-4 d-flex align-items-center justify-content-center gap-2"
                @click="goTo(btn.action)"
              >
                <i class="bi bi-pencil-square fs-5"></i> {{ btn.label }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- CARD STATISTIK -->
      <div class="card border-0 shadow-sm rounded-4">
        <div class="card-header bg-white border-bottom fw-semibold fs-5">
          📊 Statistik Mahasiswa
        </div>
        <div class="card-body">
          <div class="row g-3">
            <div v-for="btn in statButtons" :key="btn.action" class="col-12 col-md-6 col-lg-3">
              <button
                class="btn btn-outline-success w-100 py-3 rounded-4 d-flex align-items-center justify-content-center gap-2"
                @click="goTo(btn.action)"
              >
                <i class="bi bi-graph-up fs-5"></i> {{ btn.label }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const totalData = ref(0)
const activeData = ref(0)
const deletedData = ref(0)

const crudButtons = [
  { label: "Create Mahasiswa", action: "create" },
  { label: "Read Mahasiswa", action: "read" },
  { label: "Update Mahasiswa", action: "update" },
  { label: "Delete Mahasiswa", action: "delete" },
]

const statButtons = [
  { label: "Average Mahasiswa", action: "average" },
  { label: "Count Mahasiswa", action: "count" },
  { label: "Distinct Mahasiswa", action: "distinct" },
  { label: "Group Mahasiswa", action: "group" },
  { label: "Max / Min Mahasiswa", action: "maxmin" },
  { label: "Top IPK Mahasiswa", action: "topipk" },
  { label: "Tanpa Nama Mahasiswa", action: "withoutname" },
  { label: "Above Average Mahasiswa", action: "aboveaverage" },
]

const goTo = (action) => {
  router.push(`/dashboard/${action}`)
}

const handleLogout = () => {
  alert('Logout berhasil!')
  router.push('/')
}

const getStatistics = async () => {
  try {
    const response = await axios.get('https://your-api-url.com/mahasiswa/statistics')
    if (response.status === 200) {
      totalData.value = response.data.total
      activeData.value = response.data.active
      deletedData.value = response.data.deleted
    } else {
      alert('Gagal mengambil statistik data.')
    }
  } catch (error) {
    console.error(error)
    alert('Terjadi kesalahan saat mengambil statistik data.')
  }
}

onMounted(() => {
  getStatistics()
})
</script>

<style scoped>
.dashboard-wrapper {
  /* background-color: #f9fbfd; */
  min-height: 100vh;
  /* font-family: 'Poppins', sans-serif; */
}

.info-card {
  cursor: default;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.info-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

.info-icon {
  flex-shrink: 0;
}

.btn {
  transition: all 0.3s ease-in-out;
  font-weight: 600;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.card-header {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 1.25rem;
}

@media (max-width: 576px) {
  header {
    justify-content: center !important;
    text-align: center;
  }

  .info-card {
    justify-content: center !important;
  }
}
</style>
