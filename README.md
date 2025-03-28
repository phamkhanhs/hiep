# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 1: LINUX VÀ CÁC BẢN PHÂN PHỐI - TẬP TRUNG VÀO UBUNTU

## 1. Linux là gì?
Linux là một hệ điều hành mã nguồn mở (open-source) được xây dựng dựa trên nhân (kernel) Linux, do Linus Torvalds phát triển từ năm 1991. Không giống các hệ điều hành độc quyền như Windows hay macOS, Linux cho phép người dùng tự do truy cập, chỉnh sửa, và phân phối mã nguồn. Linux thường được gọi là **GNU/Linux**, vì nó kết hợp nhân Linux với các công cụ từ dự án GNU.

### Đặc điểm chính:
- **Mã nguồn mở**: Miễn phí, có thể tùy chỉnh.
- **Đa nhiệm và đa người dùng**: Hỗ trợ nhiều người dùng và tác vụ cùng lúc.
- **Ổn định và bảo mật**: Ít lỗi, ít bị tấn công bởi virus/malware.
- **Linh hoạt**: Chạy trên nhiều thiết bị, từ máy tính cá nhân đến máy chủ, siêu máy tính, và thiết bị nhúng.

### Ứng dụng:
Linux là nền tảng cho máy chủ web, hệ thống đám mây, Android, và các pipeline DevOps/Data Engineering. Trong Data Engineering, Linux hỗ trợ xử lý dữ liệu lớn qua các công cụ như Apache Spark, Hadoop. Trong DevOps, Linux là nền tảng cho CI/CD pipeline với Jenkins, Docker.

## 2. Lịch sử của Linux
Linux bắt nguồn từ năm 1991, khi Linus Torvalds, một sinh viên tại Đại học Helsinki (Phần Lan), bắt đầu phát triển một nhân hệ điều hành (kernel) dựa trên hệ điều hành MINIX. Ngày 25 tháng 8 năm 1991, ông công bố dự án trên nhóm tin Usenet, mời cộng đồng tham gia phát triển.

Nhân Linux được phát hành dưới giấy phép **GNU General Public License (GPL)**, cho phép bất kỳ ai sử dụng, chỉnh sửa và phân phối mã nguồn. Sự kết hợp giữa nhân Linux và các công cụ từ dự án GNU đã tạo nên một hệ điều hành hoàn chỉnh, thường được gọi là **GNU/Linux**. Từ thập niên 2010, Linux trở thành nền tảng chính cho các hệ thống đám mây và container hóa (như Docker, Kubernetes), hỗ trợ trực tiếp cho DevOps. Đến nay, Linux chiếm lĩnh thị trường máy chủ, siêu máy tính (hơn 90% siêu máy tính hàng đầu dùng Linux), và là nền tảng cho hệ điều hành Android.

## 3. Tại sao nên sử dụng Linux?
Linux mang lại nhiều lợi ích vượt trội so với các hệ điều hành khác:
- **Miễn phí và mã nguồn mở**: Tiết kiệm chi phí cho doanh nghiệp khi triển khai hệ thống lớn như cụm Hadoop.
- **Bảo mật cao**: Phân quyền chặt chẽ giúp bảo vệ pipeline dữ liệu khỏi truy cập trái phép.
- **Hiệu suất và linh hoạt**: Chạy tốt trên máy chủ đám mây như AWS EC2.
- **Tùy chỉnh cao**: Người dùng có thể tối ưu hệ thống cho nhu cầu cụ thể.
- **Hỗ trợ cộng đồng lớn**: Tài liệu phong phú giúp xử lý lỗi nhanh chóng.
- **Ứng dụng đa dạng**: Từ lập trình, quản trị hệ thống, đến chơi game (nhờ Steam Proton).

## 4. Giới thiệu về Linux và các bản phân phối
Linux được phát triển thành nhiều bản phân phối (distributions - distros), phục vụ các mục đích khác nhau:
- **Ubuntu**: Dễ dùng, phổ biến cho người mới.
- **Fedora**: Công nghệ tiên tiến, dành cho lập trình viên.
- **Debian**: Ổn định, dùng cho máy chủ.
- **Arch Linux**: Tùy chỉnh cao, dành cho người dùng nâng cao.

