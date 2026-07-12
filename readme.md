#Follow the following instructions for doing project changed -- version 2

1. Create a Python Virtual Env from root directory 
python -m venv venv
2. Activate it 
source venv/bin/activate

3. Intall dependencies
pip install -r requirements.txt

4. Set up open API Key from termial
set OPENAPI_API_KEY=<your-api-key>
ollama Pull model quen2.5:7b

5. Run the DB Files to create the DB locally
python -m db.create_and_write_in_product_db
python -m db.create_memory_db

6. Running the Streamlit Application 
