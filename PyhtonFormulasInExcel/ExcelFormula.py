import pythoncom
import numpy as np
import win32com.client

class PythonObjectLibrary:
    _reg_clsid_ = pythoncom.CreateGuid()            # UniqueID for our object to register it with Windows

    _reg_clsctx = pythoncom.CLSCTX_LOCAL_SERVER     # Register the object as an EXE
    # _reg_clsctx = pythoncom.IMPROC_SERVER         # Register the object as a DLL

    _reg_progid_ = "Python.ObjectLibrary"           # Name of the our project library

    _reg_desc_ = "This is our Python Object Library"    # Optional / Description of the library

    _public_methods_ = ["pythonSum","pythonMultiply","addArray"]    # this are the methods for the user in excel

    def pythonSum(self, x, y):
        return x + y

    def pythonMultiply(self, x, y):
        return x * y

    def addArray(self, myRange):
        # create an instance of the range object passed trough
        rng1 = win32com.client.Dispatch(myRange)
        rng1val = np.array(list(rng1.Value))
        return rng1val.sum()

if __name__ == "__main__":
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonObjectLibrary)
