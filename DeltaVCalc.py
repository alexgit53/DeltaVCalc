""" Small script to calculate a rocket stage's delta V for Kerbal Space Program """

from math import log, trunc
from gooey import Gooey, GooeyParser

__author__ = 'Alex Morrison'

DELIMITER = "----------"
SURFACE_GRAVITIES = {"Kerbin": 9.81, "Mun": 1.63, "Minmus": 0.491, "Duna": 2.94}

@Gooey(show_success_modal=False)
def main():
    parser = GooeyParser(description="Calculate a rocket stage's delta V for KSP")
    parser.add_argument("mass_initial", help="Initial mass of the spacecraft (tonnes)", type=float)
    parser.add_argument("mass_final", help="Final mass of the spacecraft (tonnes)", type=float)
    parser.add_argument("isp", help="Specific impulse", type=float)
    parser.add_argument("--thrust", help="Total thrust of the spacecraft (kN)", type=float, default=0)
    args = parser.parse_args()

    get_and_process_stage(args.mass_initial, args.mass_final, args.isp, args.thrust)



def delta_v(m_init, m_end, isp):
    return log(m_init / m_end) * isp * 9.81


def get_and_process_stage(m_init, m_end, isp, thrust):
    d_v = delta_v(m_init, m_end, isp)
    print(f"Mass: {m_init}-{m_end}, ISP: {isp}, Thrust: {thrust}\n")
    print(f"Delta v: {d_v:.0f} m/s")

    if thrust > 0:
        acc = (thrust / m_init, thrust / m_end)
        burntime = 2 * d_v / (acc[0] + acc[-1])
        burn_time_m, burn_time_s = divmod(burntime, 60)
        twrs = {planet: (acc[0] / gravity, acc[-1] / gravity) for planet, gravity in SURFACE_GRAVITIES.items()}

        print(f"Acceleration range: {acc[0]:.1f} - {acc[-1]:.1f} m/s^2")
        print(f"Stage time: {burn_time_m:.0f}m {burn_time_s:.0f}s")
        print("TWRs (initial - final):")
        for planet, twr in twrs.items():
            print(f"\t{planet}\t{twr[0]:.2g}\t{twr[-1]:.2g}")

    print(DELIMITER)
    return


if __name__ == "__main__":
    main()
