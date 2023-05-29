################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  27-May-2023               ####
#### Modified On: 28-May-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the template for    ####
#### OpenAI prompts to get the correct      ####
#### response.                              ####
####                                        ####
################################################

# Template to use for the system message prompt
templateVal_1 = """
    You are a helpful assistant that that can answer questions about youtube videos
    based on the video's transcript: {docs}

    Only use the factual information from the transcript to answer the question.

    If you feel like you don't have enough information to answer the question, say "I don't know".

    Your answers should be verbose and detailed.
    """
