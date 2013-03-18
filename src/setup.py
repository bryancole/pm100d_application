from distutils.core import setup

setup(name='pm100',
      version='1.0',
      description="""PM100USB Optical Power Meter python interface and
 display application (GUI).""",
      author = "Bryan Cole",
      author_email = "bryan.cole@teraview.com",
      py_modules=['pm100',],
      scripts=['pm100_wx_gui.py','post_install.py']
      )
