import cmd
import os
from rich.markdown import Markdown
from rich.console import Console
from rich import print
import pyfiglet



class cheatsheetCLI(cmd.Cmd):
    prompt = 'cheatsheetCLI>> '
    console = Console()
    text = "CheatsheetCLI"
    ascii_art = pyfiglet.figlet_format(text)

    def __init__(self):
        super().__init__()
        self.print_intro()

    def print_intro(self):
        # print("[bold magenta]Welcome to cheatsheetCLI![/bold magenta]")
        print(self.ascii_art)
        print("")
        print("Here are the available cheatsheets:")
        print("")
        print("")
        print("[bold green]1 - Git[/bold green]")
        print("[bold blue]2 - Python[/bold blue]")
        print("[bold yellow]3 - Typescript[/bold yellow]")
        print("[bold magenta]4 - Docker[/bold magenta]")
        print("[bold cyan]5 - React[/bold cyan]")
        print("")
        print("")
        print("Type the number of the cheatsheet you need (q - to exit):")

    def display_cheatsheet(self, file_name):
        file_path = os.path.join("cheatsheets", f"{file_name}.md")
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                md_content = file.read()
                self.console.print(Markdown(md_content))
        else:
            print(f"Cheatsheet for {file_name} not found.")

    def do_1(self, arg):
        self.display_cheatsheet('git')

    def do_2(self, arg):
        self.display_cheatsheet('python')

    def do_3(self, arg):
        self.display_cheatsheet('typescript')

    def do_4(self, arg):
        self.display_cheatsheet('docker')

    def do_5(self, arg):
        self.display_cheatsheet('react')


    def do_q(self, arg):
        """Exit the CLI"""
        print("Goodbye!")
        return True 

if __name__ == '__main__':
    cheatsheetCLI().cmdloop()

