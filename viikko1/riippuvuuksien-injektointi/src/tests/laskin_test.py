import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")

    def test_kaksi_perakkaista(self):
        io1 = StubIO(["1", "3", "-9999"])
        io2 = StubIO(["2", "9", "-9999"])
        laskin1 = Laskin(io1)
        laskin2 = Laskin(io2)
        laskin1.suorita()
        laskin2.suorita()

        self.assertEqual(io1.outputs[0], "Summa: 4")
        self.assertEqual(io2.outputs[0], "Summa: 11")