import Markdown from 'react-markdown'
import { useState, useEffect } from 'react'
import rehypeKatex from 'rehype-katex'
import remarkMath from 'remark-math'

const setFile = async (filepath: string) => {
    const response = await fetch(filepath);

    if (response.ok) {
        const text = await response.text();
        return text;
    }

    return response.text();
};

export default function md_latex_component({ filepath }: { filepath: string }) {
    const [text, setText] = useState('');

    useEffect(() => {
        setFile(filepath).then((text) => setText(text)).catch((error) => console.error(error));
    }, [filepath]);

    return (
        <Markdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
            {text}
        </Markdown>
    )
}