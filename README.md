# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 1: LINUX VÀ CÁC BẢN PHÂN PHỐI - TẬP TRUNG VÀO UBUNTU

## 1. Linux là gì?
Linux là một hệ điều hành mã nguồn mở (open-source) được xây dựng dựa trên nhân (kernel) Linux, do Linus Torvalds phát triển từ năm 1991. Không giống các hệ điều hành độc quyền như Windows hay macOS, Linux cho phép người dùng tự do truy cập, chỉnh sửa, và phân phối mã nguồn. Linux thường được gọi là **GNU/Linux**, vì nó kết hợp nhân Linux với các công cụ từ dự án GNU.

### Đặc điểm chính:
- **Mã nguồn mở**: Miễn phí, có thể tùy chỉnh.
- **Đa nhiệm và đa người dùng**: Hỗ trợ nhiều người dùng và tác vụ cùng lúc.
- **Ổn định và bảo mật**: Ít lỗi, ít bị tấn công bởi virus/malware.
- **Linh hoạt**: Chạy trên nhiều thiết bị, từ máy tính cá nhân đến máy chủ, siêu máy tính, và thiết bị nhúng.

### Ứng dụng:
Linux là nền tảng cho máy chủ web, hệ thống đám mây, Android, và các pipeline DevOps/Data Engineering.

## 2. Lịch sử của Linux
Linux bắt nguồn từ năm 1991, khi Linus Torvalds, một sinh viên tại Đại học Helsinki (Phần Lan), bắt đầu phát triển một nhân hệ điều hành (kernel) dựa trên hệ điều hành MINIX. Ngày 25 tháng 8 năm 1991, ông công bố dự án trên nhóm tin Usenet, mời cộng đồng tham gia phát triển.

Nhân Linux được phát hành dưới giấy phép **GNU General Public License (GPL)**, cho phép bất kỳ ai sử dụng, chỉnh sửa và phân phối mã nguồn. Sự kết hợp giữa nhân Linux và các công cụ từ dự án GNU đã tạo nên một hệ điều hành hoàn chỉnh, thường được gọi là **GNU/Linux**. Đến nay, Linux chiếm lĩnh thị trường máy chủ, siêu máy tính (hơn 90% siêu máy tính hàng đầu dùng Linux), và là nền tảng cho hệ điều hành Android.

## 3. Tại sao nên sử dụng Linux?
Linux mang lại nhiều lợi ích vượt trội so với các hệ điều hành khác:
- **Miễn phí và mã nguồn mở**
- **Bảo mật cao**
- **Hiệu suất và linh hoạt**
- **Tùy chỉnh cao**
- **Hỗ trợ cộng đồng lớn**
- **Ứng dụng đa dạng: lập trình, quản trị hệ thống, chơi game...**

## 4. Giới thiệu về Linux và các bản phân phối
Linux được phát triển thành nhiều bản phân phối (distributions - distros), phục vụ các mục đích khác nhau:
- **Ubuntu**: Dễ dùng, phổ biến cho người mới.
- **Fedora**: Công nghệ tiên tiến, dành cho lập trình viên.
- **Debian**: Ổn định, dùng cho máy chủ.
- **Arch Linux**: Tùy chỉnh cao, dành cho người dùng nâng cao.

## 5. Lịch sử của Ubuntu
Ubuntu được ra mắt ngày 20/10/2004 bởi **Canonical Ltd.**, do **Mark Shuttleworth** sáng lập. Ubuntu dựa trên Debian nhưng được cải tiến để thân thiện hơn. 

Các phiên bản Ubuntu có chu kỳ phát hành **6 tháng/lần**, với các bản **LTS (Long Term Support) được hỗ trợ 5 năm**.

## 6. Ví dụ thực hành cài đặt và kiểm tra các câu lệnh của Linux (Ubuntu)

