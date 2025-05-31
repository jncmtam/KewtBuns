## 🧩 **Tính năng chính**

### 1. Trang bán hàng

* Danh sách sản phẩm (lọc theo màu, giá, tuổi, giới tính...)
* Ảnh/video chất lượng cao
* Nút “Mua ngay” / “Đặt cọc”
* Hiển thị FOMO: “Chỉ còn 2 bé!”, “3 người đang xem”
* Tích hợp thanh toán (Momo, COD, chuyển khoản)

### 2. Blog chia sẻ kiến thức

* Bài viết như: “Chăm sóc Holland Lop 101”, “Cách chọn chuồng”
* SEO-friendly URL: `/blog/chon-tho-holland-lop`

### 3. Chatbot tư vấn

* Trả lời câu hỏi về thỏ, sản phẩm, chăm sóc
* Hiểu tiếng Việt, có cảm xúc (lo lắng, vui mừng…)
* Gợi ý sản phẩm theo câu hỏi người dùng
* Tích hợp trên web dạng widget

### 4. Quản lý đơn hàng / hàng tồn

* Trang admin theo dõi đơn và tồn kho
* Tạo mã giảm giá
* Theo dõi lịch sử mua hàng, tỷ lệ chuyển đổi

### 5. Các tiện ích khác

* Gửi email xác nhận đơn hàng
* Tốc độ tải nhanh (<2s), hỗ trợ di động tốt
* Tính năng đánh giá sản phẩm, feedback

---

## 🛠️ **Công nghệ sử dụng**

### **Frontend (Giao diện)**

* `ReactJS + TypeScript`: xây UI theo component
* `Tailwind CSS`: responsive, tối ưu mobile
* `Shopify Storefront API`: lấy dữ liệu sản phẩm, giỏ hàng
* `Redux/Zustand`: quản lý trạng thái FOMO, giỏ hàng
* `PostCSS`: hiệu ứng động tùy chỉnh

### **Backend**

* `Flask (Python)`: API tùy chỉnh (chatbot, đơn hàng, thanh toán)
* `PostgreSQL`: lưu blog, lịch sử chat, dữ liệu người dùng
* `Docker`: môi trường nhất quán khi dev & deploy
* `Momo API`: xử lý thanh toán nội địa
* `Shopify Admin API`: lấy dữ liệu đơn hàng, tồn kho

### **Chatbot AI**

* `PhoBERT` / `ViT5`: mô hình xử lý tiếng Việt
* `LoRA`: fine-tune mô hình nhỏ, tiết kiệm tài nguyên
* `LangChain + LlamaIndex`: tạo chatbot RAG thông minh
* `Qdrant` hoặc `Chroma`: lưu vector embedding
* `ElasticSearch`: tìm kiếm blog/sản phẩm
* `RLHF`: cải thiện trả lời dựa vào phản hồi người dùng
* `OCR (Tesseract)`: xử lý ảnh nếu cần (tuỳ chọn nâng cao)

### **Khác**

* `Google Analytics`: theo dõi lượt truy cập
* `Shopify SEO Tools`: tối ưu thứ hạng tìm kiếm
* `AWS / Heroku`: deploy backend
* `JWT + Flask`: phân quyền admin (nếu cần)
