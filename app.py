import gradio as gr
from markitdown import MarkItDown

md = MarkItDown()

def convert_file_to_md(file):
    """
    接收 Gradio File 物件，轉換為 Markdown 文字。
    file 可能是 None（未上傳）或檔案物件。
    """
    if file is None:
        return "⚠️ 未收到檔案，請重新上傳。"

    try:
        # file 是 Gradio File 物件，使用 file.name 取得檔案路徑
        result = md.convert(file.name if hasattr(file, 'name') else file)
        content = result.text_content or ""
    except Exception as e:
        content = f"❌ 轉換失敗：{str(e)}"

    if not content.strip():
        return "ℹ️ 轉換完成，但沒有可顯示的 Markdown 內容。"

    return content


with gr.Blocks(title="📄 MarkItDown 文件轉 Markdown 線上工具") as demo:
    
    gr.Markdown("""
    # 📄 any Docs 轉 MD Markdown ( David888.com )
    上傳支援格式檔案，系統會自動轉換為 Markdown 純文字內容。
    """)
    
    file_input = gr.File(
        label="📁 請將檔案拖曳到此區域，或點擊選擇檔案",
        file_count="single",
        type="filepath",
        height=150,
    )
    
    gr.Markdown("### 轉換結果")
    
    output = gr.Code(
        label="",
        value="",
        language="markdown",
        lines=25,
        show_label=False,
    )
    
    # 拖曳上傳或選擇檔案時自動觸發轉換
    file_input.change(convert_file_to_md, inputs=file_input, outputs=output)
    file_input.upload(convert_file_to_md, inputs=file_input, outputs=output)


if __name__ == "__main__":
    demo.launch()