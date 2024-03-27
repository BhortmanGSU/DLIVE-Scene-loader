import mido

# Scene number to recall
scene_number = 25  # Replace with your scene number

# Calculate bank number and scene number within bank
bank_number = (scene_number - 1) // 128
scene_within_bank = (scene_number - 1) % 128

# MIDI command to select bank
bank_select_command = mido.Message('control_change', channel=0, control=0, value=bank_number)

# Find the port for the MIDI device
midi_ports = mido.get_output_names()
midi_control_1_port = next((port for port in midi_ports if 'MIDI Control 1' in port), None)

if midi_control_1_port is None:
    print("MIDI Control 1 not found")
else:
    # Open the port
    with mido.open_output(midi_control_1_port) as outport:
        # Send the bank select command
        outport.send(bank_select_command)

        # MIDI command to recall scene
        scene_recall_command = mido.Message('program_change', channel=0, program=scene_within_bank)
        # Send the scene recall command
        outport.send(scene_recall_command)