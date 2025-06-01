<template>
  <div class="container py-5" style="max-width: 600px;">
    <h2 class="mb-5 text-danger fw-bold text-center">Hapus Mahasiswa</h2>

    <!-- Step 1: Input NIM -->
    <form v-if="!mahasiswaLoaded" @submit.prevent="fetchMahasiswa" class="form-card mx-auto p-5 rounded shadow">
      <div class="mb-4">
        <label for="nimInput" class="form-label fw-semibold">Masukkan NIM Mahasiswa yang ingin dihapus</label>
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

      <button type="submit" class="btn btn-danger w-100 fw-semibold">Cari Mahasiswa</button>
    </form>

    <!-- Step 2: Tampilkan detail dan tombol hapus -->
    <div v-else class="form-card mx-auto p-5 rounded shadow mt-4">
      <div class="mb-3">
        <h5>Data Mahasiswa</h5>
        <ul class="list-group">
          <li class="list-group-item"><strong>NIM:</strong> {{ mahasiswa.nim }}</li>
          <li class="list-group-item"><strong>Nama:</strong> {{ mahasiswa.nama }}</li>
          <li class="list-group-item"><strong>Jurusan:</strong> {{ mahasiswa.jurusan }}</li>
          <li class="list-group-item"><strong>Angkatan:</strong> {{ mahasiswa.angkatan }}</li>
          <li class="list-group-item"><strong>IPK:</strong> {{ mahasiswa.ipk }}</li>
        </ul>
      </div>

      <button @click="confirmDelete" class="btn btn-danger w-100 fw-semibold mb-3">
        Hapus Mahasiswa
      </button>

      <button @click="resetForm" class="btn btn-outline-secondary w-100">
        Batal & Cari NIM Lain
      </button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import axios from "axios";

const nimInput = ref("");
const mahasiswaLoaded = ref(false);

const mahasiswa = reactive({
  nim: "",
  nama: "",
  jurusan: "",
  angkatan: "",
  ipk: "",
});

const fetchMahasiswa = async () => {
  if (!nimInput.value) {
    alert("Masukkan NIM terlebih dahulu.");
    return;
  }

  try {
    const response = await axios.get(`${nimInput.value}`);
    if (response.status === 200 && response.data) {
      Object.assign(mahasiswa, response.data);
      mahasiswaLoaded.value = true;
    } else {
      alert("Mahasiswa dengan NIM tersebut tidak ditemukan.");
    }
  } catch (error) {
    console.error(error);
    alert("Terjadi kesalahan saat mengambil data mahasiswa.");
  }
};

const confirmDelete = async () => {
  const confirmed = confirm(`Yakin ingin menghapus mahasiswa dengan NIM ${mahasiswa.nim}?`);
  if (!confirmed) return;

  try {
    await axios.delete(`${mahasiswa.nim}`);
    alert("Mahasiswa berhasil dihapus.");
    resetForm();
  } catch (error) {
    console.error(error);
    alert("Gagal menghapus mahasiswa.");
  }
};

const resetForm = () => {
  nimInput.value = "";
  mahasiswaLoaded.value = false;
  mahasiswa.nim = "";
  mahasiswa.nama = "";
  mahasiswa.jurusan = "";
  mahasiswa.angkatan = "";
  mahasiswa.ipk = "";
};
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
  border-color: #dc3545;
  box-shadow: 0 0 8px rgba(220, 53, 69, 0.3);
}

/* Label styling */
.form-label {
  display: block;
  margin-bottom: 6px;
  color: #333;
}

/* Button styling */
.btn-danger {
  padding: 14px;
  font-size: 1.1rem;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(220, 53, 69, 0.3);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.btn-danger:hover {
  background-color: #bd2130;
  box-shadow: 0 8px 25px rgba(189, 33, 48, 0.5);
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

.list-group-item strong {
  width: 90px;
  display: inline-block;
  color: #555;
}
</style>
