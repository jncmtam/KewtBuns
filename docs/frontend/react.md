# ⚛️ React + TypeScript Cheatsheet (Full)

Một tổng hợp đầy đủ mọi thứ bạn cần biết khi học React với TypeScript, có ví dụ minh họa và giải thích từng phần, cực phù hợp để tham khảo khi code.

---

## 🔰 1. **Khởi động dự án**

```bash
npx create-react-app my-app --template typescript
```

Tạo dự án React + TypeScript template.

---

## 📁 2. **Cấu trúc file cơ bản**

```txt
src/
├── components/
│   └── MyComponent.tsx
├── App.tsx
├── index.tsx
└── types/
    └── global.d.ts
```

Tách components, types, hooks rõ ràng giúp dễ quản lý.

---

## 🧱 3. **Functional Component với Props**

```tsx
// Greeting.tsx
import React from 'react';

type Props = {
  name: string;
  age?: number; // optional
};

const Greeting: React.FC<Props> = ({ name, age }) => (
  <h1>Hello {name} {age && `- ${age} years old`}</h1>
);

export default Greeting;
```

---

## 📦 4. **useState với kiểu dữ liệu**

```tsx
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<{ name: string; email: string } | null>(null);
```

---

## 🔁 5. **useEffect với kiểm soát dependency**

```tsx
useEffect(() => {
  console.log('Component mounted or count changed');
}, [count]);
```

---

## 🧩 6. **useRef với TypeScript**

```tsx
const inputRef = useRef<HTMLInputElement>(null);

const handleFocus = () => {
  inputRef.current?.focus();
};
```

---

## 🧑‍🤝‍🧑 7. **Lifting State Up**

```tsx
// Parent.tsx
const [selected, setSelected] = useState<string>('');
<Child onChange={setSelected} />

// Child.tsx
const Child = ({ onChange }: { onChange: (value: string) => void }) => (
  <button onClick={() => onChange('Hello')}>Click me</button>
);
```

---

## 🛠 8. **Custom Hook với kiểu dữ liệu**

```tsx
function useCounter(initial: number = 0) {
  const [value, setValue] = useState<number>(initial);
  const increment = () => setValue((v) => v + 1);
  return { value, increment };
}
```

---

## 🧾 9. **Event typing**

```tsx
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  console.log(e.target.value);
};

const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  console.log('Clicked');
};
```

---

## 🧱 10. **Conditional rendering với TS**

```tsx
{isLoggedIn ? <Dashboard /> : <Login />}
```

---

## 🧪 11. **Typing API response**

```tsx
type User = {
  id: number;
  name: string;
};

const fetchUser = async (): Promise<User> => {
  const res = await fetch('/api/user');
  return res.json();
};
```

---

## 🧭 12. **React Router với TS**

```tsx
import { BrowserRouter, Route, Routes } from 'react-router-dom';

<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>
```

---

## 🧼 13. **DefaultProps & Component với children**

```tsx
interface BoxProps {
  children: React.ReactNode;
  border?: boolean;
}

const Box = ({ children, border = false }: BoxProps) => (
  <div className={border ? 'border' : ''}>{children}</div>
);
```

---

## 🧱 14. **Component Patterns cần biết**

* Presentational vs Container component
* Compound Components
* Render Props (ít dùng, nhưng nên biết)
* Controlled vs Uncontrolled inputs
* Form validation (React Hook Form)

---

## ✅ 15. **Testing (cơ bản)**

```tsx
// __tests__/Button.test.tsx
import { render, screen } from '@testing-library/react';
import Button from '../Button';

test('renders with text', () => {
  render(<Button>Click Me</Button>);
  expect(screen.getByText('Click Me')).toBeInTheDocument();
});
```

---

## 🧠 16. **Tips & Best Practices**

* Luôn định nghĩa type cho props và state rõ ràng
* Tránh any nếu có thể
* Sử dụng `React.FC<Props>` để có type cho children sẵn
* Sử dụng ESLint + Prettier + TypeScript config riêng
* Dùng Tailwind, Shadcn UI hoặc Radix UI cho style tốt hơn

---

## 📚 Tài liệu gợi ý

* [TypeScript-React Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
* [React Docs](https://react.dev)
* [usehooks-ts](https://usehooks-ts.com/) – rất gọn và chuẩn

---

Nếu bạn dùng VS Code, nên cài:

* Tailwind IntelliSense
* ES7+ React snippets
* Prettier
* TypeScript Hero

Done ✅
