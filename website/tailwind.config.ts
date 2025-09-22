import type { Config } from "tailwindcss";

const config = {
  content: [
    "./app/**/*.{css,js,jsx,ts,tsx}",
    "./components/**/*.{css,js,jsx,ts,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-sans)"],
        mono: ["var(--font-mono)"],
      },
    },
  },
  plugins: [require("tailwindcss-animate"), require("@tailwindcss/typography")],
} satisfies Config;

export default config;
