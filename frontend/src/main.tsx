import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Editor from './editor.tsx'
import MdLatexTest from './latex_md_test.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    <Editor />
    {/* <MdLatexTest filepath="../local/t.md" /> */}
  </StrictMode>,
)
