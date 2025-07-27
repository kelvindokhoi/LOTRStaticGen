import os
import shutil

class StaticOperations:
    def __init__(self,RUNNING_LOCALLY=True,ignore_list = []):
        self.delete_log = []
        self.copy_log = []
        self.static_path = os.path.join(os.path.abspath('./'),'static')
        self.public_path = os.path.join(os.path.abspath('./'),'public') if RUNNING_LOCALLY else os.path.join(os.path.abspath('./'),'docs')
        self.ignore_list = ignore_list

    def delete_public_contents(self):
        self.delete_log.append("Deleting public contents")
        public_path = self.public_path
        if os.path.exists(public_path):
            shutil.rmtree(public_path)
            if os.path.exists(self.public_path):
                self.delete_log.append("Deleting public contents failed ❌")
            else:
                self.delete_log.append("Deleting public contents succeeded ✅")
        else:
            self.delete_log.append("Public is already deleted ✅")

        self.delete_log.append("Creating new public directory")
        os.makedirs(public_path, exist_ok=True)


    def copy_static_content_to_public(self,path,dst):
        try:
            if os.path.isfile(path):
                file_name = os.path.basename(path)
                self.copy_log.append(f'Copying {file_name} at {path}')
                shutil.copy(path,dst)
                if os.path.exists(os.path.join(dst,file_name)):
                    self.copy_log.append(f'Copying {file_name} to {dst} succeeded ✅')
                else:
                    self.copy_log.append(f'Copying {file_name} to {dst} failed ❌')
            else: #folder
                folder_name = os.path.basename(path)
                self.copy_log.append(f"Checking folder {folder_name}")
                for dir in os.listdir(path):
                    new_path = os.path.join(path,dir)
                    if os.path.isdir(new_path):
                        new_dst = os.path.join(dst,dir)
                        os.makedirs(new_dst, exist_ok=True)
                        self.copy_static_content_to_public(new_path,new_dst)
                    else:
                        if any(dir.endswith(ending) for ending in self.ignore_list):
                            continue
                        self.copy_static_content_to_public(new_path,dst)       
        except Exception as e:
            self.copy_log.append(str(e))

    def delete_public_and_copy_static_to_public(self):
        self.delete_public_contents()
        self.copy_static_content_to_public(self.static_path,self.public_path)
        return '\n'.join(self.delete_log+self.copy_log)

    

