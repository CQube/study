import numpy as np
from functools import reduce


class Calculator:
    '''
    1. Выполнить расчет показателей безотказности ПК при 
    постоянном включении и нормальных условиях эксплуатации:
    '''

    # Интенсивность отказов λАО и сбоев λАС аппаратных средств и ПК в целом
    # (ΛКО, ΛКС) с учетом программных средств (λПО, λПС).
    '''
    Все принимаемые параметры являются значениями из json файла.
    hwDenialRates - denial_rates in json.
    rateFactor - denial_rates_factor in json.
    beta - beta in json
    '''
    def DenialAndFailureRate(self, hwDenialRates, rateFactor, beta):
        hwFailureRates = []
        swFailureRates = []
        swDenialRates = []

        hwDenialRateResult = 0
        hwFailureRateResult = 0

        # Calculated hardware failure rates.
        for counter in range(0, len(hwDenialRates)):
            hwFailureRates.append(hwDenialRates[counter] * beta)

            hwDenialRateResult += hwDenialRates[counter]
            hwFailureRateResult += hwFailureRates[counter]

        swDenialRateResult = rateFactor * hwDenialRateResult
        swFailureRateResult = beta * swDenialRateResult

        computerDenialRate = swDenialRateResult + hwDenialRateResult
        computerFailureRate = swFailureRateResult + hwFailureRateResult
        
        return {
            "software": {
                "DenialRate": swDenialRateResult,
                "FailureRate": swFailureRateResult
            },
            "hardware": {
                "DenialRate": hwDenialRateResult,
                "FailureRate": hwFailureRateResult
            },
            "computer": {
                "DenialRate": computerDenialRate,
                "FailureRate": computerFailureRate
            }
        }


    # Средняя наработка до отказа ТАО сбоя ТАС аппаратных средств и ПК в целом
    # (ТКО, ТКС) с учетом программных средств (ТПО, ТПС).
    '''
    Принимается возвращаемое значение метода DenialAndFailureRate.
    '''
    def AverageWorkingTillFailureAndDenial(self, rates):
        return {
            "software": {
                "tillDenial": 1 / rates["software"]["DenialRate"],
                "tillFailure": 1 / rates["software"]["FailureRate"]
            },
            "hardware": {
                "tillDenial": 1 / rates["hardware"]["DenialRate"],
                "tillFailure": 1 / rates["hardware"]["FailureRate"]
            },
            "computer": {
                "tillDenial": 1 / rates["computer"]["DenialRate"],
                "tillFailure": 1 / rates["computer"]["FailureRate"]
            }
        }

    # γ – процентной наработки до отказа аппаратных taγ, программных tпγ средств и ПК tкγ;
    # taγ = (-1/ ΛAО)ln(γ /100)
    '''
    Принимается возвращаемое значение метода AverageWorkingTillFailureAndDenial.
    '''
    def PercentWorkingTillDanial(self, rates, gamma):
        softwarePercent = (-1 / rates["software"]["tillDenial"]) * np.log(gamma / 100)
        hardwarePercent = (-1 / rates["hardware"]["tillDenial"]) * np.log(gamma / 100)
        computerPercent = (-1 / rates["computer"]["tillDenial"]) * np.log(gamma / 100)
        
        return {
            "software": softwarePercent,
            "hardware": hardwarePercent,
            "computer": computerPercent
        }

    # Вероятности безотказной PАО(t) бессбойной PАС(t) работы аппаратных средств,
    # программных средств PПО(t), PПС(t) и ПК в целом PКО(t), PКС(t).
    # PAC = exp(-λAC * t)
    '''
    Возвращеюся вероятности безотказной и бессбойной работы для
    software                   Рпо(t)       Рпс(t),
    hardware                   Pсо(t)       Pас(t),
    computer                   Pко(t)       Pкс(t).
    '''
    def TroubleFreeChance(self, rates, time):
        return {
            "software": {
                "denial": np.exp(-rates["software"]["DenialRate"] * time),
                "failure": np.exp(-rates["software"]["FailureRate"] * time)
            },
            "hardware": {
                "denial": np.exp(-rates["hardware"]["DenialRate"] * time),
                "failure": np.exp(-rates["hardware"]["FailureRate"] * time)
            },
            "computer": {
                "denial": np.exp(-rates["computer"]["DenialRate"] * time),
                "failure": np.exp(-rates["computer"]["FailureRate"] * time)
            }
        }

    # Вероятности отказа QАО(t) и сбоя QАС(t) аппаратных средств, программных
    # средств QПО(t), QПС(t) и ПК в целом QКО(t), QКС(t).
    '''
    Принимается возвращаемое значение метода TroubleFreeChance.
    '''
    def DenialAndFailureChance(self, chances):
        return {
            "software": {
                "denial": 1 - chances["software"]["denial"],
                "failure": 1 - chances["software"]["failure"]
            },
            "hardware": {
                "denial": 1 - chances["hardware"]["denial"],
                "failure": 1 - chances["hardware"]["failure"]
            },
            "computer": {
                "denial": 1 - chances["computer"]["denial"],
                "failure": 1 - chances["computer"]["failure"]
            }
        }


    '''
    2. Выполнить расчет показателей безотказности ПК в экстремальных условиях
    эксплуатации (повышенной температуре, вибрации, перегрузке,
    характеризуемых коэффициентами kтем, kвиб, kпер соответственно):
    '''
    # Интенсивности отказов ΛКЭ и средней наработки до отказа ТКЭ аппаратных средств (ПК).
    '''
    Принимается возвращаемое значение метода DenialAndFailureRate.
    '''
    def DenialAndWorkingTillFailureRate(self, rates, time, factors):
        extremeConditionsHwDenialRate = reduce(lambda x, y: x * y, factors) \
                                               * (rates["hardware"]["DenialRate"]
                                               + rates["hardware"]["FailureRate"])
        averageWorkingTillDenial = 1 / extremeConditionsHwDenialRate

        return {
            "hwDenialRate": extremeConditionsHwDenialRate,
            "workingTillDenial": averageWorkingTillDenial
        }

    # Вероятности безотказной работы PКЭ(t) и отказа QКЭ(t) аппаратных средств (ПК).
    '''
    Принимается возвращаемое значение метода DenialAndWorkingTillFailureRate.
    '''
    def UptimeAndDenialCahnce(self, denialRateAndWorkingTillDenail, time):
        extremeConditionsUptimeChance \
            = np.exp( -(denialRateAndWorkingTillDenail["hwDenialRate"] * time))
        extremeConditionsDenialChance = 1 - extremeConditionsUptimeChance

        return {
            "uptimeChance": extremeConditionsUptimeChance,
            "denialChance": extremeConditionsDenialChance
        }


    '''
    3. Выполнить расчет показателей сохраняемости (при выключенном состоянии
    ПК, характеризуемом показателе коэффициента снижения интенсивности
    отказа при старении G):
    '''

    # Интенсивности отказов ΛКХ и средней наработке до отказа ТсрКХ аппаратных
    # средств (ПК) при хранении.
    # λАОХ = λАО / G
    # ТАОХ  = 1 / λАОХ
    def DenialAndAvarageWorkingToFailureRate(self, hwDenialRate, failRateDropFactor):
        denialRate = hwDenialRate / failRateDropFactor
        avarageWorkingToFailure = 1 / denialRate

        return {
            "denialRate": denialRate,
            "workingToFailureRate": avarageWorkingToFailure
        }

    # Вероятности безотказного хранения PКХ(t) и отказа при хранении QКХ(t)
    # аппаратных средств (ПК).
    # PКОХ(tх) = PАОХ(tх) = exp(-λАОХ tх) = exp(-λАО tх/G)
    # QКОХ(tх) = QАОХ(tх) = 1 - PКХ(tх)
    def SafeStorageAndDenialChance(self, hwDenialRate, storingTime, failRateDropFactor):
        safeStorageChance = np.exp((-hwDenialRate * storingTime) / failRateDropFactor)
        denialChance = 1 - safeStorageChance

        return {
            "safeStorageChance": safeStorageChance,
            "denialChance": denialChance
        }


    '''
    4. Выполнить расчет показателей безотказности при циклическом включении ПК
    (заданных периодах включенного и выключенного состояния tвклi , tвыклi или
    коэффициенте, определяющем долю времени, в течение которого ПК включен, r:
    '''

    # Интенсивности отказов аппаратных λАОЦ, программных λПОЦ средств и ПК в целом.
    # ΛКОЦ  = (1 + (G - 1) r) / G * ΛКО
    '''
    Принимается возвращаемое значение метода DenialAndFailureRate.
    '''
    def TotalDenialRate(self, rates, storingTimeFactor, failRateDropFactor):
        hwDenialRate = (1 + (failRateDropFactor - 1) * storingTimeFactor) \
                        / failRateDropFactor * rates["hardware"]["DenialRate"]
        swDenialRate = (1 + (failRateDropFactor - 1) * storingTimeFactor) \
                        / failRateDropFactor * rates["software"]["DenialRate"]
        pcDenialRate = (1 + (failRateDropFactor - 1) * storingTimeFactor) \
                        / failRateDropFactor * rates["computer"]["DenialRate"]

        return {
            "hwDenialRate": hwDenialRate,
            "swDenialRate": swDenialRate,
            "pcDenialRate": pcDenialRate
        }

    # Вероятности безотказной работы аппаратных PАОЦ(t), программных PПОЦ(t)
    # средств и ПК в целом PКОЦ(t).
 	# exp[-(1+(G-1)r) (ΛКО t)/G]
    '''
    Принимается возвращаемое значение метода DenialAndFailureRate.
    '''
    def TotalUptimeChance(self, rates, storingTime, storingTimeFactor, failRateDropFactor):
        hwUptimeChance = np.exp(-(1 + (failRateDropFactor - 1) * storingTimeFactor) \
                                * (rates["hardware"]["DenialRate"] * storingTime) / failRateDropFactor)
        swUptimeChance = np.exp(-(1 + (failRateDropFactor - 1) * storingTimeFactor) \
                                * (rates["software"]["DenialRate"] * storingTime) / failRateDropFactor)
        pcUptimeChance = np.exp(-(1 + (failRateDropFactor - 1) * storingTimeFactor) \
                                * (rates["computer"]["DenialRate"] * storingTime) / failRateDropFactor)

        return {
            "hwUptimeChance": hwUptimeChance,
            "swUptimeChance": swUptimeChance,
            "pcUptimeChance": pcUptimeChance
        }


if __name__ != "__main__":
    clc = Calculator()