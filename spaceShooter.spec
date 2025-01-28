# -*- mode: python ; coding: utf-8 -*-


files = ['bolt_gold.png', 'expl3.wav', 'expl6.wav', 'getready.ogg', 'highscore.txt', 
'kitty_small.PNG', 'laserRed16.png', 'main.png', 'menu.ogg', 'meteorBrown_big1.png', 
'meteorBrown_big2.png', 'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 
'meteorBrown_small2.png', 'meteorBrown_tiny1.png', 'missile.png', 'option1.jpg', 'pew.wav', 'playerShip1_orange.png',
 'regularExplosion00.png', 'regularExplosion01.png', 'regularExplosion02.png', 'regularExplosion03.png', 
 'regularExplosion04.png', 'regularExplosion05.png', 'regularExplosion06.png', 'regularExplosion07.png', 
 'regularExplosion08.png', 'rocket.ogg', 'rumble1.ogg', 'shield_gold.png', 'sonicExplosion00.png', 
 'sonicExplosion01.png', 'sonicExplosion02.png', 'sonicExplosion03.png', 'sonicExplosion04.png', 
 'sonicExplosion05.png', 'sonicExplosion06.png', 'sonicExplosion07.png', 
'sonicExplosion08.png', 'spaceShooter.py', 'spaceShooter.spec', 'starfield.png', 'tgfcoder-FrozenJam-SeamlessLoop.ogg']

block_cipher = None

a = Analysis(
    ['spaceShooter.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

for file in files:
    a.datas += [(file, f"C:\\Users\\dbili\\space_project\\spaceshooter\\{file}", "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Kitty Space Shooter',
          debug=False,
          strip=False,
          upx=True,
          console=False)


