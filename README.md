## ChatwithyourPDF
This repository provides a user-friendly Streamlit application that allows you to interact with your PDFs in a conversational manner. Simply upload a PDF document, ask a question about its content, and the app will retrieve relevant passages and generate a response using Google's large language models (LLMs).

Key Features:

PDF Text Extraction: Efficiently extracts text from uploaded PDF files.
Text Chunking: Splits the extracted text into manageable chunks for efficient processing.
Sentence Embeddings: Creates semantic representations of text chunks using a pre-trained sentence transformer model (paraphrase-MiniLM-L6-v2).
Similarity Search: Leverages FAISS to quickly find text chunks most relevant to your question based on their embeddings.
Question Answering: Employs Google's powerful text-BISON-001 LLM model to generate a response that incorporates the retrieved passages and addresses your query.
Streamlit Integration: Offers an intuitive web interface for seamless user interaction.
Getting Started

Prerequisites:

Python 3.x (with required libraries: streamlit, PyPDF2, dotenv, langchain_chroma, langchain_community, sentence-transformers, langchain_google_genai, huggingface-transformers)
Google Cloud Platform (GCP) Project with Text-to-Text Generation (Text-BISON-001) API enabled
A Google API Key for Text-to-Text Generation API
Installation:

Clone this repository: git clone https://github.com/<your-username>/your-repo-name.git
Navigate to the repository directory: cd your-repo-name
Create a virtual environment (recommended) and activate it.
Install required libraries: pip install -r requirements.txt (assuming a requirements.txt file is present)
Configuration:

Create a .env file in the root directory of the project:
GOOGLE_API_KEY=<your_google_api_key>
Replace <your_google_api_key> with your actual Google API key for Text-to-Text Generation.
Running the App:

Start the Streamlit application: streamlit run app.py (assuming the main script is named app.py)
Usage:

Open http://localhost:8501/ in your web browser.
Upload your PDF document.
Type your question in the text box.
Click "Ask a question about your PDF:" or press Enter.
The app will process your request and display the LLM-generated response that summarizes relevant information from the PDF in relation to your question.
Additional Notes:

Consider error handling and user feedback mechanisms for a more robust and interactive experience.
Explore customizing the LLM model used for response generation based on your specific needs.
For production deployment, consult Streamlit's documentation on deployment options.
License:

This repository is licensed under the MIT License (see the LICENSE file for details).
