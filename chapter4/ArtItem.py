class ArtItem:
    def __init__(self, number, weight, value):
        self.number = number
        self.weight = weight
        self.value = value

    def __str__(self):
        return 'number %s, weight %s, value %s' % (self.number, self.weight, self.value)

