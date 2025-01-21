import cmd
import os
from rich.markdown import Markdown
from rich.console import Console
import markdown


class cheatsheetCLI(cmd.Cmd):
    intro = '''Welcome to cheatsheetCLI! Here are the available cheatsheets:
    1 - Python
    2 - TypeScript
    3 - Git
    4 - Docker
    5 - Node.js
    6 - React
    7 - AWS
    8 - Linux
    9 - SQL
    
    Type the number of the cheatsheet you need: '''
    
    prompt = 'cheatsheetCLI>> '
    console = Console()

    def display_cheatsheet(self, file_name):
        file_path = os.path.join("cheatsheets", f"{file_name}.md")
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                md_content = file.read()
                self.console.print(Markdown(md_content))
        else:
            print(f"Cheatsheet for {file_name} not found.")

    def do_1(self, arg):
        """Display Python cheatsheet"""
        print("Displaying Python cheatsheet...")
        self.display_cheatsheet('python')

    def do_2(self, arg):
        """Display TypeScript cheatsheet"""
        print("Displaying TypeScript cheatsheet...")

    def do_3(self, arg):
        """Display Git cheatsheet"""
        print("Displaying Git cheatsheet...")

    def do_exit(self, arg):
        """Exit the CLI"""
        print("Goodbye!")
        return True 

if __name__ == '__main__':
    cheatsheetCLI().cmdloop()