## 5. Lịch sử của Ubuntu
Ubuntu được ra mắt ngày 20/10/2004 bởi **Canonical Ltd.**, do **Mark Shuttleworth** sáng lập. Ubuntu dựa trên Debian nhưng được cải tiến để thân thiện hơn. Các phiên bản Ubuntu có chu kỳ phát hành **6 tháng/lần**, với các bản **LTS (Long Term Support)** được hỗ trợ 5 năm.

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
- **Kiểm tra phiên bản Ubuntu**:
  ```bash
  lsb_release -a
Kết quả: Hiển thị thông tin như Ubuntu 22.04.1 LTS.

Kiểm tra thông tin kernel:
bash

Thu gọn

Bọc lại

Sao chép
uname -r
Kết quả: Ví dụ 5.15.0-73-generic.
Xem thông tin phần cứng:
bash

Thu gọn

Bọc lại

Sao chép
lscpu
Kết quả: Hiển thị CPU, số nhân, tốc độ, v.v.
Kiểm tra dung lượng ổ cứng:
bash

Thu gọn

Bọc lại

Sao chép
df -h
Kết quả: Ví dụ /dev/sda1 20G 5.2G 14G 27% /.
Cập nhật hệ thống:
bash

Thu gọn

Bọc lại

Sao chép
sudo apt update && sudo apt upgrade -y
Kết quả: Cập nhật gói phần mềm mới nhất.
Theo dõi tài nguyên:
bash

Thu gọn

Bọc lại

Sao chép
top
Kết quả: Hiển thị CPU/RAM usage, hữu ích khi chạy pipeline nặng.
Ghi chú: Các câu lệnh này giúp kiểm tra môi trường trước khi triển khai pipeline hoặc container.

7. Tại sao chọn Ubuntu trong bối cảnh Data Engineer và DevOps?
Tích hợp tốt với DevOps: Docker, Kubernetes, Jenkins, Ansible. Ví dụ, trong thực tập, tôi dùng Ubuntu để cài Docker và chạy container Spark.
Tương thích với hệ sinh thái dữ liệu lớn: Hadoop, Spark, Kafka, Airflow.
Ổn định và đáng tin cậy: Ubuntu LTS đảm bảo không gián đoạn.
Hỗ trợ đám mây tốt: Phổ biến trên AWS, GCP, Azure.
Cộng đồng mạnh mẽ: Hỗ trợ tài liệu phong phú.
8. Ưu điểm và nhược điểm của Ubuntu
Ưu điểm:
Giao diện thân thiện, dễ dùng.
Ổn định cao với phiên bản LTS.
Bảo mật tốt, ít bị tấn công.
Miễn phí, không mất chi phí bản quyền.
Tương thích phần cứng rộng rãi.
Nhược điểm:
Hiệu suất không tối ưu trên máy cũ.
Tùy chỉnh hạn chế so với Arch Linux.
Snap package gây tranh cãi.
9. So sánh Ubuntu với các bản phân phối khác
Tiêu chí	Ubuntu	Fedora	Debian	Arch Linux
Đối tượng	Người mới	Lập trình viên	Máy chủ	Người dùng nâng cao
Dễ sử dụng	Cao	Trung bình	Trung bình	Thấp
Ổn định	Cao (LTS)	Trung bình	Rất cao	Thấp (rolling release)
Cập nhật	6 tháng/lần, LTS 2 năm/lần	6 tháng/lần	Chậm, ổn định	Liên tục
Hiệu suất	Trung bình	Cao	Trung bình	Rất cao
Tùy chỉnh	Trung bình	Trung bình	Trung bình	Rất cao
Phân tích:
Ubuntu vs Fedora: Ubuntu phù hợp hơn cho người mới như tôi trong thực tập nhờ giao diện thân thiện, trong khi Fedora thích hợp cho thử nghiệm công nghệ mới như Wayland.
Ubuntu vs Debian: Ubuntu hiện đại hơn, Debian ổn định hơn.
Ubuntu vs Arch: Ubuntu tiện lợi, Arch tùy chỉnh tối đa.
10. Kết luận
Linux là một hệ điều hành mã nguồn mở với nhiều lợi ích. Ubuntu, với sự hỗ trợ mạnh mẽ từ Canonical, là lựa chọn lý tưởng cho Data Engineer và DevOps nhờ tính ổn định, khả năng tích hợp công cụ hiện đại, và sự hỗ trợ mạnh từ cộng đồng. Thực hành cài đặt và sử dụng lệnh trên Ubuntu giúp làm quen với Linux, đặt nền tảng cho các tác vụ kỹ thuật tiếp theo. Kiến thức này sẽ giúp tôi khám phá thêm Kubernetes và Apache Airflow trong các dự án thực tập sau.



# BÁO CÁO THỰC TẬP DATA ENGINEER VÀ DEVOPS - PHẦN 2: TỔNG HỢP KIẾN THỨC

## 1. Giới thiệu
Trong quá trình thực tập với vai trò **Data Engineer** kết hợp **DevOps**, việc nắm vững các khái niệm, giao thức và công cụ mạng cơ bản là nền tảng quan trọng để triển khai, quản lý hệ thống và xử lý dữ liệu hiệu quả. Phần báo cáo này tổng hợp kiến thức về các khái niệm như **IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM**, cùng với các ví dụ thực hành đã thực hiện trong môi trường **Ubuntu**. Những kiến thức này không chỉ giúp tôi hiểu cách hoạt động của mạng mà còn hỗ trợ trực tiếp trong việc xây dựng pipeline dữ liệu và quản lý hạ tầng.

## 2. Tổng hợp kiến thức và ví dụ thực hành

### 2.1. IP (Internet Protocol)
- **Khái niệm**: IP là giao thức định tuyến và định địa chỉ cho các gói tin trên mạng. Có hai phiên bản chính:
  - **IPv4** (32-bit, ví dụ: `192.168.1.1`): Phổ biến nhưng giới hạn số lượng địa chỉ.
  - **IPv6** (128-bit, ví dụ: `2001:0db8::1`): Mở rộng không gian địa chỉ cho tương lai.
- **Vai trò**: Xác định nguồn và đích của dữ liệu, là nền tảng cho mọi giao tiếp mạng.
- **Ví dụ thực hành**: Kiểm tra địa chỉ IP trên Ubuntu để xác định cấu hình mạng trước khi triển khai pipeline:
  ```bash
  ip addr show
