from dotenv import load_dotenv
import  os
import  gradio as gr
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key = gemini_key
)

system_prompt = """
    You are Einstein.
    Answer questions through Einstein's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life
    even when the user don't ask for it. For example, if the user asks about the theory of
    relativity, you will share your personal experiences with it and not only explain the theory.
    Answer in 2 to 6 sentences
"""

prompt = ChatPromptTemplate.from_messages([("system", system_prompt), (MessagesPlaceholder(variable_name="history")),("user", "{input}")])
chain = prompt | llm | StrOutputParser()


history = []
while True:
    user_input = input("You : ")
    if user_input=="exit":
        break
    history.append( {"role": "user", "content": user_input})
    response = chain.invoke({"input":user_input,"history": history})
    print(f"Albert : {response}")
    history.append({"role":"assistant","content": response})
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))
page = gr.Blocks(
    title="Chat with Einstein",
)
with page:
    gr.Markdown(
        """
        #Chat with Einstein
        Wellcome to Your Personal conversation with Albert Einstein
        """
    )
    chatbot = gr.Chatbot()

    msg = gr.Textbox()

    clear = gr.Button()

page.launch(share=True)