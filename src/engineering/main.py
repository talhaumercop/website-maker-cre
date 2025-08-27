#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
import gradio as gr
from engineering.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
os.makedirs('output', exist_ok=True)

def run_task(input_command, project_description):
    """
    Executes the EngineeringTeam crew with given inputs.
    """
    inputs = {
        "input": input_command,
        "project": project_description
    }
    try:
        result = EngineeringTeam().crew().kickoff(inputs=inputs)
        return f"✅ Task Completed Successfully!\n\nResult:\n{result}"
    except Exception as e:
        return f"❌ Error: {e}"

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown(
        """
        # 🚀 AI-Powered Engineering Crew
        **Generate React Projects with Vite using AI**
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ Configure Your Project")
            input_command = gr.Textbox(label="Terminal Command", value="npm create vite@latest my-app -- --template react")
            project_description = gr.Textbox(label="Project Description", placeholder="Describe your project, e.g., Responsive Dark Mode Landing Page")

            run_button = gr.Button("Run Project", variant="primary")
        
        with gr.Column(scale=1):
            gr.Markdown("### ✅ Output")
            output_box = gr.Textbox(label="Result", lines=20)

    run_button.click(run_task, inputs=[input_command, project_description], outputs=[output_box])

demo.launch()
################################################################################
# def run():
#     """ Run the crew. """
#     # Start the AI team 
#     inputs = {
#         "project": "I want three tasks one to write html for navbar, other to write header section, and one two write footer. they all should output a html file"
#     }
#     try:
#         EngineeringTeam().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """ Train the crew for a given number of iterations. """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         Engineering().crew().train(
#             n_iterations=int(sys.argv[1]),
#             filename=sys.argv[2],
#             inputs=inputs
#         )
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")


# def replay():
#     """ Replay the crew execution from a specific task. """
#     try:
#         Engineering().crew().replay(task_id=sys.argv[1])
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")


# def test():
#     """ Test the crew execution and returns the results. """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#     try:
#         Engineering().crew().test(
#             n_iterations=int(sys.argv[1]),
#             eval_llm=sys.argv[2],
#             inputs=inputs
#         )
#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")


