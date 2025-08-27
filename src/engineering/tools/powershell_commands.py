from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import subprocess

class PowerShellCommandInput(BaseModel):
    """Input schema for PowerShellCommand."""
    command: str = Field(..., description="The PowerShell command to run.")

class PowerShellCommand(BaseTool):
    name: str = "PowerShell Command"
    description: str = "Executes a PowerShell command on the local system."
    args_schema: Type[BaseModel] = PowerShellCommandInput

    def _run(self, command: str) -> str:
        try:
            # Try Windows PowerShell first, then fallback to pwsh if not available
            for args in [
                ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", command],
                ["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", command],
                ["pwsh", "-NoProfile", "-NonInteractive", "-Command", command],
            ]:
                try:
                    result = subprocess.run(
                        args,
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    return result.stdout.strip() or "Command executed successfully."
                except FileNotFoundError:
                    # Try next executable in the list
                    continue
                except subprocess.CalledProcessError as e:
                    return f"Error executing command:\n{e.stderr.strip()}"
            return "Error executing command:\nPowerShell executable not found."
        except subprocess.CalledProcessError as e:
            return f"Error executing command:\n{e.stderr.strip()}"