Kết quả: Hiển thị IP của máy, ví dụ 192.168.1.100 trên giao diện eth0.

Ứng dụng thực tế: Trong thực tập, tôi dùng IP để cấu hình kết nối giữa máy chủ Spark và worker nodes.
2.2. SSH (Secure Shell)
Khái niệm: SSH là giao thức mã hóa để truy cập và quản lý máy từ xa an toàn, sử dụng cặp khóa công khai/riêng tư hoặc mật khẩu.
Vai trò: Thay thế Telnet, đảm bảo quản trị hệ thống bảo mật.
Ví dụ thực hành: Kết nối từ máy local đến server Ubuntu để kiểm tra trạng thái Docker:
bash

Thu gọn

Bọc lại

Sao chép
ssh user@192.168.1.200
Sau khi đăng nhập, tôi chạy docker ps để xem các container đang hoạt động.
Ứng dụng thực tế: SSH giúp tôi quản lý server từ xa trong quá trình triển khai CI/CD.
2.3. SCP (Secure Copy Protocol)
Khái niệm: SCP là công cụ truyền file an toàn dựa trên SSH, mã hóa dữ liệu trong quá trình chuyển.
Vai trò: Di chuyển file giữa các máy qua mạng một cách bảo mật.
Ví dụ thực hành: Sao chép file data.csv từ local sang server để xử lý dữ liệu:
bash

Thu gọn

Bọc lại

