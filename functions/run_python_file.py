import os
import config
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)
        ai_running = subprocess.run(command, capture_output=True, cwd=abs_path,text=True, timeout=30)

        if ai_running.returncode != 0:
            return f"Process exited with code {ai_running.returncode}"
        if ai_running.stdout == "" and ai_running.stderr == "":
            return 'No output produced'
        else:
            result_text = []
            if ai_running.stdout:
                result_text.append(f'STDOUT: {ai_running.stdout}') 
            if ai_running.stderr:
                result_text.append(f'STDERR: {ai_running.stderr}')
            final_results = "\n".join(result_text)    
            return final_results    
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a Python script",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to choose executable files from, relative to the working directory (no default, param is required)",
                },
                "args": {
                    "type": "array",
                        "items": {
                            "type": "string",
                                },
                            "description": "Optional command-line arguments to pass to the script",
                            },
            },
        "required": ["file_path"]
        },
    },
}
