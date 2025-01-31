import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# The below method will be used to get the response from the LLama 2 model
def getResponseFromLlama(input_text, number_words, blog_audience):
    # using Llama 2 model below (I assume you have installed this model in your local)
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q2_K.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature':0.01})
    
    # Writing the prompt template below:
    prompt_template = """
                        Write a blog for {blog_audience} on the topic {input_text} within {number_words}.
                        Start the blog by 'Hey, welcome! How are you doing?'
                    """
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
submit = st.button('Generate')

if submit:
    st.write(getResponseFromLlama(input_text, number_words, blog_audience))

