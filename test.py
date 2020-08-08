import board
import neopixel


pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1)
pixels.fill((255, 0 , 255))
pixels.show()