Sao chép
scp data.csv user@192.168.1.200:/home/user/data/
Kết quả: File được truyền thành công, kiểm tra bằng ls trên server.
Ứng dụng thực tế: Tôi dùng SCP để tải dữ liệu lên server chạy pipeline Airflow.
2.4. SMTP (Simple Mail Transfer Protocol)
Khái niệm: SMTP là giao thức gửi email qua mạng, hoạt động trên port 25, 587 (TLS), hoặc 465 (SSL).
Vai trò: Chuyển email từ client đến server mail, thường dùng để thông báo.
Ví dụ thực hành: Gửi email thông báo pipeline hoàn tất bằng Python trên Ubuntu:
python

Thu gọn

Bọc lại

Sao chép
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("user@gmail.com", "password")
server.sendmail("user@gmail.com", "recipient@example.com", "Pipeline completed")
Kết quả: Email được gửi thành công đến người nhận.
Ứng dụng thực tế: Trong thực tập, tôi tích hợp SMTP vào pipeline để báo cáo trạng thái xử lý dữ liệu.
2.5. FTP (File Transfer Protocol) và SFTP (Secure FTP)
Khái niệm:
FTP: Truyền file không mã hóa, đơn giản nhưng dễ bị tấn công.
SFTP: Dùng SSH để mã hóa, an toàn hơn FTP.
Vai trò: FTP phù hợp cho mạng nội bộ; SFTP dùng trong môi trường không an toàn.
Ví dụ thực hành: Tải file từ server bằng SFTP để đảm bảo bảo mật:
bash

Thu gọn

Bọc lại

Sao chép
sftp user@192.168.1.200
get /home/user/data.csv
Kết quả: File data.csv được tải về máy local an toàn.
Ứng dụng thực tế: Tôi ưu tiên SFTP để truyền dữ liệu nhạy cảm giữa các máy trong dự án.
2.6. HTTP/HTTPS (HyperText Transfer Protocol / Secure)
Khái niệm: HTTP truyền tải trang web qua port 80; HTTPS thêm mã hóa SSL/TLS qua port 443.
Vai trò: HTTP truy cập web cơ bản; HTTPS bảo mật dữ liệu nhạy cảm.
Ví dụ thực hành: Kiểm tra API dữ liệu bằng curl:
bash

Thu gọn

Bọc lại

Sao chép
curl -I https://api.example.com
Kết quả: Trả về header với mã trạng thái 200 OK.
Ứng dụng thực tế: Dùng HTTPS để lấy dữ liệu từ API công khai trong pipeline ETL.
2.7. DNS (Domain Name System)
Khái niệm: DNS chuyển tên miền (ví dụ: google.com) thành địa chỉ IP, hoạt động như "danh bạ" của internet.
Vai trò: Giúp truy cập dịch vụ dễ dàng qua tên thay vì nhớ IP.
Ví dụ thực hành: Tra cứu IP của tên miền để kiểm tra kết nối:
bash

Thu gọn

Bọc lại

Sao chép
nslookup google.com
Kết quả: Hiển thị IP như 142.250.190.14.
Ứng dụng thực tế: Tôi dùng DNS để cấu hình truy cập dịch vụ đám mây trong thực tập.
2.8. UDP (User Datagram Protocol)
Khái niệm: UDP là giao thức truyền dữ liệu không kết nối, nhanh nhưng không đảm bảo thứ tự hay độ tin cậy.
Vai trò: Dùng trong ứng dụng cần tốc độ cao như streaming, game online.
Ví dụ thực hành: Kiểm tra port UDP bằng netcat để thử nghiệm truyền dữ liệu:
bash

Thu gọn

Bọc lại

Sao chép
nc -u 192.168.1.200 12345
Kết quả: Gửi và nhận dữ liệu thử nghiệm qua UDP.
Ứng dụng thực tế: UDP hữu ích khi truyền log thời gian thực từ hệ thống giám sát.
2.9. TCP (Transmission Control Protocol)
Khái niệm: TCP là giao thức truyền dữ liệu có kết nối, đảm bảo thứ tự và độ tin cậy qua cơ chế handshake.
Vai trò: Dùng trong HTTP, SSH, email, yêu cầu độ chính xác cao.
Ví dụ thực hành: Kiểm tra kết nối TCP đến port SSH:
bash

