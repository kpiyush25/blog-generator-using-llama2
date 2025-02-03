import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

'''
    - Streamlit is used for creating web apps with minimal effort.
    - PromptTemplate helps structure input prompts for LLMs.
    - CTransformers is used to load and interact with transformer models locally.
'''

# The below method will be used to get the response from the LLama 2 model based on user input.
def getResponseFromLlama(input_text, number_words, blog_audience):
    # Using Llama 2 model below (Assuming you have installed this model locally)

    '''
        CTransformers is a library that loads transformer models efficiently for inference.
    - 'model' specifies the path to the model file.
    - 'model_type' defines the type of model being used (e.g., 'llama').
    - 'config' contains additional parameters such as:
      - 'max_new_tokens': Limits the number of new tokens generated.
      - 'temperature': Controls randomness (lower values make output more deterministic).
    '''
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q2_K.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature':0.01})
    
    # Writing the prompt template below:
    prompt_template = """
                        Write a blog for {blog_audience} on the topic {input_text} within {number_words}.
                        Start the blog by 'Hey, welcome! How are you doing?'
                    """
    # PromptTemplate helps structure the input dynamically based on variables.
    prompt = PromptTemplate(input_variables=["blog_audience", "input_text", "number_words"],
                            template = prompt_template)
    
    # Generating the response using Llama 2 model below:
    response = llm(prompt.format(blog_audience = blog_audience, input_text = input_text, number_words = number_words))
    print(response)
    return response



st.set_page_config(page_title="Generate Blogs using LLama 2",
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs using LLama 2")
input_text = st.text_input("Please enter the blog topic")

# Creating two more columns for two extra input fields
column1, column2 = st.columns([6,6])

with column1:
    number_words = st.text_input('Number of words')
with column2:
    blog_audience = st.selectbox('Write this blog for', 
                                 ('General public', 'Data Scientists', 'Software Engineers'), 
                                 index = 0)
submit = st.button('Generate Blog')

if submit:
    st.write(getResponseFromLlama(input_text, number_words, blog_audience))

