## 🛍️ 1. **Shopify APIs** – Quản lý bán hàng, đơn hàng và trải nghiệm mua sắm

### 🧷 Storefront API (GraphQL)

* **Mục đích**: Dùng để xây dựng giao diện khách hàng (React + Tailwind) và truy vấn sản phẩm, giỏ hàng, thanh toán.
* **Chức năng chính**:

  * `products`: Lấy danh sách sản phẩm (thỏ Holland Lop, chuồng, thức ăn…)
  * `cart`: Tạo và cập nhật giỏ hàng
  * `checkout`: Tạo link thanh toán
* **Ứng dụng**: Kết hợp với Buy Button hoặc Checkout SDK để nhúng quy trình thanh toán vào frontend.
* **Tài liệu**: [Shopify Storefront API](https://shopify.dev/docs/api/storefront)

---

### 🔧 Admin API (REST hoặc GraphQL)

* **Mục đích**: Quản lý dữ liệu nội bộ như kho hàng, đơn hàng, khách hàng cho dashboard quản trị.
* **Chức năng chính**:

  * `products`: Tạo / sửa / xóa sản phẩm và biến thể (màu lông, tuổi thỏ…)
  * `orders`: Lấy thông tin đơn hàng
  * `customers`: Quản lý thông tin người mua
  * `discounts`: Tạo mã giảm giá (giảm giá có thời hạn để tạo cảm giác khan hiếm)
* **Ứng dụng**: Flask dùng để truy xuất dữ liệu này, kết hợp JWT để phân quyền admin.
* **Tài liệu**: [Shopify Admin API](https://shopify.dev/docs/api/admin)

---

### 🔔 Webhook

* **Mục đích**: Lắng nghe sự kiện thời gian thực từ Shopify.
* **Webhook phổ biến**:

  * `orders/create`: Gửi thông báo "ai đó vừa mua thỏ Holland Lop!"
  * `products/update`: Cập nhật tồn kho → hiển thị thông báo "sắp hết hàng"
  * `carts/update`: Theo dõi hành vi người dùng để cải thiện chuyển đổi
* **Ứng dụng**: Flask backend xử lý Webhook và lưu vào Postgres, đồng thời đẩy thông báo qua WebSocket.

---

### 🎁 Custom Attributes API (phần mở rộng của Storefront)

* **Mục đích**: Cho phép người mua tùy chọn (khắc tên, chọn quà…)
* **Ứng dụng**: Gửi các thuộc tính tùy chỉnh trong quá trình checkout (vd: “Tên của thỏ là gì?”)
* **Tài liệu**: [Custom Attributes - Checkout Object](https://shopify.dev/docs/api/storefront/reference/checkout)

---

## 💰 2. **API Cổng Thanh Toán Momo**

* **Mục đích**: Xử lý thanh toán cho khách hàng tại Việt Nam.
* **Các endpoint chính**:

  * `POST /payment/request`: Gửi yêu cầu thanh toán
  * `GET /payment/query`: Kiểm tra trạng thái thanh toán
  * `POST /payment/refund`: Hoàn tiền
* **Ứng dụng**: Flask tạo request gửi đến Momo, nhận callback khi thanh toán hoàn tất → lưu vào Postgres.
* **Tài liệu**: [Momo Developer](https://developers.momo.vn)

---

## 📈 3. **Google Analytics Data API**

* **Mục đích**: Theo dõi hành vi người dùng trên trang (tỉ lệ chuyển đổi, số lần xem sản phẩm…)
* **Endpoint chính**:

  * `GET /runReport`: Tạo báo cáo tuỳ chỉnh
* **Ứng dụng**:

  * Nhúng tracking code vào React frontend
  * Flask gọi API để hiển thị báo cáo cho admin
* **Tài liệu**: [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data)

---

## 🐍 4. **Flask API Tùy Chỉnh**

### 🤖 API Chatbot

* **Mục đích**: Giao tiếp giữa người dùng và chatbot (hỏi cách nuôi thỏ, tư vấn sản phẩm…)
* **Các endpoint**:

  * `POST /chatbot/query`: Gửi câu hỏi từ người dùng
  * `GET /chatbot/logs`: Lấy lịch sử chat
  * `POST /chatbot/feedback`: Gửi phản hồi để cải thiện AI
* **Kỹ thuật**: Sử dụng LangChain, LlamaIndex, PhoBERT/ViT5 và vector database Qdrant hoặc Chroma.

---

### 📊 API Analytics tùy chỉnh

* **Mục đích**: Theo dõi chatbot, sản phẩm nổi bật, ngoài phân tích mặc định của Shopify
* **Endpoint**:

  * `GET /analytics/sales`: Lấy dữ liệu bán hàng
  * `GET /analytics/chatbot`: Theo dõi tỉ lệ tương tác chatbot

---

### 🧾 API xử lý Webhook

* **Mục đích**: Nhận sự kiện từ Momo hoặc Shopify
* **Endpoint**:

  * `POST /webhooks/momo`: Nhận phản hồi thanh toán Momo
  * `POST /webhooks/shopify`: Nhận đơn hàng mới → gửi Gmail xác nhận hoặc kích hoạt thông báo “vừa có người mua hàng”

---

## 🧠 5. **API Hệ Thống Chatbot và Xử Lý Ngôn Ngữ Tiếng Việt**

### Hugging Face Transformers

* **Mục đích**: Xử lý NLP với mô hình PhoBERT và ViT5
* **Ứng dụng**:

  * Sinh văn bản trả lời
  * Tạo embedding để lưu vào vector DB
  * Dùng LoRA để fine-tune với dữ liệu Q\&A về thỏ
* **Tài liệu**: [Huggingface Transformers](https://huggingface.co/docs/transformers)

---

### LangChain API

* **Mục đích**: Dẫn dắt chatbot qua RAG (Retrieval-Augmented Generation)
* **Thành phần chính**:

  * `RetrievalQA`, `ConversationalRetrievalChain`
* **Ứng dụng**: Lưu lịch sử hội thoại, kết hợp sản phẩm Shopify vào câu trả lời.

---

### LlamaIndex API

* **Mục đích**: Index kiến thức về thỏ và sản phẩm để trả lời theo ngữ cảnh
* **Thành phần chính**:

  * `VectorStoreIndex`, `QueryEngine`

---

### Qdrant / Chroma API

* **Mục đích**: Lưu và tìm kiếm vector embedding nhanh
* **Endpoint**:

  * `POST /collections`
  * `POST /points/search`

---

### ElasticSearch API

* **Mục đích**: Tìm kiếm bài blog hoặc sản phẩm cho chatbot đề xuất
* **Endpoint**:

  * `POST /products/_search`
  * `POST /blogs/_search`

---

### Tesseract OCR (pytesseract)

* **Mục đích**: Đọc text từ ảnh (ví dụ ảnh chụp thông tin trên bao bì)
* **Ứng dụng**: Gửi ảnh → Flask xử lý → chatbot phân tích

---

## 🈶 6. **API Hỗ Trợ Tiếng Việt (VinAI / ViNLP)**

* **Mục đích**: Xử lý ngôn ngữ tiếng Việt sâu hơn cho chatbot
* **Chức năng**:

  * Tách từ (tokenization)
  * Phân tích cảm xúc
* **Ứng dụng**: Tiền xử lý input trước khi đưa vào PhoBERT / ViT5 để hiểu đúng ý người dùng Việt.
* **Nguồn**: [VinAI NLP Tools](https://github.com/vinai)
