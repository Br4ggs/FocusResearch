import math


class ConfidenceInterval:

    @staticmethod
    def GetSampleVariance(sample: [float]) -> float:
        mean = sum(sample) / len(sample)
        sample_variance = 0
        for i in range(len(sample)):
            sample_variance += math.pow(sample[i] - mean, 2)
        return sample_variance / (len(sample) - 1)

    @staticmethod
    def GetSampleDeviation(sample: [float]) -> float:
        return math.sqrt(ConfidenceInterval.GetSampleVariance(sample))

    @staticmethod
    def GetConfidenceInterval(mean: float, sample_deviation: int, sample_size: int, t_value: float) -> (float, float):
        value = t_value * (sample_deviation / math.sqrt(sample_size))
        return mean - value, mean + value
