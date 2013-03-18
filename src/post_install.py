#!python

import sys,os

argv = sys.argv

if argv[1]=="-install":
    ### Append .py to scripts
    #os.rename(os.path.join(sys.prefix, 'Scripts', 'anikom15'),
    #          os.path.join(sys.prefix, 'Scripts', 'anikom15.py'))
    #file_created(os.path.join(sys.prefix, 'Scripts', 'anikom15.py'))
    # Create desktop and start menu shortcuts
    #desktop = get_special_folder_path("CSIDL_COMMON_DESKTOPDIRECTORY")
    startmenu = get_special_folder_path("CSIDL_COMMON_STARTMENU")
    link_pth = os.path.join(startmenu, 'Programs', 'Teraview', 'PM100_PowerMeter.lnk')
    create_shortcut(os.path.join(sys.prefix, 'Scripts', 'pm100_wx_gui.py'),
                    "Launch PM100 Optical Power Meter GUI",
                    link_pth,
                    #'', '',
                    #os.path.join(sys.prefix, 'Icons', 'anikom15.ico')
                    )
    file_created(link_pth)

elif argv[1]=="-remove":
    pass
else:
    print "Don't understand:", argv