Thu gọn

Bọc lại

Sao chép
telnet 192.168.1.200 22
Kết quả: Kết nối thành công đến port SSH.
Ứng dụng thực tế: TCP đảm bảo dữ liệu pipeline được truyền đầy đủ, không mất mát.
2.10. VPN (Virtual Private Network)
Khái niệm: VPN tạo đường hầm mã hóa để truy cập mạng riêng từ xa, thường dùng IPsec hoặc OpenVPN.
Vai trò: Bảo mật kết nối và vượt qua giới hạn địa lý.
Ví dụ thực hành: Cấu hình VPN bằng OpenVPN để truy cập mạng nội bộ:
bash

Thu gọn

Bọc lại

Sao chép
sudo openvpn --config client.ovpn
Kết quả: Kết nối thành công đến mạng nội bộ công ty.
Ứng dụng thực tế: Tôi dùng VPN để truy cập server DevOps từ xa trong thực tập.
2.11. NAT (Network Address Translation)
Khái niệm: NAT ánh xạ địa chỉ IP nội bộ sang IP công cộng, thường do router thực hiện.
Vai trò: Tiết kiệm IP công cộng, bảo vệ mạng nội bộ khỏi truy cập trực tiếp.
Ví dụ thực hành: Kiểm tra NAT trên router bằng lệnh:
bash

Thu gọn

Bọc lại

Sao chép
ip route
Kết quả: Xác định gateway mặc định (ví dụ: 192.168.1.1).
Ứng dụng thực tế: NAT giúp tôi cấu hình mạng nội bộ cho cụm máy chủ Hadoop.
2.12. VM (Virtual Machine)
Khái niệm: VM là máy ảo chạy trên phần mềm như VirtualBox, VMware, mô phỏng hệ thống độc lập.
Vai trò: Tạo môi trường thử nghiệm mà không ảnh hưởng hệ thống chính.
Ví dụ thực hành: Cài Ubuntu trên VirtualBox để thử nghiệm pipeline:
Tải ISO Ubuntu 22.04.
Tạo VM với 2GB RAM, 20GB ổ cứng.
Cài đặt và chạy:
bash

Thu gọn

Bọc lại

Sao chép
uname -a
Kết quả: Hiển thị thông tin kernel, ví dụ Linux ubuntu 5.15.0-73-generic.
Ứng dụng thực tế: Tôi dùng VM để chạy thử container Docker trước khi triển khai lên server.
3. Ứng dụng trong Data Engineer và DevOps
Data Engineer:
SCP, SFTP: Truyền file dữ liệu lớn (ví dụ: dataset 10GB) giữa các server.
SMTP: Gửi thông báo khi pipeline ETL hoàn tất.
HTTP/HTTPS: Truy cập API để lấy dữ liệu đầu vào cho Spark.
DevOps:
SSH: Quản lý server từ xa, kiểm tra trạng thái container.
VPN: Kết nối an toàn đến hạ tầng nội bộ.
VM: Thử nghiệm pipeline CI/CD trước khi triển khai production.
TCP/UDP: Tối ưu truyền dữ liệu giữa các node trong cụm Kubernetes.
4. Kết luận
Việc nắm vững các khái niệm và công cụ mạng cơ bản như IP, SSH, SCP, SMTP, FTP, SFTP, HTTP/HTTPS, DNS, UDP, TCP, VPN, NAT, VM là nền tảng để thực hiện các tác vụ trong Data Engineering và DevOps. Các ví dụ thực hành trên Ubuntu không chỉ giúp tôi hiểu cách hoạt động của từng công cụ mà còn áp dụng chúng vào quản lý hệ thống, truyền dữ liệu, và triển khai pipeline thực tế trong thực tập. Kiến thức này sẽ là bước đệm để tôi tiếp tục khám phá các công nghệ nâng cao như Kubernetes, Apache Airflow, và hệ thống giám sát trong các dự án sau.
