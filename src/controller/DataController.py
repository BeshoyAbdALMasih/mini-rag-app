from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1048576 


    def validate_uploaded_file(self,file:UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale :
            return  False,ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, "success"
    
    
    def generate_uniqe_filepath(self,orig_file_name:str, project_id:str):
        
        random_filename=self.genrate_randome_string()
        project_path=ProjectController().get_project_path(project_id=project_id)

        cleaned_filename=self.get_clean_filename(orig_file_name=orig_file_name)

        new_file_path=os.path.join(
            project_path,
            random_filename+"_"+cleaned_filename
        )    

        while os.path.exists(new_file_path):
            random_filename=self.genrate_randome_string()
           
            new_file_path=os.path.join(
                project_path,
                random_filename+"_"+cleaned_filename
                )     

        return new_file_path , random_filename+"_"+cleaned_filename


    def get_clean_filename(self,orig_file_name):
        
        cleaned_filename= re.sub(r'[^\w.]','',orig_file_name.strip())
        cleaned_filename= cleaned_filename.replace(" ","_")
        
        return cleaned_filename 

