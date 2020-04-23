import rhinoscriptsyntax as rs

def RunNotepad():
    cmd = "_Run C:/Windows/notepad.exe"
    rs.Command(cmd, False)

RunNotepad()
