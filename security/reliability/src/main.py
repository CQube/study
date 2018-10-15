#!/bin/python3

import matplotlib.pyplot as plt
from Calculator import clc
from Config import cfg


def main():
    result1 = clc.DenialAndFailureRate(
        cfg.data["denial_rates"],
        cfg.data["denial_rate_factor"],
        cfg.data["beta"]
    )
    result2 = clc.AverageWorkingTillFailureAndDenial(
        result1
    )
    result3 = clc.PercentWorkingTillDanial(
        result2,
        cfg.data["gamma"]
    )
    result4 = clc.TroubleFreeChance(
        result1,
        cfg.data["time"]
    )
    result5 = clc.DenialAndFailureChance(
        result4
    )
    result6 = clc.DenialAndWorkingTillFailureRate(
        result1,
        cfg.data["time"],
        cfg.data["operating_condition_factors"]
    )
    result7 = clc.UptimeAndDenialCahnce(
        result6,
        cfg.data["time"],
    )
    result8 = clc.DenialAndAvarageWorkingToFailureRate(
        result1["hardware"]["DenialRate"],
        cfg.data["storing"]["fail_rate_drop_factor"],
    )
    result9 = clc.SafeStorageAndDenialChance(
        result1["hardware"]["DenialRate"],
        cfg.data["cyclic_work"]["time"],
        cfg.data["storing"]["fail_rate_drop_factor"],
    )
    result10 = clc.TotalDenialRate(
        result1,
        cfg.data["cyclic_work"]["storing_time_factor"],
        cfg.data["storing"]["fail_rate_drop_factor"],
    )
    result11 = clc.TotalUptimeChance(
        result1,
        cfg.data["storing"]["time"],
        cfg.data["cyclic_work"]["storing_time_factor"],
        cfg.data["storing"]["fail_rate_drop_factor"],
    )

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
    print(result8)
    print(result9)
    print(result10)
    print(result11)


if __name__ == "__main__":
    main()