<template>
  <div class="dashboard-wrapper container py-5">
    <!-- HEADER -->
    <header class="d-flex justify-content-between align-items-center mb-5">
      <div>
        <h1 class="display-6 fw-bold text-dark">🎓 Dashboard Mahasiswa</h1>
        <p class="text-muted mb-0">Kelola data dan statistik mahasiswa dengan mudah.</p>
      </div>
      <button class="btn btn-outline-danger d-flex align-items-center gap-2" @click="handleLogout">
        <i class="bi bi-box-arrow-right"></i> Logout
      </button>
    </header>

    <!-- MAIN -->
    <main>
      <!-- CARD CRUD -->
      <div class="card border-0 shadow-sm mb-4">
        <div class="card-header bg-white border-bottom fw-semibold fs-5">
          📋 Aksi CRUD Mahasiswa
        </div>
        <div class="card-body">
          <div class="row g-3">
            <div
              v-for="btn in crudButtons"
              :key="btn.action"
              class="col-12 col-md-6 col-lg-3"
            >
              <button
                class="btn btn-primary w-100 py-2 rounded-3 d-flex align-items-center justify-content-center gap-2"
                @click="goTo(btn.action)"
              >
                <i class="bi bi-pencil-square"></i> {{ btn.label }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- CARD STATISTIK -->
      <div class="card border-0 shadow-sm">
        <div class="card-header bg-white border-bottom fw-semibold fs-5">
          📊 Statistik Mahasiswa
        </div>
        <div class="card-body">
          <div class="row g-3">
            <div
              v-for="btn in statButtons"
              :key="btn.action"
              class="col-12 col-md-6 col-lg-3"
            >
              <button
                class="btn btn-outline-success w-100 py-2 rounded-3 d-flex align-items-center justify-content-center gap-2"
                @click="goTo(btn.action)"
              >
                <i class="bi bi-graph-up"></i> {{ btn.label }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const crudButtons = [
  { label: "Create Mahasiswa", action: "create" },
  { label: "Read Mahasiswa", action: "read" },
  { label: "Update Mahasiswa", action: "update" },
  { label: "Delete Mahasiswa", action: "delete" },
];

const statButtons = [
  { label: "Average Mahasiswa", action: "average" },
  { label: "Count Mahasiswa", action: "count" },
  { label: "Distinct Mahasiswa", action: "distinct" },
  { label: "Group Mahasiswa", action: "group" },
  { label: "Max / Min Mahasiswa", action: "maxmin" },
  { label: "Top IPK Mahasiswa", action: "topipk" },
  { label: "Tanpa Nama Mahasiswa", action: "withoutname" },
  { label: "Above Average Mahasiswa", action: "aboveaverage" },
];

const goTo = (action) => {
  router.push(`/dashboard/${action}`)
}

const handleLogout = () => {
  alert("Logout berhasil!")
  router.push("/")
}
</script>

<style scoped>
.dashboard-wrapper {
  background-color: #f7f9fc;
  min-height: 100vh;
}

/* Efek Hover Modern */
.btn {
  transition: all 0.3s ease-in-out;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
}
</style>
