from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv 
from crewai import LLM

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.7
)

class CustomerServiceCrew:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )
    
    def create_agents(self):
        # Customer Service Agent
        customer_service = Agent(
            role='Customer Service Representative',
            goal='Provide helpful and empathetic customer support',
            backstory="""Expert customer service representative with years of experience 
                      handling customer inquiries and providing solutions. Known for 
                      clear communication and problem-solving abilities.""",
            llm=self.llm
        )
        
        # Technical Support Agent
        technical_support = Agent(
            role='Technical Support Specialist',
            goal='Resolve technical issues and provide clear explanations',
            backstory="""Experienced technical support specialist with deep knowledge 
                      of systems and troubleshooting. Skilled at explaining complex 
                      concepts in simple terms.""",
            llm=self.llm
        )
        
        # Quality Assurance Agent
        qa_agent = Agent(
            role='Response Quality Specialist',
            goal='Ensure responses are professional, helpful, and complete',
            backstory="""Quality assurance expert who reviews and refines customer 
                      service responses to ensure they meet highest standards of 
                      clarity and helpfulness.""",
            llm=self.llm
        )
        
        return customer_service, technical_support, qa_agent
    
    def create_tasks(self, customer_message, agents):
        customer_service, technical_support, qa_agent = agents
        
        # Initial response task
        initial_response = Task(
            description=f"""Review this customer message and prepare an initial response:
                         {customer_message}
                         Consider tone, urgency, and customer needs.""",
            agent=customer_service
        )
        
        # Technical review task
        technical_review = Task(
            description="""Review the initial response and add any necessary technical 
                        details or corrections. Ensure accuracy of information.""",
            agent=technical_support
        )
        
        # Final quality check task
        quality_check = Task(
            description="""Review and refine the response. Ensure it is professional, 
                        clear, and addresses all customer concerns. Format for natural 
                        text-to-speech delivery.""",
            agent=qa_agent
        )
        
        return [initial_response, technical_review, quality_check]
    
    def process_message(self, customer_message):
        agents = self.create_agents()
        tasks = self.create_tasks(customer_message, agents)
        
        crew = Crew(
            agents=list(agents),
            tasks=tasks,
            verbose=True
        )
        
        result = crew.kickoff()
        return result 