from crewai import Crew
from textwrap import dedent
from agents import AnalysisAgents
from tasks import AnalysisTasks
import json
from dotenv import load_dotenv
from flask import jsonify, Flask, request
load_dotenv()

app = Flask(__name__)


class AnalysisCrew:
    def __init__(self, posts):
        self.posts = posts

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = AnalysisAgents()
        tasks = AnalysisTasks()

        # Define your custom agents and tasks here
        user_sentiment_agent = agents.user_sentiment_analyzer_agent()
        json_data_agent = agents.json_data_generator_agent()

        # Custom tasks include agent name and variables as input
        collect_data = tasks.collect_data(
            agent=user_sentiment_agent,
            user_posts=self.posts
        )

        create_json = tasks.create_json(
            agent=json_data_agent,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[user_sentiment_agent,
                    json_data_agent
                    ],
            tasks=[
                collect_data,
                create_json
            ],
            verbose=False,
        )

        result = crew.kickoff()
        return result


@app.route("/analyze", methods=["POST"])
def analyze():
    post = request.json
    analysis_crew = AnalysisCrew(posts=post)
    result = analysis_crew.run().replace('`', '')
    result_json = json.loads(result)
    return jsonify(result_json[0])


@app.route("/", methods=["GET"])
def index():
    return jsonify("send request on analyze route")


if __name__ == "__main__":
    app.run(debug=True)
