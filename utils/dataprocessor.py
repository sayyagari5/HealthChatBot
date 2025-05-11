import pandas as pd
 import numpy as np

 def process_user_input(user_input):
 # Simulate dataset for processing
 data = pd.DataFrame({"input": [user_input]})
 # Extract keywords (simplified)
 data["keywords"] = data["input"].apply(lambda x: " ".join(x.split()[:3]))
 return {"keywords": data["keywords"].iloc[0]}
