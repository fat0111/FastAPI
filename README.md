# 🎁 [LAB 1] - FAST API


Ứng dụng API sử dụng trí tuệ nhân tạo để sinh nội dung quảng bá địa điểm du lịch bất ngờ theo phong cách "Hộp mù" (Blind Box).

## 👤 1. Thông tin sinh viên
* **Họ và tên:** Đinh Tiến Phát
* **Mã số sinh viên:** 24120405
* **Môn học:** Tư Duy Tính Toán
* **Giảng viên thực hành:** Lê Đức Khoan
---

## 🤖 2. Tên mô hình và liên kết
Hệ thống triển khai mô hình ngôn ngữ thế hệ mới từ nền tảng **Hugging Face**:
* **Tên mô hình:** Qwen2.5-0.5B-Instruct
* **Liên kết:** [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)

---

## 🌟 3. Mô tả ngắn về chức năng của hệ thống
Hệ thống đóng vai trò cung cấp API thông minh cho ứng dụng **Blind Box Travelling**, giúp giải quyết bài toán nội dung cho các địa điểm du lịch ẩn (Hidden Gems):
* **Sinh manh mối bí ẩn:** Từ tên một địa danh, AI đóng vai hướng dẫn viên bí ẩn để viết ra 4 dòng mô tả hấp dẫn.
* **Tự động hóa nội dung:** Giúp tạo ra hàng ngàn tấm vé "Hộp mù" khác nhau một cách nhanh chóng với văn phong lôi cuốn.
* **Tối ưu hóa Local AI:** Sử dụng mô hình kích thước nhỏ (0.5B) để đảm bảo tốc độ phản hồi API cực nhanh ngay trên máy tính cá nhân.

---

## 🛠 4. Hướng dẫn cài đặt thư viện
Yêu cầu máy tính đã cài đặt **Python 3.8+**. Thực hiện cài đặt các thư viện cần thiết thông qua file `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🚀 5. Hướng dẫn chạy chương trình
### Bước 1: Khởi động API Server
Để chạy chương trình, thực hiện lệnh sau tại thư mục gốc của dự án:
```bash
uvicorn main:app --reload
```
*Lưu ý: Trong lần đầu chạy, hệ thống sẽ tự động tải mô hình từ Hugging Face (khoảng 1GB).*

### Bước 2: Chạy kiểm thử (Test)
Mở một terminal mới và chạy file script để kiểm tra kết quả trả về từ AI:
```bash
python test_api.py
```

---

## 🔌 6. Hướng dẫn gọi API và Ví dụ request/response
Hệ thống sử dụng **FastAPI** với tài liệu trực quan tại `http://127.0.0.1:8000/docs`.

### **Endpoint: Sinh manh mối Blind Box**
* **URL:** `http://127.0.0.1:8000/generate`
* **Method:** `POST`
* **Dữ liệu đầu vào (Request Body):**
```json
{
  "location": "Chùa Một Cột",
  "max_new_tokens": 150
}
```
* **Kết quả trả về (Response JSON):**
```json
{
  "location": "Chùa Một Cột",
  "blind_box_hint": "Địa điểm này là một di tích văn hóa nổi tiếng ở vùng núi phía Bắc Việt Nam, nằm trong khu vực núi rừng đặc biệt. Đây là nơi có nhiều tác phẩm nghệ thuật quý giá như bức tranh "Cây cỏ" và "Đền Hùng", được UNESCO công nhận là Di sản thế giới. Chùa này còn nổi tiếng với những nghi lễ truyền thống như cầu vồng, lễ hội tinh thần và các hoạt động văn hóa dân gian độc đáo. Chùa này còn là điểm đến lý tưởng cho hành hương, tham quan và trải nghiệm văn hóa cổ kính của người dân tộc thiểu số ở miền núi phía Bắc."
}
```

---

## 🎬 7. Liên kết video demo

https://github.com/user-attachments/assets/03935d6b-d6cd-40ea-82ce-5bc78bf90712


---





