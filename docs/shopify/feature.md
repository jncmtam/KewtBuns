# Shopify features
**FOMO** + **High quality products**
```md
- User
    - Product Listings
    - Navigation with categories and filters
    - Blogs
        - Holland Lops informations
        - Cages, Food, Medicine, ...
        -
    - Mutiple payment methods (Momo, Bank, COD,...)
    - Customer reviews and ratings
    - Add to cart (Wishlish/Save for later) + Buy now + Deposit
    - Discount codes/ coupon
    - Order Histories and tracking
    - Announcement Gmails
- Admin
    - Inventory management
    - Order and customer analytics
    - Product & blog management
    - Role-based access (admin, staff, etc.)
```
# Chatbot features
```md
- Virtual Shopping assistants
- Smart chat recommendations, emotions, Holland Lops involed informations 
-> Smart chatbot with smart answer, RLHF
```
# Techstack
### Frontend
```
React
Tailwind
Typescript + PostCSS
```
### Backend
#### Shopify
```
Python (Flask, RestAPI)
Docker - Kubenettes
Postgres
```
#### Chatbot
- Research on this problem to write paper
```
OCR

LLM :
- ViNLP, VNP -> vietnamese token process
- PhoBert, ViT5, VinAI's models
- Global LLM  : LLama3, Grok, Mistral (finetune for Vietnamese)
- RAG : Langchain + Llama Index

Finetune :
- Hugging Face
- LoRA

RLHF:
- HuggingFace TRL, OpenRL
- Human-in-the-loop

VectorDb:
- Qdrandt, Chroma : documents embedding
- FAISS : fast retrieve on vector database

Embedding Model :
- Sentence-BERT, ViT5-embedding

Search Engine :
- Elastic Search
```