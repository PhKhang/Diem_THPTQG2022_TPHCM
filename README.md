# Diem_THPTQG2022_TPHCM
Tra cứu điểm THPT bằng SBD/họ tên của các thí sinh TP.HCM trong file excel có sẵn, hoặc chỉnh sửa chương trình để tự tải dữ liệu xuống từ sở. 

## Installing scraping script

### Prerequisites
- Python và chạy được `python -V` từ mọi nơi trong cmd/powershell. Nếu không có, dùng https://www.microsoft.com/store/productId/9PJPW5LDXLZ5
- Pip. Nếu không có, chạy `python get-pip.py`

### Setting up

Tải xuống file `diem12.py` và vào thư mục có chứa file đó, hoặc dùng lệnh (nếu được):
```
git clone https://github.com/PhKhang/Diem_THPTQG2022_TPHCM
cd .\Diem_THPTQG2022_TPHCM\
```

Tải các module cần thiết:
```
pip install pandas requests bs4 lxml rich
```

### Building

Chỉnh sửa range SBD (optional: cho máy chậm, chỉ dò được 2000 thí sinh như i5 gen 2 đời Tống) và tên output file (optional) trong `diem12.py`.
Chạy:
```
python .\diem12.py
```
File CSV sẽ hiện trong thư mục của chương trình.
Cách chuyển từ file [.csv sang .xlsx](https://www.thegioididong.com/hoi-dap/cach-khac-phuc-file-csv-bi-loi-font-tieng-viet-khi-mo-1392354#:~:text=M%E1%BB%9F%20file%20Excel%20%3E%20Ch%E1%BB%8Dn%20th%E1%BA%BB%20Data%20%3E%20Nh%E1%BA%A5n%20v%C3%A0o%20Get%20External%20Data%20%3E%20Ch%E1%BB%8Dn%20From%20Text%20%3E%20Ch%E1%BB%8Dn%20file%20CSV%20c%E1%BA%A7n%20m%E1%BB%9F%20%3E%20Nh%E1%BA%A5n%20Open%20%3E%20Ch%E1%BB%8Dn%20Delimited%20%3E%20%C4%90i%20%C4%91%E1%BA%BFn%20File%20origin%20%3E%20Ch%E1%BB%8Dn%20UTF%2D8%20%3E%20Nh%E1%BA%A5n%20Next%20%3E%20Ch%E1%BB%89%20t%C3%ADch%20ch%E1%BB%8Dn%20%C3%B4%20Comma%20%3E%20Nh%E1%BA%A5n%20Next%20%3E%20Nh%E1%BA%A5n%20Finish%20%3E%20Ch%E1%BB%8Dn%20%C3%B4%20ch%E1%BB%A9a%20d%E1%BB%AF%20li%E1%BB%87u%20%3E%20Nh%E1%BA%A5n%20OK%20%C4%91%E1%BB%83%20m%E1%BB%9F%20file%20CSV%20kh%C3%B4ng%20b%E1%BB%8B%20l%E1%BB%97i%20font.) 
