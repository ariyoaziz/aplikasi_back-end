<template>
  <div class="container py-5" style="max-width: 600px;">
    <h2 class="mb-5 text-primary fw-bold text-center">Update Mahasiswa</h2>

    <!-- Step 1: Input NIM -->
    <form v-if="!mahasiswaLoaded" @submit.prevent="fetchMahasiswa" class="form-card mx-auto p-5 rounded shadow">
      <div class="mb-4">
        <label for="nimInput" class="form-label fw-semibold">Masukkan NIM Mahasiswa</label>
        <input
          v-model="nimInput"
          type="text"
          id="nimInput"
          class="form-control form-input"
          placeholder="Contoh: 12345678"
          required
          autofocus
        />
      </div>

      <button type="submit" class="btn btn-primary w-100 fw-semibold">Cari Mahasiswa</button>
    </form>

    <!-- Step 2: Form Update -->
    <form v-else @submit.prevent="submitUpdate" class="form-card mx-auto p-5 rounded shadow mt-4">
      <div class="mb-4">
        <label for="nim" class="form-label fw-semibold">NIM</label>
        <input
          v-model="mahasiswa.nim"
          type="text"
          id="nim"
          class="form-control form-input"
          disabled
        />
        <small class="text-muted">NIM tidak dapat diubah.</small>
      </div>

      <div class="mb-4">
        <label for="nama" class="form-label fw-semibold">Nama</label>
        <input
          v-model="mahasiswa.nama"
          type="text"
          id="nama"
          class="form-control form-input"
          placeholder="Masukkan nama lengkap"
          required
        />
      </div>

      <div class="mb-4">
        <label for="jurusan" class="form-label fw-semibold">Jurusan</label>
        <input
          v-model="mahasiswa.jurusan"
          type="text"
          id="jurusan"
          class="form-control form-input"
          placeholder="Masukkan jurusan"
          required
        />
      </div>

      <div class="mb-4">
        <label for="angkatan" class="form-label fw-semibold">Angkatan</label>
        <input
          v-model.number="mahasiswa.angkatan"
          type="number"
          id="angkatan"
          class="form-control form-input"
          placeholder="Masukkan tahun angkatan"
          required
          min="2000"
          max="2100"
        />
      </div>

      <div class="mb-5">
        <label for="ipk" class="form-label fw-semibold">IPK</label>
        <input
          v-model.number="mahasiswa.ipk"
          type="number"
          id="ipk"
          step="0.01"
          class="form-control form-input"
          placeholder="Masukkan IPK (0.00 - 4.00)"
          required
          min="0"
          max="4"
        />
      </div>

      <button type="submit" class="btn-submit btn btn-primary w-100 fw-semibold">
        Update
      </button>

      <button @click.prevent="resetForm" class="btn btn-outline-secondary w-100 mt-3">
        Reset & Cari NIM Lain
      </button>
    </form>

  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const nimInput = ref('')
const mahasiswaLoaded = ref(false)

const mahasiswa = reactive({
  nim: '',
  nama: '',
  jurusan: '',
  angkatan: '',
  ipk: '',
})

const fetchMahasiswa = async () => {
  if (!nimInput.value) {
    alert('Masukkan NIM terlebih dahulu.')
    return
  }

  try {
    const response = await axios.get(`${nimInput.value}`)
    if (response.status === 200 && response.data) {
      Object.assign(mahasiswa, response.data)
      mahasiswaLoaded.value = true
    } else {
      alert('Mahasiswa dengan NIM tersebut tidak ditemukan.')
    }
  } catch (error) {
    console.error(error)
    alert('Terjadi kesalahan saat mengambil data mahasiswa.')
  }
}

const submitUpdate = async () => {
  try {
    await axios.put(`${mahasiswa.nim}`, mahasiswa)
    alert('Data mahasiswa berhasil diperbarui!')
    router.push('/dashboard') // atau ke halaman lain sesuai kebutuhan
  } catch (error) {
    console.error(error)
    alert('Gagal memperbarui data mahasiswa.')
  }
}

const resetForm = () => {
  nimInput.value = ''
  mahasiswaLoaded.value = false
  mahasiswa.nim = ''
  mahasiswa.nama = ''
  mahasiswa.jurusan = ''
  mahasiswa.angkatan = ''
  mahasiswa.ipk = ''
}
</script>

<style scoped>
.container {
  max-width: 600px;
}

/* Form card styling */
.form-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.form-card:hover {
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

/* Input styling */
.form-input {
  border: 1.8px solid #ddd;
  border-radius: 8px;
  padding: 12px 15px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.3);
}

/* Label styling */
.form-label {
  display: block;
  margin-bottom: 6px;
  color: #333;
}

/* Submit button styling */
.btn-submit {
  padding: 14px;
  font-size: 1.1rem;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 123, 255, 0.3);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.btn-submit:hover {
  background-color: #0056b3;
  box-shadow: 0 8px 25px rgba(0, 86, 179, 0.5);
  transform: translateY(-2px);
}

button.btn-outline-secondary {
  padding: 12px;
  font-size: 1rem;
  border-radius: 10px;
  border: 2px solid #6c757d;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}

button.btn-outline-secondary:hover {
  background-color: #6c757d;
  color: #fff;
  border-color: #6c757d;
}
</style>
