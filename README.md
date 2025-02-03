# blog-generator-using-llama2
## Installation & Setup
- Clone this repository
    Using HTTPS:
    ```bash
    git clone https://github.com/kpiyush25/blog-generator-using-llama2.git
    ```
    or using SSH:
    ```bash
    git clone git@github.com:kpiyush25/blog-generator-using-llama2.git
    ```
- Download an actual Llama2 chat model and replace `replace_this_with_actual_model.bin` with it inside models/ directory
    - I used `llama-2-7b-chat.ggmlv3.q2_K.bin` model from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- Navigate to the project root:
    ```bash
    cd blog-generator-using-llama2
    ```
- Create a virtual environment (You can use Conda as well)
    ```bash
    python3 -m venv llama_venv
    ```
- Activate your virtual environment:
    ```bash
    source llama_venv/Scripts/activate
    ```
- Install the dependencies mentioned in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Instructions to run
- Activate your virtual environment:
    ```bash
    source llama_venv/Scripts/activate
    ```
- Run the app using `streamlit`:
    ```bash
    streamlit run blog_generator_app.py
    ```
- Go to your localhost:8501 (Streamlit uses port 8501 by default if its available; You can see the exact localhost url in your terminal output)
- Use the UI to generate your blogs
- Deactivate the virtual environment after use:
    ```bash
    deactivate
    ```
