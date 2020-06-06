# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Astro1_Moon'],
             binaries=[],
             datas=[('./*.py','./'),('assets/*.png','assets/'),('assets/*.jpg','assets/'),('assets/gih/*.jpg','assets/gih/'),('assets/gih/*.png','assets/gih/'),('assets/gih/*.txt','assets/gih/'),('assets/earth_moon/*.jpg','assets/earth_moon/'),('assets/earth_moon/*.txt','assets/earth_moon/'),('assets/earth_moon/*.png','assets/earth_moon/'),('assets/moon_age/*.txt','assets/moon_age/'),('assets/moon_age/*.png','assets/moon_age/'),('assets/moon_age/*.jpg','assets/moon_age/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
