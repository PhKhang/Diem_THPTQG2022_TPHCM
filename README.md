# Diem_THPTQG2022_TPHCM
Tra cứu điểm bằng SBD/họ tên của các thí sinh TP.HCM trong file có sẵn, hoặc chỉnh sửa chương trình để tự tải dữ liệu xuống từ sở. 

## Installing scraping script

### Prerequisites
- Python và chạy được `python -V` từ mọi nơi trong cmd/powershell. Nếu không, dùng https://www.microsoft.com/store/productId/9PJPW5LDXLZ5
- Pip. Nếu không có, chạy `python get-pip.py`

### Setting up

Tải xuống file `diem12.py` và vào thư mục có chứa file đó, hoặc dùng:
```
git clone https://github.com/PhKhang/Diem_THPTQG2022_TPHCM
cd .\Diem_THPTQG2022_TPHCM\
```

Tải các module cần thiết:
```
pip install pandas requests bs4 lxml rich
```

### Building

Chỉnh sửa range SBD (optional cho máy chậm, chỉ dò được 2000 thí sinh) và tên output file trong `lop12.py`.
Chạy:
```
python .\lop12.py
```
File CSV sẽ hiện trong thư mục của chương trình.
