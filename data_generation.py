# Inbuild packages
import os 
import warnings
warnings.filterwarnings("ignore")

# Third party package
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Custom packages
from prompt_template import SUMMARY, QUESTION

# env variables 
load_dotenv()

# add config value
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


################################################################################################

def frontend() :

    # set title
    st.title("Play with parameters : Gemini AI")

    temp_value = st.slider("Select Temperature:", 0.0, 1.0)
    top_p_value = st.slider("Select Top p :", 0.0, 1.0)
    top_k_value = st.slider("Select Top K :", 1, 10)

    # show params info
    info_button = st.button("Parameter Information")
    if info_button :
        st.write("""Temperature : The temperature parameter influences the randomness of the generated responses. 
                 A higher value, such as 0.8, makes the answers more diverse, while a lower value, like 0.2, makes them more focused and deterministic.""")
        
        st.write("""Top P : The top_p parameter, also known as nucleus sampling or "penalty" in the API, controls the diversity and quality of the responses. 
                    It limits the cumulative probability of the most likely tokens. 
                    Higher values like 0.9 allow more tokens, leading to diverse responses, while lower values like 0.2 provide more focused and constrained answers.""")
        
        st.write("Top K : Top K means, Takes into consideration only the top 5 most likely words when determining the next word, fostering diversity in the output.")
        

    # add dropdown list
    category = st.selectbox("Category", ['Summary', "Question"])

    # add text input
    user_input = st.text_area("Enter your text :")

    # submit button 
    submit_button = st.button("Submit")

    if submit_button :

        # select prompt
        prompt = prompts_data(category)
        prompt = prompt.format(user_input)

        # prompt reponse
        prompt_reponse = llm_chat(prompt, 
                                  temp_value, 
                                  top_p_value, 
                                  top_k_value,
                                  )
        
        # show prompt data
        prompt_reponse = f""" Temperature : {temp_value}, Top P : {top_p_value}, Top K : {top_k_value} \n
                             {prompt_reponse}"""
        
        st.write(prompt_reponse)


################################################################################################
    
def llm_chat(text_data: str, 
             temperature : str, 
             top_p : float, 
             top_k : float,
             ) -> str :

    try :
        # defined model
        model = genai.GenerativeModel("gemini-pro")

        # generate text data 
        response = model.generate_content(text_data, 
                                          generation_config = genai.types.GenerationConfig(temperature = temperature, 
                                                                                            top_p = top_p,
                                                                                            top_k = top_k
                                                                                            ))
        # format text data
        response = response.text.replace("**", "") 
        return response


    except :
        return "Please generate new token, your current token is expired..." 
    

################################################################################################

def prompts_data(category: str) -> str :

    if category == "Summary" :
        return SUMMARY
        
    elif category == "Question" :
        return QUESTION
    




# https://codemaker2016.medium.com/build-your-own-chatgpt-using-google-gemini-api-1b079f6a8415