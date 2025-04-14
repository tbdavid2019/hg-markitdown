import gradio as gr
from markitdown import MarkItDown
import os
import shutil
from uuid import uuid4

md = MarkItDown()

def convert_file_to_md(file):
    try:
        result = md.convert(file.name)  
        content = result.text_content
    except Exception as e:
        content = f"❌ 轉換失敗：{str(e)}"
    return content

demo = gr.Interface(
    fn=convert_file_to_md,
    inputs=gr.File(label="上傳支援格式檔案（如 PDF、Word、Excel 等）"),
    outputs=gr.Textbox(label="轉換後的 Markdown 結果", lines=25),
    title="📄 MarkItDown 文件轉 Markdown 線上工具",
    description="上傳你的檔案，我們將自動轉換為 Markdown 格式內容，支援 PDF、Word、Excel、PowerPoint、圖片、音訊等格式。",
    allow_flagging="never"  # ← 加這行就不會出現 Flag 按鈕了
)

demo.launch()