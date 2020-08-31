#!/usr/bin/env python
#
# Reproduce the Schneider TV Remote Control on a GUI

import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('TV Schneider')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
[sg.Button('On'), sg.Button('Chut')],
[sg.Button('1'), sg.Button('2'), sg.Button('3')],
[sg.Button('4'), sg.Button('5'), sg.Button('6')],
[sg.Button('7'), sg.Button('8'), sg.Button('9')],
[sg.Button('0')],
[sg.Button('Aspect'), sg.Button('Sleep'), sg.Button('Audio')],
[sg.Button('Haut')],
[sg.Button('Gauche'), sg.Button('OK'), sg.Button('Droite')],
[sg.Button('Exit'), sg.Button('Bas'), sg.Button('Menu')],
[sg.Button('Vol +'), sg.Button('Source'), sg.Button('Prog +')],
[sg.Button('Vol -'), sg.Button('Display'), sg.Button('Prog -')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
  #event, values = window.read()
  event = window.read()
  #if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
  if event == 'On':
    print('Bouton On')
  elif event == 'Chut':
    print('Bouton Chut')
  elif event == '1':
    print('Bouton 1')
  elif event == '2':
    print('Bouton 2')
  elif event == '3':
    print('Bouton 3')
  else:
    print('Exit app')
    break

window.close()