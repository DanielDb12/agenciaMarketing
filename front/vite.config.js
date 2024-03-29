import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
// https://vitejs.dev/config/
export default defineConfig({


  resolve: {
    alias: {
      '@assets': path.resolve(__dirname, './src/assets/'),
      '@hocs': path.resolve(__dirname, './src/hocs'),
      '@container': path.resolve(__dirname, './src/container'),
      '@components': path.resolve(__dirname, './src/components'),
      '@style': path.resolve(__dirname, './src/style'),
      '@redux': path.resolve(__dirname, './src/redux/'),
    }
  },





  plugins: [react()],
})
