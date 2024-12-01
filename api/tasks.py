from crewai import Task
from textwrap import dedent


class AnalysisTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def collect_data(self, agent, user_posts):
        return Task(
            description=dedent(
                f"""
                    **Task**: Analyze and Find Sentiment on User Posts
                    **Description**: Perform a detailed analysis of user posts to identify the primary topics of discussion, with a focus on companies mentioned.
                        Extract the sentiment expressed by the user about each company, using a scoring system from 0 to 10 (0 being negative, 10 being highly positive).
                        Summarize the findings in a structured format, clearly indicating:
                        1. The company the user talks about the most.
                        2. The overall sentiment score for that company.

                        Ensure accuracy and clarity in the sentiment analysis, and use a professional tone in your output.

                    **Parameters**:
                    - **User Posts**: {user_posts}

                    **Output**:
                    - A structured summary including:
                    - The company most discussed by the user.
                    - The sentiment score for the most-discussed company.

                    **Additional Notes**:
                    - Focus on extracting actionable insights from user posts.
                    - Use reliable methods or tools for sentiment analysis.
                    - Ensure all output is clear, concise, and easy to understand.


                    **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )

    def create_json(self, agent):
        return Task(
            description=dedent(
                f"""
                **Task**: Generate JSON Data
                **Description**: Create a structured JSON file based on the provided data.
                    The JSON file should include two key parameters:
                    - "company": The company being mentioned in the data.
                    - "sentiment": A numeric sentiment score from 0 to 10 representing the sentiment towards the company
                    (0 being negative, 10 being highly positive).

                    Ensure the JSON file is well-structured, easy to read, and accurately reflects the input data.
                    Follow proper formatting conventions for JSON creation.

                **Parameters**:
                - none

                **Output**:
                - A JSON file containing the "company" and "sentiment" fields, formatted as:
                ```
                [

                    "company": "<company_name>",
                    "sentiment": "<sentiment_score>",
                    ...
                ]
                ```

                **Additional Notes**:
                - Ensure the data integrity is maintained during JSON generation.
                - Validate the JSON for proper syntax and completeness.
                - Focus on making the JSON file both human-readable and machine-parsable.
                """
            ),
            agent=agent,
        )
