# -*- mode: python -*-
import platform

arch = platform.architecture()
if arch[0].startswith("64"):
  bits=64
elif arch[0].startswith("32"):
  bits=32
else:
  print "unknown bits?"
  bits=NA

sys = platform.system().lower()
if sys.startswith("windows"):
  ext=".exe"
else:
  ext=""

block_cipher = None

if sys.startswith("linux"):
  a = Analysis(['main.py'],
             pathex=['.'],
             binaries=None,
             datas=None,
             hiddenimports=['_cffi_backend'],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
elif sys.startswith("windows"):
  a = Analysis(['main.py'],
             pathex=['.'],
             hiddenimports=['_cffi_backend', 'queue'],
             hookspath=None,
             runtime_hooks=None)
             
a.binaries  += [('sc_monkey_runner32.so', './bin/sc_monkey_runner32.so', 'BINARY')]
a.binaries  += [('sc_monkey_runner64.so', './bin/sc_monkey_runner64.so', 'BINARY')]

# windoze
if platform.system().find("Windows")>= 0:
  a.datas = [i for i in a.datas if i[0].find('Include') < 0]
  if platform.architecture()[0] == "32bit":
    a.binaries  += [('mk.dll', '.\\bin\\mk32.dll', 'BINARY')]
  else:
    a.binaries  += [('mk.dll', '.\\bin\\mk64.dll', 'BINARY')]
  a.binaries += [('msvcr100.dll', os.environ['WINDIR'] + '\\system32\\msvcr100.dll', 'BINARY')]
  ico="monkey.ico'"
  pyz = PYZ(a.pure)
else:
  ico="options"
  pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=("%s-%s-%s%s" % ('monkey', sys, bits, ext)),
          debug=False,
          strip=True,
          upx=True,
          console=True, icon=ico )
