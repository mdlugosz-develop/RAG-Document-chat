import gradio as gr
from app.file_processor import process_file
from app.qa_system import answer_question
from app.url_processor import process_url , process_wikipedia# Import the new URL processing function

def create_interface(vector_store, retriever):
    with gr.Blocks(theme="base") as demo:
        file_input = gr.File(label="Upload Document")
        url_input = gr.Textbox(label="Enter WIKI URL")  # Add URL input field
        text_output = gr.Textbox(label="Chunked Text", lines=10)
        question_input = gr.Textbox(label="Ask a Question")
        answer_output = gr.Textbox(label="Answer", lines=2)
        submit_button = gr.Button("Submit")

        file_input.change(fn=lambda file: process_file(file, vector_store), inputs=file_input, outputs=text_output)
        url_input.change(fn=lambda url: process_wikipedia(url, vector_store), inputs=url_input, outputs=text_output)  # Handle URL input
        submit_button.click(fn=lambda question: answer_question(question, retriever), inputs=[question_input], outputs=answer_output)

    return demo