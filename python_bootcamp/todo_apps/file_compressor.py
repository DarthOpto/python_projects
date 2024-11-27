import FreeSimpleGUI as fsg
from zip_creator import make_archive

# Select Files Elements
select_files_label = fsg.Text("Select files to compress:")
select_files_input = fsg.Input()
select_files_choose_btn = fsg.FilesBrowse("Choose", key='files_to_compress')

# Destination Elements
destination_label = fsg.Text("Select destination folder:")
destination_input = fsg.Input()
destination_choose_button = fsg.FolderBrowse("Choose", key='destination_folder')

# Compress button
compress_button = fsg.Button("Compress")
output_label = fsg.Text(key="output", text_color="green")

window = fsg.Window("File Compressor", layout=[[select_files_label, select_files_input, select_files_choose_btn],
                                                    [destination_label, destination_input, destination_choose_button],
                                                    [compress_button, output_label]])

while True:
    event, values = window.read()
    filepaths = values["files_to_compress"].split(";")
    folder_to_put_compressed_file = values["destination_folder"]
    make_archive(filepaths, folder_to_put_compressed_file)
    window["output"].update(value="Compression completed")


window.close()
