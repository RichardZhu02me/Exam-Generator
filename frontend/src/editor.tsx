import 'katex/dist/katex.min.css';

import Highlight from '@tiptap/extension-highlight'
import Typography from '@tiptap/extension-typography'
import { EditorContent, useEditor } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'
import { Mathematics, createMathMigrateTransaction } from '@tiptap/extension-mathematics'
import { useEffect, useState } from 'react';
import './editor.css'

const setFile = async (filepath: string) => {
  const response = await fetch(filepath);

  if (response.ok) {
    const text: string = await response.text();
    return text;
  }

  return response.text();
};


export default function Editor({ filepath }: { filepath: string }) {
  const [text, setText] = useState('default_val');

  useEffect(() => {
    setFile(filepath).then((text) => setText(text)).catch((error) => console.error(error));
  }, [filepath])

  const editor = useEditor({
    shouldRerenderOnTransaction: true,
    extensions: [
      Mathematics.configure({
      }),
      StarterKit,
      Highlight,
      Typography,
    ],
    content: text,
    onUpdate: ({ editor }) => {
      console.log("triggered math migration")
      const tr = editor.state.tr
      const updatedTr = createMathMigrateTransaction(editor, tr)
      console.log("triggered math migration")
      editor.view.dispatch(updatedTr)
    },
  })

  useEffect(() => {
    if (editor && text) {
      editor.commands.setContent(text);
    }
  }, [editor, text]);


  return (
    <>
      <EditorContent editor={editor} />
    </>
  )
}
