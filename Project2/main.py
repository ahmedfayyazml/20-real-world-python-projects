from dotenv import load_dotenv
import os
import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=gemini_key
)

system_prompt = """
You are Einstein...
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ]
)

chain = prompt | llm | StrOutputParser()


def chat(user_input, history):
    history = history or []
    langchain_history = []

    # Convert flat Gradio messages → LangChain messages
    for msg in history:
        if msg["role"] == "user":
            langchain_history.append(HumanMessage(content=msg["content"]))
        else:
            langchain_history.append(AIMessage(content=msg["content"]))

    # Generate LLM response
    response = chain.invoke({"input": user_input, "history": langchain_history})

    # Return flat list of dict messages
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response})

    return "", history


# UI
page = gr.Blocks()

with page:
    gr.Markdown("# Chat with Einstein")

    chatbot = gr.Chatbot()  # no type=

    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: ("", []), None, [msg, chatbot])

page.launch(share=True)
