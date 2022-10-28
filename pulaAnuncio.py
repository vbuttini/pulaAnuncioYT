import pyautogui as pg

while True:
    button = pg.locateOnScreen(r'imagens/imagemAnuncio.png', confidence=0.8)
    if button is None: continue
    pg.click(button)
