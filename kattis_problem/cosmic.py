import sys
import math


def calc_mean(tmps_total: int, temps_in_kelvin: list) -> int:  # type: ignore
    tmps = 0
    for _, temperatures in enumerate(temps_in_kelvin):
        tmps += temperatures
    return math.floor(tmps / tmps_total)


def get_input() -> tuple:  # type: ignore
    temp_total_in = sys.stdin.readline().strip()
    total_tmp_readings = int(temp_total_in)
    input_values = sys.stdin.readline().split()
    temp_kelvin_values = [int(value) for value in input_values]
    return total_tmp_readings, temp_kelvin_values


def main() -> None:
    total_num, temps_in_kelvin = get_input()
    mean = calc_mean(total_num, temps_in_kelvin)
    print(mean)


if __name__ == "__main__":
    main()
