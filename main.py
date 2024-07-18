#from transformers import AutoTokenizer, AutoModelForSequenceClassification
#from scipy.special import softmax
import numpy as np
import pandas as pd
from taipy.gui import Gui, notify
import taipy.gui.builder as tgb

path = None
data = pd.DataFrame()
treatment=0
dataframe = pd.DataFrame({"No. of ":['Row_Count', "Col_Count"],
                          "Count":[0,0],
                        })
def load_csv_file(state):
    state.data = pd.read_csv(state.path)
    notify(state, 'info', f'The file uploaded successfully')
    return data

def local_callback(state,data):
    notify(state, 'info', f'The data shape is: {state.data.shape}')
    return state.data.describe()
# md = """
# <|toggle|theme|>
# <#Data Processing **(Apple or/And Youtube)**{: .color-primary} Dashboard>
# <|layout|class_name=card|{path}|file_selector|label=Upload dataset|on_action=load_csv_file|extensions=.csv|>

# <|{data}|table|rebuild|>
# """
table_properties = {
    "class_name": "rows-bordered",
    "filter": True,
}
# Definition of the page with tgb
with tgb.Page() as page:
    tgb.toggle(theme=True)

    tgb.text("# Data Processing Dashboard", mode="md")
    with tgb.Page() as page_file:
        tgb.file_selector("{path}", extensions=".csv", label="Upload .csv file",
                    on_action=load_csv_file)
        
        #with tgb.expandable("Table"):
        #tgb.table("{data}", properties=table_properties)

        with tgb.button("Analyze", on_action=local_callback):
            tgb.text("Total rows in the table are {data.shape[0]}", format="%.2f")
            tgb.text("Total columns in the table are {data.shape[1]}", format="%.2f")
 

# Initialize the GUI with the updated dataframe
Gui(page).run(debug=True,title="Data upload",port=2451)