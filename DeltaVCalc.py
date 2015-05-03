""" Small script to calculate a rocket stage's delta V for Kerbal Space Program """

from math import log, trunc

__author__ = 'Alex'

GRAVITATIONAL_CONSTANT = 9.81


def main():
    while True:
        m_init = float(input("Initial mass: "))
        m_end = float(input("    End mass: "))
        isp = float(input("  Engine ISP: "))
        delta_v = trunc(calculate_delta_v(m_init, m_end, isp))
        print("Rocket Delta V = " + str(delta_v) + "m/s")
        input("Enter to begin again, or Ctrl + c close...")

def calculate_delta_v(m_init, m_end, isp):
    return log(m_init/m_end) * isp * GRAVITATIONAL_CONSTANT


if __name__ == "__main__":
    main()