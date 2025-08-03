import google.generativeai as genai

genai.configure(api_key="AIzaSyBep74bb3Ou0J9GOihg_hNgViEEDIy86wk")

models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)
