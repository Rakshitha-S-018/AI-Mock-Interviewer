import gradio as gr

def chatbot(message):
    return f"AI Interviewer: {message}"

demo = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="AI Mock Interviewer"
)

demo.launch()