## 🧱 1. Kỹ năng lập trình phần mềm

### ✅ Frontend (React, Tailwind, TypeScript)

#### **React:**

* **Cần học:**

  * Tư duy "chia nhỏ giao diện thành các component".

    * Ví dụ: một trang sản phẩm có `ProductCard`, `CartButton`, `ReviewList`,...
  * Quản lý trạng thái: học `useState`, `useContext`, hoặc Zustand.
  * Routing: dùng `React Router` cho các trang như `/san-pham`, `/gio-hang`, `/bai-viet`.

* **Ví dụ thực hành:**

  * Tạo trang sản phẩm với nút "Thêm vào giỏ hàng", khi bấm thì hiện số lượng trong giỏ.

#### **Tailwind CSS:**

* **Cần học:**

  * Dùng class tiện ích như `flex`, `grid`, `text-lg`, `bg-pink-100` để thiết kế đẹp nhanh.
  * Tùy chỉnh giao diện với `tailwind.config.js`: chỉnh màu thương hiệu, font chữ,...

* **Ví dụ:**

  * Tạo card giới thiệu thỏ: hình ảnh + tên + giá + hiệu ứng hover.

#### **TypeScript:**

* **Cần học:**

  * Khai báo kiểu cho props, API response.
  * Tránh lỗi runtime bằng cách “gõ cứng” dữ liệu.

* **Ví dụ:**

  * Tạo interface `Product` gồm: `id`, `name`, `price`, `image`.

---

### ✅ Shopify Storefront API

* **Cần học:**

  * Làm quen với GraphQL: viết query để lấy danh sách sản phẩm, chi tiết đơn hàng,...
  * Tích hợp giỏ hàng và thanh toán bằng API của Shopify.

* **Ví dụ:**

  * Gửi GraphQL query để lấy 10 sản phẩm mới nhất và hiển thị lên trang chủ.

---

### ✅ Backend (Flask + Postgres + Docker)

#### **Flask:**

* **Cần học:**

  * Tạo REST API: ví dụ như `/api/chatbot` để gọi chatbot.
  * Bảo mật cơ bản với JWT.
* **Ví dụ:**

  * API `/api/order-status` cho admin kiểm tra tình trạng đơn hàng.

#### **Postgres:**

* **Cần học:**

  * Thiết kế bảng dữ liệu: đơn hàng, bài viết, log chat,...
  * Dùng SQLAlchemy để thao tác database dễ hơn.

* **Ví dụ:**

  * Tạo bảng `orders` gồm `id`, `product_id`, `status`, `created_at`.

#### **Docker:**

* **Cần học:**

  * Tạo Dockerfile cho Flask và Postgres.
  * Dùng Docker Compose chạy cả 2 service cùng lúc.

* **Ví dụ:**

  * Một lệnh `docker-compose up` sẽ chạy web server Flask + Postgres + chatbot cùng lúc.

---

### ✅ Tích hợp thanh toán

* **Cần học:**

  * Tích hợp Momo bằng SDK Python.
  * Xử lý webhook: khi Momo báo thanh toán thành công, lưu vào Postgres.

* **Ví dụ:**

  * Người dùng thanh toán qua Momo -> webhook gọi Flask -> cập nhật đơn hàng thành "đã thanh toán".

---

### ✅ Triển khai (Deploy)

* **Cần học:**

  * Deploy Flask lên Heroku/DigitalOcean.
  * Đảm bảo HTTPS (SSL) để bảo mật giao dịch.

---

## 🤖 2. Kỹ năng làm Chatbot

### ✅ Kiến thức nền tảng

* **Cần học:**

  * Mô hình Transformer là gì (cơ bản).
  * Biết sơ về PhoBERT, ViT5, cách chúng xử lý tiếng Việt.

* **Ví dụ:**

  * Chatbot biết trả lời “Thỏ Holland Lop có hiền không?” bằng tiếng Việt tự nhiên.

---

### ✅ Fine-tune PhoBERT

* **Cần học:**

  * Dùng Hugging Face để fine-tune PhoBERT với dữ liệu hỏi đáp riêng về thỏ.
  * Dùng kỹ thuật LoRA để tiết kiệm GPU khi fine-tune.

* **Ví dụ:**

  * Bạn tạo 1000 câu hỏi như “Thỏ ăn gì?”, “Bao lâu thì vệ sinh chuồng?” rồi fine-tune thành chatbot.

---

### ✅ RAG (Retrieval-Augmented Generation)

* **Cần học:**

  * Dùng LangChain hoặc LlamaIndex để kết hợp "tìm kiếm + sinh câu".
  * Lưu thông tin về sản phẩm, blog dưới dạng vector.

* **Ví dụ:**

  * Khi người dùng hỏi “Thỏ mini giá bao nhiêu?”, chatbot tìm câu trả lời từ dữ liệu thật thay vì đoán bừa.

---

### ✅ RLHF (Tăng chất lượng chatbot bằng đánh giá người dùng)

* **Cần học:**

  * Dùng phản hồi người dùng để cải thiện chatbot.
  * Ghi lại câu hỏi - câu trả lời và đánh giá 1–5 sao.

* **Ví dụ:**

  * Người dùng thấy chatbot trả lời không đúng -> bạn dùng dữ liệu này để cải thiện bằng RLHF.

---

### ✅ Cơ sở dữ liệu vector và tìm kiếm

* **Cần học:**

  * Dùng FAISS, Qdrant hoặc Chroma để tìm kiếm câu trả lời tương đồng.
  * Dùng ElasticSearch để tìm bài viết blog.

* **Ví dụ:**

  * Người dùng gõ “Cách chăm thỏ con”, chatbot tìm blog liên quan để gợi ý.

---

### ✅ Tích hợp chatbot vào website

* **Cần học:**

  * Tạo endpoint Flask: `/api/chat` nhận câu hỏi, trả lời bằng chatbot.
  * Tạo React component cho cửa sổ chat thân thiện.

* **Ví dụ:**

  * Một ô chat góc phải website, khi khách hỏi “Ship toàn quốc không?”, chatbot trả lời tức thì.

---

## 📅 3. Lộ trình học (Gợi ý)

| Giai đoạn | Thời gian   | Mục tiêu                                                   |
| --------- | ----------- | ---------------------------------------------------------- |
| Tháng 1-2 | 20-30h/tuần | Học frontend (React, Tailwind, Shopify API), làm giao diện |
| Tháng 3   | 20-30h/tuần | Học Flask + Postgres + Docker, tạo API đơn giản            |
| Tháng 4-5 | 20-30h/tuần | Làm chatbot PhoBERT, fine-tune với dữ liệu riêng           |
| Tháng 6   | 20-30h/tuần | Tích hợp chatbot + vector search + RAG                     |
| Tháng 7   | 20-30h/tuần | Triển khai toàn bộ, mời bạn bè test dùng                   |

---

## 📚 Nguồn học uy tín

* **React, Flask, Docker:**

  * FreeCodeCamp, YouTube: TechWorld with Nana, Fireship
* **AI/NLP:**

  * Hugging Face course (huggingface.co/learn)
  * Tài liệu PhoBERT/ViT5 từ VinAI
* **Shopify API:**

  * shopify.dev
* **Cộng đồng:**

  * Hugging Face Discord, Cộng đồng VinAI, Facebook NLP Vietnam
