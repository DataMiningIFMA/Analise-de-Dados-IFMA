import os
import pandas as pd

input_folder = 'C:/Users/there/Documents/PROJETO MINERAÇÃO/Araioses' 
output_folder = 'C:/Users/there/Documents/PROJETO MINERAÇÃO/Ara' 

os.makedirs(output_folder, exist_ok=True)

def filter_and_save_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            df = pd.read_csv(file_path)
            df_filtered = df[(df['ano'] >= 2019) & (df['ano'] <= 2023)]
            
            output_path = os.path.join(output_folder, filename)
            df_filtered.to_csv(output_path, index=False)

filter_and_save_files(input_folder, output_folder)

print("Arquivos filtrados e salvos com sucesso!")