### 6.1. Cài đặt Ubuntu
#### Chuẩn bị:
- Tải file ISO Ubuntu 22.04 LTS từ [ubuntu.com](https://ubuntu.com).
- Tạo USB boot bằng **Rufus (Windows)** hoặc `dd` (Linux).
- Yêu cầu phần cứng tối thiểu: **2GB RAM, 20GB ổ cứng**.

#### Quy trình cài đặt:
1. Cắm USB, vào BIOS, chọn boot từ USB.
2. Chọn **"Install Ubuntu"** từ menu GRUB.
3. Chọn ngôn ngữ, múi giờ, phân vùng ổ cứng, tạo user/password.
4. Hoàn tất cài đặt, khởi động lại máy.

### 6.2. Kiểm tra các câu lệnh cơ bản
**Kiểm tra phiên bản Ubuntu:**
```bash
lsb_release -a
```
*Kết quả: Hiển thị thông tin như Ubuntu 22.04.1 LTS.*

**Kiểm tra thông tin kernel:**
```bash
uname -r
```
*Kết quả: Ví dụ 5.15.0-73-generic.*

**Xem thông tin phần cứng:**
```bash
lscpu
```
*Kết quả: Hiển thị CPU, số nhân, tốc độ, v.v.*

**Kiểm tra dung lượng ổ cứng:**
```bash
df -h
```
*Kết quả: Ví dụ /dev/sda1 20G 5.2G 14G 27% /*

**Cập nhật hệ thống:**
```bash
sudo apt update && sudo apt upgrade -y
```
*Kết quả: Cập nhật gói phần mềm mới nhất.*

## 7. Tại sao chọn Ubuntu trong bối cảnh Data Engineer và DevOps?
- **Tích hợp tốt với DevOps**: Docker, Kubernetes, Jenkins, Ansible.
- **Tương thích với hệ sinh thái dữ liệu lớn**: Hadoop, Spark, Kafka, Airflow.
- **Ổn định và đáng tin cậy**: Ubuntu LTS đảm bảo không gián đoạn.
- **Hỗ trợ đám mây tốt**: Ubuntu là nền tảng phổ biến trên AWS, GCP, Azure.
- **Cộng đồng mạnh mẽ**: Hỗ trợ tài liệu phong phú.

## 8. Ưu điểm và nhược điểm của Ubuntu
### Ưu điểm:
- Giao diện thân thiện, dễ dùng.
- Ổn định cao với phiên bản LTS.
- Bảo mật tốt, ít bị tấn công.
- Miễn phí, không mất chi phí bản quyền.
- Tương thích phần cứng rộng rãi.

### Nhược điểm:
- Hiệu suất không tối ưu trên máy cũ.
- Tùy chỉnh hạn chế so với Arch Linux.
- Snap package gây tranh cãi.

## 9. So sánh Ubuntu với các bản phân phối khác
| Tiêu chí     | Ubuntu | Fedora | Debian | Arch Linux |
|-------------|--------|--------|--------|------------|
| **Đối tượng** | Người mới | Lập trình viên | Máy chủ | Người dùng nâng cao |
| **Dễ sử dụng** | Cao | Trung bình | Trung bình | Thấp |
| **Ổn định** | Cao (LTS) | Trung bình | Rất cao | Thấp (rolling release) |
| **Cập nhật** | 6 tháng/lần, LTS 2 năm/lần | 6 tháng/lần | Chậm, ổn định | Liên tục |
| **Hiệu suất** | Trung bình | Cao | Trung bình | Rất cao |
| **Tùy chỉnh** | Trung bình | Trung bình | Trung bình | Rất cao |

## 10. Kết luận
Linux là một hệ điều hành mã nguồn mở với nhiều lợi ích. Ubuntu, với sự hỗ trợ mạnh mẽ từ Canonical, là lựa chọn lý tưởng cho Data Engineer và DevOps nhờ tính ổn định, khả năng tích hợp công cụ hiện đại, và sự hỗ trợ mạnh từ cộng đồng. Thực hành cài đặt và sử dụng lệnh trên Ubuntu giúp làm quen với Linux, đặt nền tảng cho các tác vụ kỹ thuật tiếp theo.




# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 2: TỔNG HỢP KIẾN THỨC

## 1. Giới thiệu
Trong quá trình thực tập với vai trò **Data Engineer** kết hợp **DevOps**, việc nắm vững các khái niệm, giao thức và công cụ mạng cơ bản là nền tảng quan trọng để triển khai, quản lý hệ thống và xử lý dữ liệu hiệu quả. Phần báo cáo này tổng hợp kiến thức về các khái niệm như **IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM**, cùng với các ví dụ thực hành đã thực hiện trong môi trường **Ubuntu**.

## 2. Tổng hợp kiến thức và ví dụ thực hành

### 2.1. IP (Internet Protocol)
- **Khái niệm**: IP là giao thức định tuyến và định địa chỉ cho các gói tin trên mạng. Có hai phiên bản chính:
  - **IPv4** (32-bit, ví dụ: `192.168.1.1`)
  - **IPv6** (128-bit, ví dụ: `2001:0db8::1`)
- **Vai trò**: Xác định nguồn và đích của dữ liệu trong mạng.
- **Ví dụ thực hành**: Kiểm tra địa chỉ IP trên Ubuntu bằng lệnh:
  ```bash
  ip addr show
  ```
  Kết quả: Hiển thị IP của máy, ví dụ `192.168.1.100` trên giao diện `eth0`.

### 2.2. SSH (Secure Shell)
- **Khái niệm**: SSH là giao thức mã hóa để truy cập và quản lý máy từ xa an toàn.
- **Vai trò**: Thay thế Telnet, cho phép thực thi lệnh từ xa.
- **Ví dụ thực hành**: Kết nối từ máy local đến server Ubuntu:
  ```bash
  ssh user@192.168.1.200
  ```
  Sau khi nhập mật khẩu, tôi đã truy cập shell của server để kiểm tra log hệ thống.

### 2.3. SCP (Secure Copy Protocol)
- **Khái niệm**: SCP là công cụ truyền file an toàn dựa trên SSH.
- **Vai trò**: Di chuyển file giữa các máy qua mạng.
- **Ví dụ thực hành**: Sao chép file `data.csv` từ local sang server:
  ```bash
  scp data.csv user@192.168.1.200:/home/user/data/
  ```
  File được truyền thành công và kiểm tra bằng lệnh `ls` trên server.

### 2.4. SMTP (Simple Mail Transfer Protocol)
- **Khái niệm**: SMTP là giao thức gửi email qua mạng.
- **Vai trò**: Đảm bảo email được chuyển từ client đến server mail.
- **Ví dụ thực hành**: Cấu hình gửi email thông báo từ script Python trên Ubuntu:
  ```python
  import smtplib
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("user@gmail.com", "password")
  server.sendmail("user@gmail.com", "recipient@example.com", "Pipeline completed")
  ```
  Email thông báo hoàn tất pipeline dữ liệu đã được gửi.

### 2.5. FTP (File Transfer Protocol) và SFTP (Secure FTP)
- **Khái niệm**:
  - **FTP** truyền file không mã hóa.
  - **SFTP** sử dụng SSH để mã hóa dữ liệu.
- **Vai trò**: FTP đơn giản nhưng kém an toàn; SFTP bảo mật hơn.
- **Ví dụ thực hành**: Tải file từ server bằng SFTP:
  ```bash
  sftp user@192.168.1.200
  get /home/user/data.csv
  ```
  File `data.csv` được tải về máy local an toàn.

### 2.6. HTTP/HTTPS (HyperText Transfer Protocol / Secure)
- **Khái niệm**: HTTP là giao thức truyền tải trang web; HTTPS bổ sung mã hóa SSL/TLS.
- **Vai trò**: Truy cập web (HTTP) và bảo mật dữ liệu (HTTPS).
- **Ví dụ thực hành**: Kiểm tra phản hồi từ API bằng `curl`:
  ```bash
  curl -I https://api.example.com
  ```
  Kết quả: Trả về header với mã trạng thái `200 OK`.

### 2.7. DNS (Domain Name System)
- **Khái niệm**: DNS chuyển tên miền (ví dụ: `google.com`) thành địa chỉ IP.
- **Vai trò**: Giúp truy cập dịch vụ qua tên thay vì IP.
- **Ví dụ thực hành**: Tra cứu IP của tên miền:
  ```bash
  nslookup google.com
  ```
  Kết quả: Hiển thị IP như `142.250.190.14`.

### 2.8. UDP (User Datagram Protocol)
- **Khái niệm**: UDP là giao thức truyền dữ liệu không kết nối, nhanh nhưng không đảm bảo thứ tự.
- **Vai trò**: Dùng trong streaming, game online.
- **Ví dụ thực hành**: Kiểm tra port UDP bằng `netcat`:
  ```bash
  nc -u 192.168.1.200 12345
  ```
  Gửi và nhận dữ liệu thử nghiệm qua UDP.

## 3. Ứng dụng trong Data Engineer và DevOps
- **Data Engineer**:
  - **SCP, SFTP**: Truyền dữ liệu lớn.
  - **SMTP**: Gửi thông báo pipeline.
  - **HTTP/HTTPS**: Truy cập API dữ liệu.
- **DevOps**:
  - **SSH**: Quản lý server.
  - **VPN**: Kết nối an toàn.
  - **VM**: Thử nghiệm pipeline CI/CD.
  - **TCP/UDP**: Tối ưu mạng.

## 4. Kết luận
Việc nắm vững các khái niệm và công cụ mạng cơ bản như **IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM** là nền tảng để thực hiện các tác vụ trong **Data Engineering** và **DevOps**. Các ví dụ thực hành trên Ubuntu đã giúp tôi hiểu rõ cách áp dụng chúng vào quản lý hệ thống, truyền dữ liệu và triển khai pipeline. Kiến thức này sẽ là bước đệm để tôi tiếp tục phát triển trong lĩnh vực **kỹ thuật dữ liệu** và **vận hành hệ thống**.

