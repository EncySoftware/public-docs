# System module

The system module is connected to every script automatically. It contains the routines for files,
folders, dialogs and other programs, and the variable `error_level`.

## Text files

A text file is read with an object of the class `file_reader` and written with an object of the
class `file_writer`. The encoding of the file is set with a number:

| Encoding | Value |
|---|---|
| UTF-8 | `1` |
| UTF-16 | `2` |
| Windows code page (ANSI) | `3` |

`create_file_writer(file: string; encoding: integer; create_flags: integer): file_writer` opens a
file for writing. `create_flags` is `1` to create a new file (an existing file is overwritten) or `2`
to add to the end of a file that already exists.

| Method of `file_writer` | Action |
|---|---|
| `writeln(line: string)` | Writes the line and a line break |
| `Destroy` | Closes the file |

`create_file_reader(file: string; encoding: integer): file_reader` opens a file for reading.

| Method of `file_reader` | Action |
|---|---|
| `readln(var line: string)` | Reads the next line into `line` |
| `eof: integer` | `1` if the end of the file is reached, otherwise `0` |
| `size: integer` | Size of the file in bytes |
| `Destroy` | Closes the file |

The file written by a `file_writer` stays open until `Destroy` is called; until then it cannot be
read.

```pascal
program TextFile
var
  w: file_writer
  r: file_reader
  line, fileName: string
begin
  fileName = get_cur_dir + '\report.txt'

  w = create_file_writer(fileName, 1, 1)
  w.writeln('first line')
  w.writeln('second line')
  w.Destroy

  r = create_file_reader(fileName, 1)
  while r.eof = 0 do begin
    r.readln(line)
    print line
  end
  r.Destroy
end
```

## Files and folders

| Routine | Result |
|---|---|
| `file_exists(file: string): boolean` | `true` if the file exists |
| `delete_file(file: string): boolean` | Deletes the file; `true` on success |
| `dir_exists(dir: string): boolean` | `true` if the folder exists |
| `create_dir(dir_name: string): boolean` | Creates the folder; `true` on success |
| `remove_dir(dir_name: string): boolean` | Deletes an empty folder; `true` on success |
| `get_cur_dir: string` | Current folder |
| `set_cur_dir(dir_name: string): boolean` | Changes the current folder; `true` on success |
| `extract_file_name(file_name: string): string` | File name with extension, without the folder |
| `extract_file_dir(file_name: string): string` | Folder of the file |

A path without a folder is relative to the current folder.

## Dialogs

| Routine | Result |
|---|---|
| `show_message(message, title: string; buttons, icon: integer): integer` | Shows the message `message` and returns the button pressed; `title` is not used |
| `input_edit(capt: string): string` | Asks for a line of text with the prompt `capt`; returns the text or an empty string if the dialog is cancelled |
| `input_combo(capt: string; val_list: string_array50; def_index: integer): integer` | Offers a choice from the list `val_list`; returns the index of the chosen item (from 0) or `def_index` if the dialog is cancelled |
| `open_file_dialog(init_dir, title, filter: string; filter_index: integer): string` | Standard dialog for opening a file; returns the full file name or an empty string |
| `save_file_dialog(init_dir, title, filter: string; filter_index: integer): string` | Standard dialog for saving a file; returns the full file name or an empty string |

`show_message` values:

| `buttons` | Buttons | `icon` | Icon |
|---|---|---|---|
| 1 | OK | 1 | Error |
| 2 | OK, Cancel | 2 | Warning |
| 3 | Yes, No | 3 | Information |
| 4 | Yes, No, Cancel | other | Question |
| 5 | Abort, Retry, Ignore | | |

The result is `1` for OK, `2` for Cancel, `3` for Yes, `4` for No, `5` for Abort, `6` for Retry,
`7` for Ignore.

`string_array50` is an array of 50 strings declared in the system module; empty strings are not
shown in the list.

The `filter` of the file dialogs is a list of pairs "description|mask" separated with `|`, for
example `'Text files (*.txt)|*.txt|All files (*.*)|*.*'`. `filter_index` selects the pair shown
first, starting from 1. Both file dialogs have a form with the fifth parameter
`def_filename: string`, the file name suggested in the dialog.

```pascal
var
  items: string_array50
  choice: integer
begin
  items[0] = 'Roughing'
  items[1] = 'Finishing'
  choice = input_combo('Machining stage', items, 0)
  if show_message('Selected: ' + items[choice], 'Stage', 2, 3) = 1 then
    print items[choice]
end
```

## Other programs

`start_process(cmd_line: string): boolean` starts a program with the command line `cmd_line` and
returns `true` if it has started. The script does not wait for the program to finish.

```pascal
start_process('notepad.exe ' + fileName)
```

## error_level

The variable `error_level` controls the reporting of [run-time errors](runtime-errors.md): `el_default`
(0) reports them, `el_no_report` (1) does not.
