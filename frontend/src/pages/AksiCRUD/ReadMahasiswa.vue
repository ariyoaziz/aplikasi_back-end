<template>
  <div class="container py-5">
    <header class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">Daftar Mahasiswa</h2>
      <button @click="downloadExcel" class="btn btn-success d-flex align-items-center gap-2 px-4 py-2 shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-file-earmark-spreadsheet" viewBox="0 0 16 16">
          <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zM10 1v3a1 1 0 0 0 1 1h3v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-12a1 1 0 0 1 1-1h6z"/>
          <path d="M8 8H6v1h2v1H5v1h3v1H6v1h3v-1H8v-1h2v-1H8V8z"/>
        </svg>
        Unduh Excel
      </button>
    </header>

    <div class="table-responsive shadow rounded">
      <table class="table table-hover mb-0">
        <thead class="table-light">
          <tr>
            <th scope="col" class="text-secondary">No</th>
            <th scope="col" class="text-secondary">NIM</th>
            <th scope="col" class="text-secondary">Nama</th>
            <th scope="col" class="text-secondary">Jurusan</th>
            <th scope="col" class="text-secondary">Angkatan</th>
            <th scope="col" class="text-secondary">IPK</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="6" class="text-center py-5 text-muted">Memuat data...</td>
          </tr>
          <tr v-else-if="mahasiswaList.length === 0">
            <td colspan="6" class="text-center py-5 text-muted">Data tidak tersedia.</td>
          </tr>
          <tr v-else v-for="(mhs, index) in mahasiswaList" :key="mhs.id" class="align-middle">
            <td class="text-secondary">{{ index + 1 }}</td>
            <td>{{ mhs.nim }}</td>
            <td>{{ mhs.nama }}</td>
            <td>{{ mhs.jurusan }}</td>
            <td>{{ mhs.angkatan }}</td>
            <td>{{ mhs.ipk }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "@/axios";
import * as XLSX from "xlsx";

const mahasiswaList = ref([]);
const loading = ref(true);

const getMahasiswa = async () => {
  try {
    const response = await axios.get("/mahasiswa");
    if (response.status === 200) {
      mahasiswaList.value = response.data;
    } else {
      alert("Gagal mengambil data mahasiswa.");
    }
  } catch (error) {
    console.error(error);
    alert("Terjadi kesalahan saat mengambil data.");
  } finally {
    loading.value = false;
  }
};

const downloadExcel = () => {
  const data = mahasiswaList.value.map((mhs, index) => ({
    No: index + 1,
    NIM: mhs.nim,
    Nama: mhs.nama,
    Jurusan: mhs.jurusan,
    Angkatan: mhs.angkatan,
    IPK: mhs.ipk,
  }));

  const worksheet = XLSX.utils.json_to_sheet(data);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Mahasiswa");

  XLSX.writeFile(workbook, "Daftar_Mahasiswa.xlsx");
};

onMounted(() => {
  getMahasiswa();
});
</script>

<style scoped>
.container {
  max-width: 100vh;
  min-height: 100vh;
  
}

h2 {
  font-size: 1.8rem;
}

button.btn {
  font-weight: 600;
  background-color: #28a745;
  border: none;
  transition: background-color 0.3s ease;
  user-select: none;
}

button.btn:hover {
  background-color: #218838;
}

.table {
  border-collapse: separate !important;
  border-spacing: 0 8px;
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
  overflow: hidden;
  border-radius: 8px;
}

.table thead tr th {
  border-bottom: none !important;
  padding: 14px 20px;
}

.table tbody tr {
  background-color: #fff;
  transition: box-shadow 0.3s ease;
  cursor: default;
}

.table tbody tr:hover {
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.12);
  background-color: #f9fefd;
}

.table tbody tr td {
  padding: 14px 20px;
  vertical-align: middle;
}

.text-secondary {
  color: #6c757d !important;
}
</style>
