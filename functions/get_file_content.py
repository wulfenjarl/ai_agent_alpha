
import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'


        with open(target_dir, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            extra_bits = f.read(1)
            # After reading the first MAX_CHARS...
            if extra_bits:
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return file_content_string

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads file content as a string",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read file content from, relative to the working directory (no default, param required)",
                },
            },
            "required": ["file_path"]
        },
    },
}
