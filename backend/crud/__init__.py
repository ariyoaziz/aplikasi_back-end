from .count_mahasiswa import count_all_mahasiswa
from .distinct_mahasiswa import get_all_jurusan
from .avarage_mahasiswa import get_average_ipk
from .max_min_mahasiswa import get_max_ipk, get_min_ipk
from .group_mahasiswa import count_per_angkatan
from .above_avarage_mahasiswa import get_mahasiswa_above_average
from .top_ipk_mahasiswa import top5_mahasiswa
from .tanpa_nama_mahasiswa import mahasiswa_tanpa_nama
from .create_mahasiswa import create_mahasiswa
from .delete_mahasiswa import delete_mahasiswa
from .update_mahasiswa import update_mahasiswa
from .read_mahasiswa import get_mahasiswa

__all__ = [
    "count_all_mahasiswa",
    "get_all_jurusan",
    "get_average_ipk",
    "get_max_ipk",
    "get_min_ipk",
    "count_per_angkatan",
    "get_mahasiswa_above_average",
    "top5_mahasiswa",
    "mahasiswa_tanpa_nama",
    "create_mahasiswa",
    "delete_mahasiswa",
    "update_mahasiswa",
    "get_mahasiswa",
]
