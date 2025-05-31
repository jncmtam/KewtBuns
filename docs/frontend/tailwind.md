# 🌀 Tailwind CSS Cheatsheet (Full)

A complete reference for Tailwind utility classes, organized by category.

---

## 🎨 Color

| Class Type          | Example                  | Description                     |
|---------------------|--------------------------|---------------------------------|
| `text-{color}-{n}`  | `text-gray-800`          | Text color                      |
| `bg-{color}-{n}`    | `bg-blue-500`            | Background color                |
| `border-{color}-{n}`| `border-red-300`         | Border color                    |
| `hover:bg-*`        | `hover:bg-green-600`     | Hover background color          |
| `ring-*`            | `ring-indigo-500`        | Outline ring color              |

---

## 📐 Spacing – Margin & Padding

| Class     | Description                       |
|-----------|-----------------------------------|
| `m-4`     | Margin all sides (1rem)           |
| `mt-2`    | Margin top                        |
| `mb-8`    | Margin bottom                     |
| `mx-4`    | Margin left & right               |
| `my-2`    | Margin top & bottom               |
| `p-4`     | Padding all sides                 |
| `px-6`    | Padding left & right              |
| `py-2`    | Padding top & bottom              |

🔢 Common values: `0`, `1`, `2`, `3`, `4`, `6`, `8`, `10`, `12`, `16`, `20`, `24`, `32`, `40`

---

## 📦 Width & Height

| Class     | Description                       |
|-----------|-----------------------------------|
| `w-4`, `h-4`     | Width/Height (1rem)        |
| `w-full`         | Full width                 |
| `h-screen`       | Full screen height         |
| `max-w-sm`       | Max width (e.g. 640px)     |
| `min-h-[300px]`  | Custom min-height          |
| `aspect-video`   | Maintain 16:9 ratio        |

---

## 🧱 Border & Radius

| Class             | Description                     |
|------------------|----------------------------------|
| `border`          | Default 1px border              |
| `border-2`        | Thicker border                  |
| `border-gray-300` | Border color                    |
| `rounded`         | Default border-radius           |
| `rounded-md`      | Medium radius                   |
| `rounded-xl`      | Extra-large radius              |
| `rounded-full`    | Circle/Full pill                |

---

## 🧑‍🎨 Typography

| Class             | Description                     |
|------------------|----------------------------------|
| `text-sm`, `text-xl`, `text-2xl` | Font sizes      |
| `font-light`, `font-medium`, `font-bold` | Font weight |
| `text-center`, `text-left`, `text-right` | Text align |
| `leading-tight`, `leading-loose` | Line height     |
| `tracking-wide`, `tracking-tight` | Letter spacing |
| `truncate`        | One-line cut with ellipsis      |

---

## 📐 Layout – Flexbox

| Class             | Description                     |
|------------------|----------------------------------|
| `flex`            | Enable flex                     |
| `flex-row`, `flex-col` | Direction                  |
| `items-center`    | Align items vertically          |
| `justify-between`, `justify-center` | Align horizontally |
| `gap-4`           | Gap between items               |

---

## 🔳 Layout – Grid

| Class             | Description                     |
|------------------|----------------------------------|
| `grid`            | Enable grid layout              |
| `grid-cols-2`     | 2 columns                       |
| `grid-cols-12`    | 12 columns                      |
| `gap-4`           | Grid gap                        |
| `place-items-center` | Center content               |

---

## 🧭 Positioning & Display

| Class             | Description                     |
|------------------|----------------------------------|
| `relative`, `absolute`, `fixed`, `sticky` | Position |
| `top-0`, `bottom-4`, `left-2`, `right-4` | Offsets   |
| `z-10`, `z-50`     | Z-index                        |
| `hidden`, `block`, `inline-block`, `inline` | Display |
| `overflow-hidden`, `overflow-scroll` | Scroll behavior |

---

## 🌀 Effects – Hover, Focus, Transition

| Class             | Description                     |
|------------------|----------------------------------|
| `hover:bg-blue-600` | Change bg on hover           |
| `hover:scale-105`    | Scale on hover              |
| `transition`         | Enable transition           |
| `duration-300`       | Duration in ms              |
| `ease-in-out`        | Easing function             |
| `ring-2`, `ring-offset-2` | Focus ring             |

---

## 🧼 Shadows

| Class             | Description                     |
|------------------|----------------------------------|
| `shadow`          | Small shadow                    |
| `shadow-md`       | Medium shadow                   |
| `shadow-lg`       | Large shadow                    |
| `hover:shadow-xl` | Shadow on hover                 |

---

## 📱 Responsive Prefixes

| Prefix | Min Width (px) | Usage Example             |
|--------|----------------|---------------------------|
| `sm:`  | 640            | `sm:text-sm`              |
| `md:`  | 768            | `md:px-4`                 |
| `lg:`  | 1024           | `lg:grid-cols-3`          |
| `xl:`  | 1280           | `xl:gap-6`                |
| `2xl:` | 1536           | `2xl:text-2xl`            |

📌 *Tailwind classes stack. Mobile-first by default.*

---

## 🌙 Dark Mode (if enabled)

```html
<div class="bg-white text-black dark:bg-black dark:text-white">
  Theme changes based on mode
</div>
