from pathlib import Path
import os


project_name = "Air_Qualit_App"

list_of_items = [

    f'{project_name}/README.md',
    f'{project_name}/src/__init__.py',
    f'{project_name}/src/logger.py',
    f'{project_name}/src/utils.py',
    f'{project_name}/src/exception.py',
    f'{project_name}/src/components/__init__.py',
    f'{project_name}/src/components/data_ingestion.py',
    f'{project_name}/src/components/data_transformation.py',
    f'{project_name}/src/components/model_trainer.py',
    
]

for file_path in list_of_items:

    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(file_path)) or (not os.path.getsize(file_path)):
        with open(file_path, 'w') as file_obj:
            pass
    else:
        print("File already exist.")