from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI


class AnalysisAgents:
    def __init__(self):
        self.OpenAIGPT4mini = ChatOpenAI(
            model_name="gpt-4o-mini", temperature=0.7)  # type: ignore

    def user_sentiment_analyzer_agent(self):
        return Agent(
            role="User Sentiment Analyst",
            backstory=dedent(
                """
                An expert in analyzing user sentiment from textual content.
                Experienced in synthesizing and interpreting information to extract actionable insights about companies.
                Skilled in providing concise summaries based on user feedback and sentiment analysis.
                """
            ),
            goal=dedent(
                """
                Analyze user posts to extract insights about companies mentioned.
                Specifically:
                - Identify the company mentioned most frequently in the posts.
                - Assign a sentiment score from 0 to 10, where 0 indicates very negative sentiment, 
                  and 10 indicates very positive sentiment.
                - Provide a single-line summary of the most frequently mentioned company 
                  and the corresponding sentiment score.
                """
            ),
            verbose=False,
            llm=self.OpenAIGPT4mini,
        )

    def json_data_generator_agent(self):
        return Agent(
            role="JSON Data Generator",
            backstory=dedent(
                """
                A specialist in creating well-structured and easily interpretable JSON files.
                Proficient in organizing data into structured formats for seamless integration and readability.
                Skilled at transforming raw input into actionable, standardized JSON representations.
                """
            ),
            goal=dedent(
                """
                Create a JSON file based on the provided data. The JSON file should:
                - Contain two fields: "company" and "sentiment".
                - The "company" field represents the name of the company mentioned.
                - The "sentiment" field represents the sentiment score (an integer between 0 and 10) 
                  reflecting the user's sentiment towards the company.
                Ensure the JSON is well-formatted and ready for use.
                """
            ),
            verbose=False,
            llm=self.OpenAIGPT4mini,
        )
