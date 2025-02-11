from crewai import Crew, Task, Process, Agent, LLM
from crewai.project import CrewBase, agent, crew, task

from tools.pdf_reader import PDF_reader_tool
from tools.store_insight import Store_findings
from crewai_tools import PDFSearchTool

import os
from dotenv import load_dotenv
load_dotenv()


import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = LLM(
    model="gpt-4o-mini",
    temperature=0,
    base_url="https://api.openai.com/v1", 
    # api_key=os.getenv("OPENAI_API_KEY")
)

## Ollama Local
# llm = LLM(
#     # model='ollama/mistral:7b',
#     # # # model='ollama/llama3.1:8b',
#     # # # model='ollama/deepseek-r1:7b',
#     # base_url='http://localhost:11434',

#     temperature=0
# )


@CrewBase
class ResumeCrew:
    """Resume Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # @agent
    # def pdf_rag_agent(self) -> Agent:
    #     return Agent(
    #         llm=llm,
    #         config=self.agents_config['pdf_rag_agent'],
    #         tools=[PDFSearchTool("/Users/minsuplee/Desktop/llmagents/src/JD_analysis/pdfs/Minsup_Lee_Resume_2025_v2.pdf")],
    #         verbose=True,
    #         allow_delegation=False,
    #     )
    
    @agent
    def pdf_reader_agent(self) -> Agent:
        return Agent(
            llm=llm,
            config=self.agents_config['pdf_reader_agent'],
            tools=[PDF_reader_tool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def resume_analyst_agent(self) -> Agent:
        return Agent(
            llm=llm,
            config=self.agents_config['resume_analyst_agent'],
            tools=[Store_findings()],
            verbose=True,
            allow_delegation=False,
        )
    
    # @task
    # def pdf_rag_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['pdf_rag_task'],
    #         agent=self.pdf_rag_agent(),
    #     )
    
    @task
    def pdf_reader_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_reader_task'],
            agent=self.pdf_reader_agent(),
        )
    
    @task
    def resume_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_analyst_task'],
            agent=self.resume_analyst_agent(),
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # llm=llm,
            verbose=True,
            process=Process.sequential,
        )
    
    
    