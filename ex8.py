formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")

print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "i had the thing",
    "that you could tyoe uop right",
    "but it didn;t sing",
    "so i said goodnight"
)