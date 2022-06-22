from turtle import left 
from matplotlib.pyplot import fill
from numpy import s_
from pyparsing import col
import qiskit
import tkinter
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition


#Define window
root = tkinter.Tk();
root.title('Qubit-Visualizer');

#set the icon
root.iconbitmap(default='logo.ico');
root.geometry('399x378');
root.resizable(0,0); #Blocking the resiable feature :)
 
#defining colors and font 
background = '#2c94c8';
buttons = '#834558';
special_buttons = '#bc3454';
button_font = ('Arial',18);
display_font = ('Arial',32);

#Define display
def display_gate(gate_input):
    """
    Adds a corresponding gate notation to diaplay to keep track of operations
    If number of operations reach 10 then all gates are disabled. 
    """

    #Insert the defined gate
    display.insert(tkinter.END,gate_input);

    #Check if number of operations reached 10 if yes then disable all the gates
    input_gates = display.get();
    num_gates_presssed = len(input_gates);
    list_input_gates = list(input_gates);
    search_word = ["R","D"];
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word];
    num_gates_presssed -= sum(count_double_valued_gates);
    if num_gates_presssed == 10:
        gates = [x_gate, y_gate, z_gate, s_gate, sd_gate, t_gate, td_gate, hadmard];
        for gate in gates:
            gate.config(state=tkinter.DISABLED);



#Initialize Quantum Circuit
def initialize_circuit():
    global circuit;
    circuit = QuantumCircuit(1);

initialize_circuit();
theta = 0;


#Define functions

#define function for visualize button
def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations for applied gates in a seperate tkinter window
    Handles any possible visualization error
    """
    try:
        visualize_transition(circuit=circuit);
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy();




#define function for clear button
def clear(circuit):
    """
    Clears the Display 
    Reinitializes the Quantum Circuit for fresh Calculation
    Checks if the gate buttons are diabled if yes then enables them
    """
    #clear the display
    display.delete(0,tkinter.END);

    #reset the circuit to initial state |0>
    initialize_circuit();

    if x_gate['state'] == tkinter.DISABLED:
        gates = [x_gate, y_gate, z_gate, s_gate, sd_gate, t_gate, td_gate, hadmard];
        for gate in gates:
            gate.config(state=tkinter.NORMAL);




#define function for about 
def about():
    """""
    Display the info about project!
    """""
    info = tkinter.Tk();
    info.title('About');
    info.geometry('650x470');
    info.resizable(0,0);

    text = tkinter.Text(info,height=20,width=20);

    #creat label
    label = tkinter.Label(info,text='About QuantumLabs: ');
    label.config(font=('Arial',14));

    text_to_display ="""
    About : Visualization tool for Single Qubit Rotation on Block Sphere

    Created by : Harshal Rudra
    Created Using = Python,Tkinter,Qiskit
    """
    label.pack();
    text.pack(fill='both',expand =True);
    text.insert(tkinter.END,text_to_display);

    info.mainloop();

#Define Layout
#Define Frames 
display_frame = tkinter.LabelFrame(root);
button_frame = tkinter.LabelFrame(root, bg='black');
display_frame.pack();
button_frame.pack(fill='both', expand=True);

#Define the Display Frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10,justify=tkinter.LEFT);
display.pack(padx=3,pady=4);

#Define the Button Frame Layout
#Define first row of buttons 
x_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='X',command=lambda:[display_gate('x'),circuit.x(0)]);
y_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Y',command=lambda:[display_gate('y'),circuit.y(0)]);
z_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Z',command=lambda:[display_gate('z'),circuit.z(0)]);
x_gate.grid(row=0,column=0,ipadx=45,pady=1);
y_gate.grid(row=0,column=1,ipadx=45,pady=1);
z_gate.grid(row=0,column=2,ipadx=53,pady=1,sticky='E');

#Define second row of buttons 
# Rx_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='RX')#,command=lambda:[display_gate('Rx'),user_input(circuit,'x')]);
# Ry_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='RY')#,command=lambda:[display_gate('Ry'),user_input(circuit,'y')]);
# Rz_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='RZ')#,command=lambda:[display_gate('Rz'),user_input(circuit,'z')]);
# Rx_gate.grid(row=1,column=0, columnspan=1,sticky='WE',pady=1);
# Ry_gate.grid(row=1,column=1, columnspan=1,sticky='WE',pady=1);
# Rz_gate.grid(row=1,column=2, columnspan=1,sticky='WE',pady=1);

#Define Third row of buttons
s_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='S',command=lambda:[display_gate('s'),circuit.s(0)]);
sd_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='SD',command=lambda:[display_gate('SD'),circuit.sdg(0)]);
hadmard = tkinter.Button(button_frame,font=button_font,bg=buttons,text='H',command=lambda:[display_gate('H'),circuit.h(0)]);
s_gate.grid(row=2,column=0, columnspan=1,sticky='WE',pady=1);
sd_gate.grid(row=2,column=1,sticky='WE',pady=1);
hadmard.grid(row=2,column=2, rowspan=2,sticky='WENS',pady=1);


#Define fourth row of buttons
t_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='T',command=lambda:[display_gate('t'),circuit.t(0)]);
td_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='TD',command=lambda:[display_gate('TD'),circuit.tdg(0)]);
t_gate.grid(row=3,column=0,sticky='WE',pady=1);
td_gate.grid(row=3,column=1,sticky='WE',pady=1);

#Define the Quit and Visualize buttons
quit = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Quit',command=root.destroy);
visualize = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Visualize', command=lambda:visualize_circuit(circuit,root));
quit.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5,pady=1);
visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8,pady=1);

#Define clear button
clear_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Clear', command=lambda:clear(circuit));
clear_button.grid(row=5,column=0,columnspan=3,sticky='WE');

#Define about button
about_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='About',command=about);
about_button.grid(row=6,column=0,columnspan=3,sticky='WE');





#Run the mainloop
root.mainloop();


