""" Small script to calculate a rocket stage's delta V for Kerbal Space Program """

from math import log, trunc

__author__ = 'Alex'

DELIMITER = "----------"
TWR_DEC_PLACES = 2
SURFACE_GRAVITIES = [("Kerbin", 9.81), ("Mun", 1.63), ("Minmus", 0.491)]


def main():
    while True:
        print("Enter stage details")

        # Get the stage values
        m_init = get_typed_input("Initial mass: ", float)
        m_end = get_typed_input("End mass: ", float)
        # If we have no masses, we can't do any calculations, so start again
        if None in (m_init, m_end):
            continue
        isp = get_typed_input("Engine ISP: ", float)
        thrust = get_typed_input("Total thrust: ", float)

        # Calculate our values if we have the data, or set them to a string if not
        try:
            delta_v = abs(trunc(calculate_delta_v(m_init, m_end, isp)))
        except TypeError:
            delta_v = "?"

        try:
            acc_init = abs(trunc(thrust / m_init))
            acc_end = abs(trunc(thrust / m_end))
            TWRs = ["TWR on {0}: {1} - {2}".format(planet,
                                                   str(round(acc_init / gravity, TWR_DEC_PLACES)),  # Min TWR
                                                   str(round(acc_end / gravity, TWR_DEC_PLACES))  # Max TWR
                                                   )
                    for (planet, gravity) in SURFACE_GRAVITIES]
        except TypeError:
            acc_end = "?"
            acc_init = "?"
            TWRs = ["TWRs: ?"]

        # Display our calculated values, and offer to repeat
        print(DELIMITER)
        print("Delta v: " + str(delta_v) + " m/s")
        print("Acceleration range: {0} - {1} m/s^2".format(str(min(acc_end, acc_init)), str(max(acc_end, acc_init))))
        print("\n".join(TWRs))
        print(DELIMITER)
        input("Enter to begin again, or Ctrl+c to close...")


def calculate_delta_v(m_init, m_end, isp):
    return log(m_init / m_end) * isp * SURFACE_GRAVITIES["Kerbin"]


def get_typed_input(prompt, type_function):
    while True:
        returned_value = input(prompt)
        if not returned_value:
            return None
        try:
            returned_value = type_function(returned_value)
        except ValueError:
            print("Invalid input")
            continue
        else:
            return returned_value


if __name__ == "__main__":
    main()