import gradio as gr
from markitdown import MarkItDown

md = MarkItDown()

def convert_file_to_md(file_path: str) -> str:
    if not file_path:
        return "⚠️ 未收到檔案，請重新上傳。"

    try:
        result = md.convert(file_path)
        content = result.text_content or ""
    except Exception as e:
        content = f"❌ 轉換失敗：{str(e)}"

    if not content.strip():
        return "ℹ️ 轉換完成，但沒有可顯示的 Markdown 內容。"

    return content


with gr.Blocks(title="📄 MarkItDown 文件轉 Markdown 線上工具") as demo:
    gr.Markdown("""
    ## 📄 MarkItDown 文件轉 Markdown
    上傳支援格式檔案，系統會自動轉換為 Markdown 內容。也可以按下「開始轉換」手動觸發。
    """)

    with gr.Row():
        file_input = gr.File(
            label="拖曳或選擇支援格式檔案（PDF、Word、Excel、PowerPoint、圖片、音訊等）",
            file_count="single",
            type="filepath",
        )
        convert_button = gr.Button("開始轉換", variant="primary")

    gr.Markdown("### 轉換後的 Markdown 結果")
    output = gr.Markdown(
        value="請上傳或轉換檔案，結果將顯示於此。",
        show_copy_button=True,
    )

    file_input.upload(convert_file_to_md, inputs=file_input, outputs=output)
    convert_button.click(convert_file_to_md, inputs=file_input, outputs=output)


if __name__ == "__main__":
    demo.launch()