import gradio as gr
from markitdown import MarkItDown

md = MarkItDown()

def convert_file_to_md(files):
    """
    接收多個 Gradio File 物件，轉換為 Markdown 文字。
    files 可能是 None（未上傳）、單一檔案物件（取決於 Gradio 版本），或是檔案物件列表。
    """
    if not files:
        return "⚠️ 未收到檔案，請重新上傳。"
        
    # 確保 files 是個列表
    if not isinstance(files, list):
        files = [files]

    combined_content = []
    
    for file in files:
        try:
            # 取出檔名標題
            filename = file.name if hasattr(file, 'name') else str(file)
            import os
            basename = os.path.basename(filename)
            
            combined_content.append(f"# 📄 檔案：{basename}\n")
            
            # 轉換
            result = md.convert(filename)
            content = result.text_content or ""
            
            if not content.strip():
                combined_content.append("ℹ️ 轉換完成，但沒有可顯示的 Markdown 內容。\n")
            else:
                combined_content.append(content)
                
        except Exception as e:
            combined_content.append(f"❌ 轉換失敗：{str(e)}\n")
            
        combined_content.append("\n" + "="*40 + "\n\n")

    return "".join(combined_content)


with gr.Blocks(title="📄 MarkItDown 文件轉 Markdown 線上工具") as demo:
    
    gr.Markdown("""
    # 📄 any Docs 轉 MD Markdown ( David888.com )
    上傳支援格式檔案，系統會自動轉換為 Markdown 純文字內容。
    """)
    
    file_input = gr.File(
        label="📁 請將檔案拖曳到此區域，或點擊選擇多個檔案",
        file_count="multiple",
        type="filepath",
        file_types=[".txt", ".md", ".html", ".csv", ".json", ".xml", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", "image", "audio"],
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
    
    # 拖曳上傳或選擇檔案時自動觸發轉換 (change 包含上傳與清除)
    file_input.change(convert_file_to_md, inputs=file_input, outputs=output)


if __name__ == "__main__":
    demo.launch()