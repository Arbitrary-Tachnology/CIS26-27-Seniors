# Variables, Arithmetic, and importing Modules

# Demo 1 - variables and assignment
def demo1_variables():
    CAN_VOLUME = 0.355  # volume of a can in liters
    BOTTLE_VOLUME = 2.0  # volume of a bottle in liters

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six-pack volume:", packVolume, "liters.")
    print("Two-liter bottle volume:", BOTTLE_VOLUME, "liters.")

demo1_variables()

# = means "is set to" or "gets"
lives = 3
print("Lives at start:", lives)
lives = lives + 2
print("After a power-up:", lives)