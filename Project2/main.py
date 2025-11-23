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
    model="gemini-1.5-flash",
    temperature=0.5,
    google_api_key=gemini_key
)

system_prompt = """
    You are Einstein.
    Answer questions through Einstein's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life
    even when the user don't ask for it. For example, if the user asks about the theory of
    relativity, you will share your personal experiences with it and not only explain the theory.
    Answer in 2 to 6 sentences
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), (MessagesPlaceholder(variable_name="history")), ("user", "{input}")])
chain = prompt | llm | StrOutputParser()


def chat(user_input, history):
    history = history or []
    langchain_history = []

    for user_text, ai_text in history:
        langchain_history.append(HumanMessage(content=user_text))
        langchain_history.append(AIMessage(content=ai_text))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    history.append((user_input, response))

    return "", history


page = gr.Blocks(title="Chat with Einstein")
with page:
    gr.Markdown(
        """
        #Chat with Einstein
        Welcome to Your Personal conversation with Albert Einstein
        """
    )
    chatbot = gr.Chatbot()

    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

clear.click(lambda: (None, []), None, [msg, chatbot])
page.launch(share=True)