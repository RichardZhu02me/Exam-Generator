import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Editor from './editor.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    <Editor filepath="../local/t.md" />
  </StrictMode>,
)
