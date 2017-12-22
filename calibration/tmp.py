from St7API import *
import ctypes
import os
import sys

unitStrings = {suPASCAL: 'Pa',
               suKILOPASCAL: 'kPa',
               suMEGAPASCAL: 'MPa',
               suKSCm: 'KSCm',
               suPSI: 'PSI',
               suPSF: 'PSF'}

# Account for differences between Python2 and Python3 (2.6 and upwards should work).

if sys.version_info[0] >= 3:
    # Python 3
    import tkinter as tk
    import tkinter.filedialog as tkFD

else:
    import Tkinter as tk
    import tkFileDialog as tkFD


# Error checking function. Turns a non-zero integer returned by Strand API call into a Python exception
def ChkErr(ErrorCode):
    ErrorOccured = (ErrorCode != 0)
    if ErrorOccured:
        ErrorString = ctypes.create_string_buffer(kMaxStrLen)

        # Attempt to get API error string
        iErr = St7GetAPIErrorString(ErrorCode, ErrorString, kMaxStrLen)

        # If that failed, attempt to retrive a solver error string
        if iErr:
            iErr = St7GetSolverErrorString(ErrorCode, ErrorString, kMaxStrLen)

        if not iErr:
            raise Exception('%s (%d)' % (ErrorString.value, ErrorCode))
        else:
            raise Exception('An unknown error occured (%d)' % ErrorCode)

    return ErrorOccured


# Main optimisation function, called either by the GUI or can be called directly if this module is imported elsewhere
def RunPlateDemo(modPath, nIters = 1, showWindow = True, maxThickness = 2):
    # Wrap everything in a try/except/finally block so the API is unloaded even after an exception
    try:
        # Initialise
        ChkErr(St7Init())

        # Open the file
        ChkErr(St7OpenFile(1, modPath, r'C:\temp'.encode()))

        # Show the model window if that was requested
        if showWindow:
            ChkErr(St7CreateModelWindow(1))
            ChkErr(St7ShowModelWindow(1))
            ChkErr(St7PositionModelWindow(1, 0, 0, 640, 480))

        # Set results file name to model name without extension
        resFileName = os.path.splitext(modPath)[0]
        ChkErr(St7SetResultFileName(1, resFileName))

        # Perform optimsation several times if requested
        for iIter in range(nIters):

            # Run Linear Static Solver
            ChkErr(St7RunSolver(1, stLinearStaticSolver, smBackgroundRun, 1))

            # Open results files
            nPrim, nSec = ctypes.c_int(), ctypes.c_int()
            ChkErr(St7OpenResultFile(1, resFileName + '.lsa'.encode(), ''.encode(), False, nPrim, nSec))

            # Get the number of plates and iterate over them, saving the VM stress
            nPlatesCtypes = ctypes.c_int()
            numPoints, numCols = ctypes.c_int(), ctypes.c_int()
            ChkErr(St7GetTotal(1, tyPLATE, nPlatesCtypes))

            # Build dictionary of PlateNum->VM Stress
            plateVM = {}
            plateResultArrayType = ctypes.c_double * kMaxPlateResult
            plateResArray = plateResultArrayType()

            for iPlate in range(1, nPlatesCtypes.value + 1):
                ChkErr(St7GetPlateResultArray(1, rtPlateStress, stPlateCombined, iPlate, 1, AtCentroid,
                                                  psPlateMidPlane, 0, numPoints, numCols, plateResArray))

                plateVM[iPlate] = plateResArray[ipPlateCombVonMises]

            # Close results file
            ChkErr(St7CloseResultFile(1))

            # Get the units
            unitsArrayType = ctypes.c_long * kLastUnit
            units = unitsArrayType()
            ChkErr(St7GetUnits(1, units))

            vmVals = plateVM.values()
            meanVM = sum(vmVals)/len(vmVals)
            print('[%d/%d] Min/Mean/Max VM Stress: %f/%f/%f %s'%(iIter+1, nIters, min(vmVals), meanVM, max(vmVals), unitStrings.get(units[ipSTRESSU], '??Units')))

            # Modify plate thicknesses
            plateAttributeType = ctypes.c_double * kMaxAttributeDoubles
            plateAttribs = plateAttributeType()
            for iPlate in range(1, nPlatesCtypes.value + 1):
                ChkErr(St7GetPlateThickness2(1, iPlate, plateAttribs))
                newThickness = min([plateAttribs[ipTHICKM] * plateVM[iPlate]/meanVM, maxThickness])
                plateAttribs[ipTHICKM] = newThickness
                plateAttribs[ipTHICKB] = newThickness
                ChkErr(St7SetPlateThickness2(1, iPlate, plateAttribs))

            if showWindow:
                ChkErr(St7UpdateElementPropertyData(1, ptPLATEPROP, 1))
                ChkErr(St7RedrawModel(1, True))

        # Save and close
        ChkErr(St7SaveFile(1))

    finally:
        # These calls are made even if an exception was raised in the main block
        if showWindow:
            ChkErr(St7DestroyModelWindow(1))

        St7CloseFile(1)
        St7Release()


# Code to generate and run the GUI.
if __name__ == '__main__':

    # Generate main window
    root = tk.Tk()
    root.title('Plate Optimisation')

    # Layout with some options
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Variables which are manipulated by user interface controls
    filePath = tk.StringVar()
    numIters = tk.StringVar()
    showWind = tk.BooleanVar()

    # Get user input of the model name
    def selFile(*args):
        st7FileType = [ ('St7 files', '.st7') ]
        filePath.set(os.path.normpath(tkFD.askopenfilename(parent=mainframe, filetypes=st7FileType)))
        fileNameLabel['text'] = filePath.get()

    # Function called when user clicks Run
    def runOpt(*args):
        if os.path.isfile(filePath.get()):
            print(filePath.get())
            RunPlateDemo(filePath.get().encode(), nIters = int(numIters.get()), showWindow = bool(showWind.get()))
        else:
            fileNameLabel['text'] = 'Select a file'


    fileNameLabel = tk.Label(mainframe, text='')
    fileNameLabel.grid(column=1, columnspan=2, row=1, sticky=(tk.N, tk.W))

    pickFile = tk.Button(mainframe, text='Select File', command=selFile)
    pickFile.grid(column=1, columnspan=2, row=2, sticky=(tk.N, tk.E, tk.W))

    numIters.set('5')
    iterSel = tk.Spinbox(mainframe, from_=1, to=20, textvariable=numIters)
    iterSel.grid(column=1, row=3, sticky=(tk.E, tk.W))

    showWind.set(True)
    showModCheck = tk.Checkbutton(mainframe, text='Show model window', variable=showWind)
    showModCheck.grid(column=1, columnspan=2, row=4, sticky=(tk.N, tk.W))

    tk.Label(mainframe, text='Number of iterations to perform').grid(column=2, row=3, sticky=tk.W)

    # Run button
    runButton = tk.Button(mainframe, text='Perform Optimisation', command=runOpt)
    runButton.grid(column=1, columnspan=2, row=5, sticky=(tk.S, tk.E, tk.W))

    # Put some padding around everything
    for child in mainframe.winfo_children(): child.grid_configure(padx=6, pady=6)

    root.mainloop()
