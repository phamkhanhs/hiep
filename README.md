# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS

## Mục lục
- [Phần 1: Linux và Ubuntu](#phần-1-linux-và-các-bản-phân-phối---tập-trung-vào-ubuntu)
  - [1. Linux là gì?](#1-linux-là-gì)
  - [2. Lịch sử của Linux](#2-lịch-sử-của-linux)
  - [3. Tại sao nên sử dụng Linux?](#3-tại-sao-nên-sử-dụng-linux)
  - [4. Giới thiệu về Linux và các bản phân phối](#4-giới-thiệu-về-linux-và-các-bản-phân-phối)
  - [5. Lịch sử của Ubuntu](#5-lịch-sử-của-ubuntu)
  - [6. Ví dụ thực hành cài đặt và kiểm tra](#6-ví-dụ-thực-hành-cài-đặt-và-kiểm-tra-các-câu-lệnh-của-linux-ubuntu)
  - [7. Tại sao chọn Ubuntu cho Data Engineer và DevOps?](#7-tại-sao-tôi-chọn-ubuntu-trong-bối-cảnh-data-engineer-và-devops)
  - [8. Ưu điểm và nhược điểm của Ubuntu](#8-ưu-điểm-và-nhược-điểm-của-ubuntu)
  - [9. So sánh Ubuntu với các bản phân phối khác](#9-so-sánh-ubuntu-với-các-bản-phân-phối-khác)
  - [10. Package Management và Shell Scripting](#10-package-management-và-shell-scripting)
  - [11. System Administration](#11-system-administration)
  - [12. Bảo mật Linux](#12-bảo-mật-linux)
  - [13. Kết luận phần 1](#13-kết-luận-phần-1)
- [Phần 2: Tổng hợp kiến thức mạng](#phần-2-tổng-hợp-kiến-thức-mạng)
  - [1. Giới thiệu](#1-giới-thiệu)
  - [2. Khái niệm mạng cơ bản](#2-khái-niệm-mạng-cơ-bản)
  - [3. Các thuật ngữ mạng máy tính](#3-các-thuật-ngữ-mạng-máy-tính)
  - [4. Công cụ mạng cơ bản và thực hành](#4-công-cụ-mạng-cơ-bản-và-thực-hành)
  - [5. Tổng hợp giao thức và ví dụ thực hành](#5-tổng-hợp-giao-thức-và-ví-dụ-thực-hành)
  - [6. Container Networking](#6-container-networking)
  - [7. Cloud Networking](#7-cloud-networking)
  - [8. Network Security](#8-network-security)
  - [9. Monitoring và Logging](#9-monitoring-và-logging)
  - [10. Troubleshooting Guide](#10-troubleshooting-guide)
  - [11. Ứng dụng trong Data Engineer và DevOps](#11-ứng-dụng-trong-data-engineer-và-devops)
  - [12. Kết luận phần 2](#12-kết-luận-phần-2)

# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 1: LINUX VÀ CÁC BẢN PHÂN PHỐI - TẬP TRUNG VÀO UBUNTU

## 1. Linux là gì?
Linux là một hệ điều hành mã nguồn mở (open-source) được xây dựng dựa trên nhân (kernel) Linux, do Linus Torvalds phát triển từ năm 1991. Không giống các hệ điều hành độc quyền như Windows hay macOS, Linux cho phép người dùng tự do truy cập, chỉnh sửa, và phân phối mã nguồn. Linux thường được gọi là **GNU/Linux**, vì nó kết hợp nhân Linux với các công cụ từ dự án GNU.

### Đặc điểm chính
* **Mã nguồn mở**: Miễn phí, có thể tùy chỉnh.
* **Đa nhiệm và đa người dùng**: Hỗ trợ nhiều người dùng và tác vụ cùng lúc.
* **Ổn định và bảo mật**: Ít lỗi, ít bị tấn công bởi virus/malware.
* **Linh hoạt**: Chạy trên nhiều thiết bị, từ máy tính cá nhân đến máy chủ, siêu máy tính, và thiết bị nhúng.

### Ứng dụng
Linux là nền tảng cho máy chủ web, hệ thống đám mây, Android, và các pipeline DevOps/Data Engineering. Trong Data Engineering, Linux hỗ trợ xử lý dữ liệu lớn qua các công cụ như Apache Spark, Hadoop. Trong DevOps, Linux là nền tảng cho CI/CD pipeline với Jenkins, Docker.

## 2. Lịch sử của Linux
Linux bắt nguồn từ năm 1991, khi Linus Torvalds, một sinh viên tại Đại học Helsinki (Phần Lan), bắt đầu phát triển một nhân hệ điều hành (kernel) dựa trên hệ điều hành MINIX. Ngày 25 tháng 8 năm 1991, ông công bố dự án trên nhóm tin Usenet, mời cộng đồng tham gia phát triển.

Nhân Linux được phát hành dưới giấy phép **GNU General Public License (GPL)**, cho phép bất kỳ ai sử dụng, chỉnh sửa và phân phối mã nguồn. Sự kết hợp giữa nhân Linux và các công cụ từ dự án GNU đã tạo nên một hệ điều hành hoàn chỉnh, thường được gọi là **GNU/Linux**. Từ thập niên 2010, Linux trở thành nền tảng chính cho các hệ thống đám mây và container hóa (như Docker, Kubernetes), hỗ trợ trực tiếp cho DevOps. Đến nay, Linux chiếm lĩnh thị trường máy chủ, siêu máy tính (hơn 90% siêu máy tính hàng đầu dùng Linux), và là nền tảng cho hệ điều hành Android.

## 3. Tại sao nên sử dụng Linux?
Linux mang lại nhiều lợi ích vượt trội so với các hệ điều hành khác:
* **Miễn phí và mã nguồn mở**: Tiết kiệm chi phí cho doanh nghiệp khi triển khai hệ thống lớn như cụm Hadoop.
* **Bảo mật cao**: Phân quyền chặt chẽ giúp bảo vệ pipeline dữ liệu khỏi truy cập trái phép.
* **Hiệu suất và linh hoạt**: Chạy tốt trên máy chủ đám mây như AWS EC2.
* **Tùy chỉnh cao**: Người dùng có thể tối ưu hệ thống cho nhu cầu cụ thể.
* **Hỗ trợ cộng đồng lớn**: Tài liệu phong phú giúp xử lý lỗi nhanh chóng.
* **Ứng dụng đa dạng**: Từ lập trình, quản trị hệ thống, đến chơi game (nhờ Steam Proton).

## 4. Giới thiệu về Linux và các bản phân phối
Linux được phát triển thành nhiều bản phân phối (distributions - distros), phục vụ các mục đích khác nhau:
* **Ubuntu**: Dễ dùng, phổ biến cho người mới.
* **Fedora**: Công nghệ tiên tiến, dành cho lập trình viên.
* **Debian**: Ổn định, dùng cho máy chủ.
* **Arch Linux**: Tùy chỉnh cao, dành cho người dùng nâng cao.

## 5. Lịch sử của Ubuntu
Ubuntu được ra mắt ngày 20/10/2004 bởi **Canonical Ltd.**, do **Mark Shuttleworth** sáng lập. Ubuntu dựa trên Debian nhưng được cải tiến để thân thiện hơn. Các phiên bản Ubuntu có chu kỳ phát hành **6 tháng/lần**, với các bản **LTS (Long Term Support)** được hỗ trợ 5 năm.

## 6. Ví dụ thực hành cài đặt và kiểm tra các câu lệnh của Linux (Ubuntu)

### 6.1. Cài đặt Ubuntu
#### Chuẩn bị
* Tải file ISO Ubuntu 22.04 LTS từ [ubuntu.com](https://ubuntu.com).
* Tạo USB boot bằng **Rufus (Windows)** hoặc `dd` (Linux).
* Yêu cầu phần cứng tối thiểu: **2GB RAM, 20GB ổ cứng**.

#### Quy trình cài đặt
1. Cắm USB, vào BIOS, chọn boot từ USB.
2. Chọn **"Install Ubuntu"** từ menu GRUB.
3. Chọn ngôn ngữ, múi giờ, phân vùng ổ cứng, tạo user/password.
4. Hoàn tất cài đặt, khởi động lại máy.

#### Cài đặt thông qua WSL/WSL2 trên Windows
WSL (Windows Subsystem for Linux) cho phép chạy môi trường Linux trực tiếp trên Windows mà không cần máy ảo.

##### Cài đặt WSL2
1. Bật tính năng WSL trên Windows:
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

2. Khởi động lại máy tính.

3. Tải và cài đặt Linux kernel update package từ Microsoft.

4. Đặt WSL2 làm phiên bản mặc định:
```powershell
wsl --set-default-version 2
```

##### Cài đặt Ubuntu trên WSL
* **Cách 1**: Qua Microsoft Store
  1. Mở Microsoft Store
  2. Tìm "Ubuntu"
  3. Chọn phiên bản (Ubuntu 22.04 LTS) và nhấn "Get"
  4. Sau khi cài đặt, khởi động Ubuntu và tạo user/password

* **Cách 2**: Qua Command Line
```powershell
wsl --install -d Ubuntu-22.04
```

##### Ưu điểm của WSL2
* Tích hợp tốt với Windows
* Hiệu năng gần với Linux native
* Hỗ trợ GPU cho các tác vụ AI/ML
* Dễ dàng truy cập file giữa Windows và Linux
* Phù hợp cho phát triển DevOps và Data Engineering

##### Lưu ý khi dùng WSL2
* Cần Windows 10 version 2004 trở lên
* Yêu cầu virtualization được bật trong BIOS
* Một số giới hạn về networking khác với Linux native
* Nên cấu hình giới hạn RAM để tránh WSL2 dùng quá nhiều tài nguyên

### 6.2. Kiểm tra các câu lệnh cơ bản
* **Kiểm tra phiên bản Ubuntu**:
```bash
lsb_release -a
```
* **Kiểm tra thông tin kernel**:
```bash
uname -r
```
* **Xem thông tin phần cứng**:
```bash
lscpu
```
* **Kiểm tra dung lượng ổ cứng**:
```bash
df -h
```
* **Cập nhật hệ thống**:
```bash
sudo apt update && sudo apt upgrade -y
```
* **Theo dõi tài nguyên**:
```bash
top
```

## 7. Tại sao tôi chọn Ubuntu trong bối cảnh Data Engineer và DevOps?
* **Tích hợp tốt với DevOps**: Docker, Kubernetes, Jenkins, Ansible.
* **Tương thích với hệ sinh thái dữ liệu lớn**: Hadoop, Spark, Kafka, Airflow.
* **Ổn định và đáng tin cậy**: Ubuntu LTS đảm bảo không gián đoạn.
* **Hỗ trợ đám mây tốt**: Phổ biến trên AWS, GCP, Azure.
* **Cộng đồng mạnh mẽ**: Hỗ trợ tài liệu phong phú.

## 8. Ưu điểm và nhược điểm của Ubuntu
### Ưu điểm
* Giao diện thân thiện, dễ dùng.
* Ổn định cao với phiên bản LTS.
* Bảo mật tốt, ít bị tấn công.
* Miễn phí, không mất chi phí bản quyền.
* Tương thích phần cứng rộng rãi.

### Nhược điểm
* Hiệu suất không tối ưu trên máy cũ.
* Tùy chỉnh hạn chế so với Arch Linux.
* Snap package gây tranh cãi.

## 9. So sánh Ubuntu với các bản phân phối khác
| Tiêu chí | Ubuntu | Fedora | Debian | Arch Linux |
|----------|---------|---------|---------|------------|
| Đối tượng | Người mới | Lập trình viên | Máy chủ | Người dùng nâng cao |
| Dễ sử dụng | Cao | Trung bình | Trung bình | Thấp |
| Ổn định | Cao (LTS) | Trung bình | Rất cao | Thấp (rolling release) |
| Cập nhật | 6 tháng/lần | 6 tháng/lần | Chậm, ổn định | Liên tục |
| Hiệu suất | Trung bình | Cao | Trung bình | Rất cao |
| Tùy chỉnh | Trung bình | Trung bình | Trung bình | Rất cao |

## 10. Package Management và Shell Scripting

### 10.1. Package Management
#### APT (Advanced Package Tool)
* **Cài đặt packages**:
```bash
sudo apt update
sudo apt install tên-gói
```
* **Xóa packages**:
```bash
sudo apt remove tên-gói
sudo apt autoremove
```
* **Tìm kiếm packages**:
```bash
apt search từ-khóa
```

#### Snap
* **Ưu điểm**:
  * Tự động cập nhật
  * Bảo mật sandbox
  * Hỗ trợ đa phân phối
* **Nhược điểm**:
  * Khởi động chậm hơn
  * Chiếm nhiều dung lượng
* **Ví dụ**:
```bash
sudo snap install docker
```

#### Flatpak
* **Ưu điểm**:
  * Độc lập với bản phân phối
  * Bảo mật sandbox
* **Nhược điểm**:
  * Cài đặt phức tạp hơn
* **Ví dụ**:
```bash
flatpak install flathub com.spotify.Client
```

### 10.2. Shell Scripting
#### Cơ bản
```bash
#!/bin/bash
# Biến
TEN="Người dùng"
echo "Xin chào $TEN"

# Vòng lặp
for i in {1..5}; do
    echo $i
done

# Điều kiện
if [ -f "tập-tin.txt" ]; then
    echo "Tập tin tồn tại"
fi
```

#### Hàm
```bash
#!/bin/bash
sao_luu_csdl() {
    local TEN_CSDL=$1
    local THU_MUC_SAO_LUU="/sao-luu"
    
    echo "Đang sao lưu $TEN_CSDL vào $THU_MUC_SAO_LUU"
    # logic sao lưu ở đây
}

sao_luu_csdl "csdl-cua-toi"
```

## 11. System Administration

### 11.1. Systemd Services
* **Tạo service mới**:
```ini
[Unit]
Description=Dịch Vụ Tùy Chỉnh Của Tôi
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/dich-vu-cua-toi
Restart=always

[Install]
WantedBy=multi-user.target
```

* **Quản lý services**:
```bash
sudo systemctl start dich-vu-cua-toi
sudo systemctl enable dich-vu-cua-toi
sudo systemctl status dich-vu-cua-toi
```

### 11.2. Log Management
* **Xem logs**:
```bash
journalctl -u dich-vu-cua-toi
```
* **Rotate logs**:
```bash
logrotate /etc/logrotate.d/dich-vu-cua-toi
```

## 12. Bảo mật Linux

### 12.1. File Permissions
```bash
# Thay đổi chủ sở hữu
chown nguoidung:nhom tap-tin.txt

# Thay đổi quyền truy cập
chmod 755 tap-tin.txt

# Đặt quyền mặc định
umask 022
```

### 12.2. SELinux/AppArmor
* **Chế độ SELinux**:
  * Cưỡng chế
  * Cho phép
  * Vô hiệu hóa
* **Hồ sơ AppArmor**:
```bash
aa-status
aa-enforce /etc/apparmor.d/ho-so
```

### 12.3. Các Biện Pháp Bảo Mật Tốt Nhất
* Sử dụng khóa SSH thay vì mật khẩu
* Cập nhật hệ thống thường xuyên
* Giám sát nhật ký hệ thống
* Sao lưu định kỳ
* Cấu hình tường lửa

## 13. Kết luận phần 1
Linux và đặc biệt là Ubuntu là nền tảng vững chắc cho Data Engineer và DevOps, với các công cụ quản lý package đa dạng, khả năng scripting mạnh mẽ, và tính năng bảo mật cao. Việc hiểu và áp dụng đúng các công cụ này sẽ giúp tối ưu hóa workflow và đảm bảo hệ thống hoạt động ổn định, an toàn.

# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 2: TỔNG HỢP KIẾN THỨC MẠNG

## 1. Giới thiệu
Trong thực tập vai trò **Data Engineer** kết hợp **DevOps**, việc hiểu các khái niệm mạng cơ bản, thuật ngữ, giao thức và công cụ mạng là bước đầu để tôi quản lý hệ thống và xử lý dữ liệu hiệu quả. Phần báo cáo này tổng hợp kiến thức về mạng, bao gồm **khái niệm cơ bản**, **thuật ngữ**, **công cụ mạng**, và các thực hành trên **Ubuntu** với các giao thức như **IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM**.

## 2. Khái niệm mạng cơ bản
* **Mạng máy tính**: Là hệ thống kết nối các máy tính để chia sẻ tài nguyên (dữ liệu, phần cứng) qua các giao thức.
* **Các thành phần chính**:
  * **Node**: Thiết bị trong mạng (máy tính, server, router).
  * **Giao thức**: Quy tắc để truyền dữ liệu (IP, TCP, UDP).
  * **Topology**: Cách bố trí mạng (bus, star, ring).
* **Vai trò trong thực tập**: Hiểu mạng giúp tôi cấu hình server, truyền dữ liệu, và triển khai pipeline.

## 3. Các thuật ngữ mạng máy tính
* **LAN (Local Area Network)**: Mạng nội bộ, phạm vi nhỏ (ví dụ: văn phòng).
* **WAN (Wide Area Network)**: Mạng diện rộng, kết nối nhiều khu vực (ví dụ: internet).
* **Port**: Cổng logic để phân biệt dịch vụ (80 cho HTTP, 22 cho SSH).
* **Packet**: Đơn vị dữ liệu truyền qua mạng.
* **Router**: Thiết bị định tuyến gói tin giữa các mạng.
* **Firewall**: Hệ thống bảo vệ mạng khỏi truy cập trái phép.

## 4. Công cụ mạng cơ bản và thực hành
* **Ping**: Kiểm tra kết nối mạng.
```bash
ping 192.168.1.200
```
Kết quả: Nhận phản hồi nếu máy đích hoạt động.

* **Netstat**: Xem trạng thái kết nối mạng.
```bash
netstat -tuln
```
Kết quả: Hiển thị các port đang lắng nghe (ví dụ: 22, 80).

* **Traceroute**: Theo dõi đường đi của gói tin.
```bash
traceroute google.com
```
Kết quả: Liệt kê các hop từ máy tôi đến Google.

## 5. Tổng hợp giao thức và ví dụ thực hành

### 5.1. IP (Internet Protocol)
* **Khái niệm**: IP định địa chỉ cho máy tính (IPv4: 192.168.1.1, IPv6: 2001:0db8::1).
* **Vai trò**: Định tuyến dữ liệu.
* **Ví dụ thực hành**: Kiểm tra IP:
```bash
ip addr show
```
Kết quả: 192.168.1.100 trên eth0.

### 5.2. SSH (Secure Shell)
* **Khái niệm**: SSH mã hóa kết nối từ xa.
* **Vai trò**: Quản lý server.
* **Ví dụ thực hành**: Đăng nhập server:
```bash
ssh user@192.168.1.200
```
Kết quả: Truy cập shell, chạy uptime.

### 5.3. SCP (Secure Copy Protocol)
* **Khái niệm**: SCP truyền file qua SSH.
* **Vai trò**: Chuyển dữ liệu an toàn.
* **Ví dụ thực hành**: Upload file:
```bash
scp data.csv user@192.168.1.200:/home/user/data/
```
Kết quả: File có trên server.

### 5.4. SMTP (Simple Mail Transfer Protocol)
* **Khái niệm**: SMTP gửi email.
* **Vai trò**: Thông báo công việc.
* **Ví dụ thực hành**: Gửi email:
```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("user@gmail.com", "password")
server.sendmail("user@gmail.com", "recipient@example.com", "Pipeline completed")
```
Kết quả: Email gửi thành công.

### 5.5. FTP (File Transfer Protocol) và SFTP (Secure FTP)
* **Khái niệm**: 
  * FTP: Truyền file không mã hóa
  * SFTP: Dùng SSH để mã hóa, an toàn hơn FTP
* **Vai trò**: FTP phù hợp cho mạng nội bộ; SFTP dùng trong môi trường không an toàn.
* **Ví dụ thực hành**: Tải file bằng SFTP:
```bash
sftp user@192.168.1.200
get /home/user/data.csv
```
Kết quả: File tải về local.

### 5.6. HTTP/HTTPS (HyperText Transfer Protocol / Secure)
* **Khái niệm**: HTTP truyền web; HTTPS mã hóa.
* **Vai trò**: Truy cập web/API.
* **Ví dụ thực hành**: Kiểm tra API:
```bash
curl -I https://api.example.com
```
Kết quả: Mã 200 OK.

### 5.7. DNS (Domain Name System)
* **Khái niệm**: DNS chuyển tên miền thành IP.
* **Vai trò**: Truy cập dịch vụ qua tên.
* **Ví dụ thực hành**: Tra cứu IP:
```bash
nslookup google.com
```
Kết quả: IP như 142.250.190.14.

### 5.8. UDP (User Datagram Protocol)
* **Khái niệm**: UDP truyền nhanh, không kiểm tra lỗi.
* **Vai trò**: Dùng cho tốc độ cao.
* **Ví dụ thực hành**: Test UDP:
```bash
nc -u 192.168.1.200 12345
```
Kết quả: Truyền tin nhắn thử.

### 5.9. TCP (Transmission Control Protocol)
* **Khái niệm**: TCP truyền đáng tin cậy.
* **Vai trò**: Đảm bảo dữ liệu chính xác.
* **Ví dụ thực hành**: Kiểm tra SSH:
```bash
telnet 192.168.1.200 22
```
Kết quả: Kết nối thành công.

### 5.10. VPN (Virtual Private Network)
* **Khái niệm**: VPN mã hóa kết nối.
* **Vai trò**: Bảo mật mạng.
* **Ví dụ thực hành**: Dùng OpenVPN:
```bash
sudo openvpn --config client.ovpn
```
Kết quả: Kết nối mạng công ty.

### 5.11. NAT (Network Address Translation)
* **Khái niệm**: NAT đổi IP nội bộ thành công cộng.
* **Vai trò**: Bảo vệ mạng.
* **Ví dụ thực hành**: Xem gateway:
```bash
ip route
```
Kết quả: Gateway 192.168.1.1.

### 5.12. VM (Virtual Machine)
* **Khái niệm**: VM là máy ảo.
* **Vai trò**: Thử nghiệm hệ thống.
* **Ví dụ thực hành**: Cài Ubuntu:
  1. Tải ISO Ubuntu 22.04.
  2. Tạo VM: 2GB RAM, 20GB ổ cứng.
  3. Chạy:
```bash
uname -a
```
Kết quả: Kernel 5.15.0-73-generic.

## 6. Ứng dụng trong Data Engineer và DevOps
### Data Engineer
* SCP/SFTP: Chuyển dataset.
* SMTP: Báo cáo pipeline.
* HTTP/HTTPS: Lấy dữ liệu API.

### DevOps
* SSH: Quản lý server.
* VPN: Kết nối nội bộ.
* VM: Test pipeline.

## 7. Kết luận
Phần này giúp tôi hiểu khái niệm mạng, thuật ngữ, và công cụ qua thực hành trên Ubuntu. Các kiến thức về IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM hỗ trợ tôi trong việc quản lý hệ thống và pipeline dữ liệu, là nền tảng cho công việc Data Engineer và DevOps.

## 6. Container Networking

### 6.1. Docker Networking
* **Network drivers**:
  * Bridge
  * Host
  * Overlay
  * Macvlan
* **Commands**:
```bash
# Create network
docker network create mynet

# Connect container
docker run --network mynet nginx
```

### 6.2. Kubernetes Networking
* **Services**:
  * ClusterIP
  * NodePort
  * LoadBalancer
* **Network Policies**:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow
spec:
  podSelector:
    matchLabels:
      app: api
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
```

## 7. Cloud Networking

### 7.1. Virtual Private Cloud (VPC)
* **Components**:
  * Subnets
  * Route Tables
  * Internet Gateways
  * NAT Gateways
* **Best Practices**:
  * Separate public/private subnets
  * Use Network ACLs
  * Implement VPC Flow Logs

### 7.2. Security Groups
```bash
# AWS CLI example
aws ec2 create-security-group \
    --group-name my-sg \
    --description "My security group"
```

## 8. Network Security

### 8.1. SSL/TLS Certificates
```bash
# Generate self-signed certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout private.key -out certificate.crt
```

### 8.2. Firewall Rules
```bash
# UFW examples
sudo ufw allow 22/tcp
sudo ufw allow from 192.168.1.0/24 to any port 3306
```

## 9. Monitoring và Logging

### 9.1. Prometheus
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

### 9.2. ELK Stack
* **Filebeat configuration**:
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/*.log
```

## 10. Troubleshooting Guide

### 10.1. Network Issues
* **Connectivity**:
```bash
# Check DNS
dig example.com

# Check routing
traceroute example.com

# Check ports
netstat -tuln
```

### 10.2. Common Problems
* **DNS Resolution**:
```bash
# Edit resolv.conf
nameserver 8.8.8.8
nameserver 8.8.4.4
```

* **SSL Issues**:
```bash
# Test SSL
openssl s_client -connect example.com:443
```

## 11. Ứng dụng trong Data Engineer và DevOps

### Data Engineer
* Pipeline monitoring
* Data transfer optimization
* Security compliance

### DevOps
* CI/CD networking
* Infrastructure automation
* Container orchestration

## 12. Kết luận phần 2
Kiến thức mạng là nền tảng quan trọng cho cả Data Engineer và DevOps. Việc hiểu và áp dụng đúng các concepts về networking, từ cơ bản đến nâng cao như container networking và cloud infrastructure, sẽ giúp xây dựng và vận hành hệ thống một cách hiệu quả và an toàn.

## Tài liệu tham khảo
1. Ubuntu Documentation: https://help.ubuntu.com/
2. Docker Networking: https://docs.docker.com/network/
3. Kubernetes Networking: https://kubernetes.io/docs/concepts/services-networking/
4. AWS VPC Documentation: https://docs.aws.amazon.com/vpc/
5. Prometheus Documentation: https://prometheus.io/docs/
6. ELK Stack: https://www.elastic.co/guide/
