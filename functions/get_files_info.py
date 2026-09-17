
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        lines = []
        for name in os.listdir(target_dir):
            full_path = os.path.join(target_dir, name)
            size = os.path.getsize(full_path)
            is_direct = os.path.isdir(full_path)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_direct}")
            result = "\n".join(lines)
        return result
            
    except Exception as e:
        return f"Error: {e}"

  