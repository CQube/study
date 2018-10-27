#!/bin/python3

from Calculator import clc
from PlotCreator import plc
from Config import cfg


def main():
    result1 = clc.DenialAndFailureRate(
        cfg.data["denial_rates"],
        cfg.data["denial_rate_factor"],
        cfg.data["beta"]
    )


    '''
    1. Normal conditions
    '''
    # DenialFreeChances(result1)
    # DenialChances(result1)
    # FailureFreeChances(result1)
    # FailureChances(result1)
    # TroubleFreeChances(result1)
    # TroubleChances(result1)
    # SafeStoringChances(
    #     result1["hardware"]["DenialRate"],
    #     cfg.data["cyclic_work"]["time"],
    #     cfg.data["storing"]["fail_rate_drop_factor"],
    # )


    result6 = clc.DenialAndWorkingTillFailureRate(
        result1,
        cfg.data["time"],
        cfg.data["operating_condition_factors"]
    )

    '''
    2. Real conditions
    '''
    # RealConditionsChances(
    #     result6,
    #     cfg.data["time"],
    # )



    '''
    3. Cyclic working.
    '''
    CyclicWorkingTroubleFreeChances(
        result1,
        cfg.data["storing"]["time"],
        cfg.data["cyclic_work"]["storing_time_factor"],
        cfg.data["storing"]["fail_rate_drop_factor"],
    )
    # CyclicWorkingTroubleChances(
    #     result1,
    #     cfg.data["storing"]["time"],
    #     cfg.data["cyclic_work"]["storing_time_factor"],
    #     cfg.data["storing"]["fail_rate_drop_factor"],
    # )


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
    result7 = clc.UptimeAndDenialChance(
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


    plc.draw()


def DenialFreeChances(rates):
    DenialFreeChanceData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        DenialFreeChanceData['hardware'].append(chances["hardware"]["denial"])
        DenialFreeChanceData['software'].append(chances["software"]["denial"])
        DenialFreeChanceData['computer'].append(chances["computer"]["denial"])
        DenialFreeChanceData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(DenialFreeChanceData)


def DenialChances(rates):
    DenialChancesData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        DenialChancesData['hardware'].append(1 - (chances["hardware"]["denial"]))
        DenialChancesData['software'].append(1 - (chances["software"]["denial"]))
        DenialChancesData['computer'].append(1 - (chances["computer"]["denial"]))
        DenialChancesData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(DenialChancesData)


def FailureFreeChances(rates):
    FailureFreeChanceData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        FailureFreeChanceData['hardware'].append(chances["hardware"]["failure"])
        FailureFreeChanceData['software'].append(chances["software"]["failure"])
        FailureFreeChanceData['computer'].append(chances["computer"]["failure"])
        FailureFreeChanceData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(FailureFreeChanceData)


def FailureChances(rates):
    FailureChancesData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        FailureChancesData['hardware'].append(1 - (chances["hardware"]["failure"]))
        FailureChancesData['software'].append(1 - (chances["software"]["failure"]))
        FailureChancesData['computer'].append(1 - (chances["computer"]["failure"]))
        FailureChancesData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(FailureChancesData)


def TroubleFreeChances(rates):
    TroubleFreeChanceData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        TroubleFreeChanceData['hardware'].append(chances["hardware"]["denial"] + chances["hardware"]["failure"])
        TroubleFreeChanceData['software'].append(chances["software"]["denial"] + chances["software"]["failure"])
        TroubleFreeChanceData['computer'].append(chances["computer"]["denial"] + chances["computer"]["failure"])
        TroubleFreeChanceData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(TroubleFreeChanceData)


def TroubleChances(rates):
    TroubleChancesData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TroubleFreeChance(rates, i / 100)

        TroubleChancesData['hardware'].append(1 - (chances["hardware"]["denial"] + chances["hardware"]["failure"]))
        TroubleChancesData['software'].append(1 - (chances["software"]["denial"] + chances["software"]["failure"]))
        TroubleChancesData['computer'].append(1 - (chances["computer"]["denial"] + chances["computer"]["failure"]))
        TroubleChancesData['timepoint'].append(i / 100)

    plc.DrawProbabilityGraph(TroubleChancesData)


def SafeStoringChances(hwDenialRate, storingTime, failRateDropFactor):
    data = {
        'safe': [],
        'fail': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.SafeStorageAndDenialChance(hwDenialRate, i / 100, failRateDropFactor)

        data['safe'].append(chances["safeStorageChance"])
        data['fail'].append(chances["denialChance"])
        data['timepoint'].append(i / 100)

    plc.DrawStoringProbability(data)


def RealConditionsChances(denialRateAndWorkingTillDenail, time):
    data = {
        'uptime': [],
        'danial': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.UptimeAndDenialChance(denialRateAndWorkingTillDenail, i / 1000)

        data['uptime'].append(chances["uptimeChance"])
        data['danial'].append(chances["denialChance"])
        data['timepoint'].append(i / 1000)

    plc.DrawRealConditionsGraph(data)


def CyclicWorkingTroubleFreeChances(rates, storingTime, storingTimeFactor, failRateDropFactor):
    TroubleFreeChanceData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TotalUptimeChance(rates, i / 10, storingTimeFactor, failRateDropFactor)

        TroubleFreeChanceData['hardware'].append(chances["hwUptimeChance"])
        TroubleFreeChanceData['software'].append(chances["swUptimeChance"])
        TroubleFreeChanceData['computer'].append(chances["pcUptimeChance"])
        TroubleFreeChanceData['timepoint'].append(i / 10)

    plc.DenialFreeCycligProbability(TroubleFreeChanceData)


def CyclicWorkingTroubleChances(rates, storingTime, storingTimeFactor, failRateDropFactor):
    TroubleChancesData = {
        'hardware': [],
        'software': [],
        'computer': [],
        'timepoint': []
    }

    for i in range(1, 11):
        chances = clc.TotalUptimeChance(rates, i / 10, storingTimeFactor, failRateDropFactor)

        TroubleChancesData['hardware'].append(1 - (chances["hwUptimeChance"]))
        TroubleChancesData['software'].append(1 - (chances["swUptimeChance"]))
        TroubleChancesData['computer'].append(1 - (chances["pcUptimeChance"]))
        TroubleChancesData['timepoint'].append(i / 10)

    plc.DenialCycligProbability(TroubleChancesData)


if __name__ == "__main__":
    main()