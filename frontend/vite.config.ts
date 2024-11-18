import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';


export default defineConfig(({ mode }) => {


  // Load environment variables based on the mode (development, production, etc.)
  const env = loadEnv(mode, process.cwd());

  return {
    plugins: [react()],
    resolve: {
      alias: {
        // Setting up the alias for the src directory
        '@': path.resolve(__dirname, 'src'), // '@' resolves to the 'src' folder
      },
    },
    define: {
      'process.env.VITE_SERVER_URL': JSON.stringify(env.VITE_SERVER_URL || ''),
    }
  };
});
