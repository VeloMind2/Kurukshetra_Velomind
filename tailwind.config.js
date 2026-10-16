/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#04070D',
          900: '#080D18', // main background
          850: '#0D1527', // card background
          800: '#111B2D', // secondary surface
          700: '#182640',
          600: '#1E2F4F',
          500: '#2A4068',
        },
        cyan: {
          accent: '#56E5F2', // electric cyan
          glow: 'rgba(86, 229, 242, 0.25)',
          muted: '#207F8A',
        },
        violet: {
          accent: '#8B7CFF', // secondary accent
          glow: 'rgba(139, 124, 255, 0.25)',
          muted: '#584BA3',
        },
        mint: {
          accent: '#63E6BE', // success
          glow: 'rgba(99, 230, 190, 0.25)',
        },
        amber: {
          accent: '#FFC76A', // warning
          glow: 'rgba(255, 199, 106, 0.25)',
        },
        border: {
          subtle: '#1C2942',
          glow: 'rgba(86, 229, 242, 0.3)',
        },
        text: {
          main: '#F4F7FC',
          muted: '#A3B0C5',
          faint: '#65758E',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Consolas', 'monospace'],
      },
      boxShadow: {
        'glow-cyan': '0 0 25px -5px rgba(86, 229, 242, 0.35)',
        'glow-violet': '0 0 25px -5px rgba(139, 124, 255, 0.35)',
        'glow-mint': '0 0 20px -5px rgba(99, 230, 190, 0.35)',
        'glow-amber': '0 0 20px -5px rgba(255, 199, 106, 0.35)',
        'panel': '0 8px 32px 0 rgba(0, 0, 0, 0.45)',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        }
      }
    },
  },
  plugins: [],
}
