import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
  // Load environment variables based on the mode (development, production, etc.)
  const env = loadEnv(mode, process.cwd());

  return {
    plugins: [react()],
    define: {
      'process.env.VITE_SERVER_URL': JSON.stringify(env.VITE_SERVER_URL || ''),
      
    },
    build: {
      rollupOptions: {
        // Exclude jsPDF from the bundle
        external: ['jspdf']
      }
    }
  };
});