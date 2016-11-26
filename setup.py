import cx_Freeze

executables = [cx_Freeze.Executable(script="trat.py", icon="logo.png")]

cx_Freeze.setup(
    name = "Trat",
    options={"build_exe": {"packages": ["tkinter"],
                           "include_files": ["logo1.png", "logo.png"]}
            },
    executables = executables
    )
