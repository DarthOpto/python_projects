import FreeSimpleGUI as fsg

# Select Files Elements
select_files_label = fsg.Text("Select files to compress:")
select_files_input = fsg.Input()
select_files_choose_btn = fsg.FilesBrowse("Choose")

# Destination Elements
destination_label = fsg.Text("Select destination folder:")
destination_input = fsg.Input()
destination_choose_button = fsg.FolderBrowse("Choose")

# Compress button
compress_button = fsg.Button("Compress")

window = fsg.Window("File Compressor", layout=[[select_files_label, select_files_input, select_files_choose_btn],
                                                    [destination_label, destination_input, destination_choose_button],
                                                    [compress_button]])
window.read()
window.close()
