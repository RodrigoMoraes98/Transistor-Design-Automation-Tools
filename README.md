# Transistor-Design-Automation-Tools

- Note that this project is under development.
############################################################################################################################
To run the design automation tools, it is required to have Python installed, as well as some modules, such as:
- NumPy
- Pandas
- PyQt5
- Matplotlib

To install the required modules, open the terminal and execute the following command:
 
pip install #name of the module#

With all the requirements installed, there are some changes that needs to be made.
  - The files "SizingTool.py", "SweepTool.py" and the folder "Circuit Sizing Tool" are put in the home folder.
  For example: if the user name is "John", so the files will be in the path "/home/John/".
  - The netlist files in this repository are not properly configurated to be used for any user, so at the moment, it needs to be manually changed.
  Inside the folder "/Circuit Sizing Tool/netlist/" there are two folders with the netlist files. Open the ".scs" files with any text editor and change the home folder in some of the first lines.
  - The file "CIWmenu.il" can be executed directly by the CIW terminal from the Cadence Virtuoso environment. To run the application, on the CIW terminal, use the command 
 
  - #load("file_directory/CIWmenu.il")#
 
The terminal will print "t" if the process was done correctly. A menu will appear with the name "GAMA Tools", on which the softwares can be accessed.
#############################################################################################################################
