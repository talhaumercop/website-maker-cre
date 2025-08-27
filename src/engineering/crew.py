import os
from tabnanny import verbose
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from .tools.powershell_commands import PowerShellCommand
# Load environment variables (your API keys)
load_dotenv()

@CrewBase
class EngineeringTeam():
    """Engineering Team Crew"""
    
    # Load agent and task configurations
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def powershell_command_run_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['powershell_command_run_agent'],
            verbose=True,
            tools=[PowerShellCommand()]
        )

    @task
    def powershell_command_task(self) -> Task:
        return Task(
            config=self.tasks_config['powershell_command_task'],
            verbose=True,
            output_file='output/powershell_command_output.txt',
        )
        
    @agent
    def frontend_html_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_html_engineer'],
        )
    
    @agent
    def frontend_css_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_css_engineer'],
        )

    @agent
    def code_checker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_checker_agent'],
        )
        
      
    @task
    def frontend_development_task_html(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_development_task_html'],
            verbose=True,
        )

    @task
    def code_checker_task_html(self) -> Task:
        return Task(
            config=self.tasks_config['code_checker_task_html'],
            verbose=True,
            output_file='my-app/src/App.jsx'
        )
        
    @task
    def frontend_development_task_css(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_development_task_css'],  # Fixed!
            verbose=True,
    )
    
    @task
    def code_checker_task_css(self) -> Task:
        return Task(
            config=self.tasks_config['code_checker_task_css'],
            verbose=True,
            output_file='my-app/src/App.css'
        )
    
########################################################################
    # @agent
    # def dynamic_task_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['dynamic_task_agent'],
    #     )

    # @task
    # def dynamic_task_maker_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['dynamic_task_maker_task'],
    #         verbose=True,
    #         output_file='src/engineering/config/task_dynamic.yaml'
    #     )
##########################################################################
    @crew
    def crew(self) -> Crew:
        """Creates the Engineering Team crew"""
        return Crew(
            agents=self.agents,  # All the AI workers
            tasks=self.tasks,    # All the jobs to do
            process=Process.sequential,  # Do jobs one after another
            verbose=True,        # Show us what's happening
        )
