from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()

from models.schema import ResumeMatch
from utils.prompt import SYSTEM_PROMPT

parser = PydanticOutputParser(pydantic_object=ResumeMatch)

chat_model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def analyze_resume(resume_text: str, jd_text: str) -> ResumeMatch:
    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT + parser.get_format_instructions()
        ),
        HumanMessage(
            content=f"""
Resume:
{resume_text}

Job Description:
{jd_text}
"""
        )
    ]

    response = chat_model.invoke(messages)
    return parser.parse(response.content)