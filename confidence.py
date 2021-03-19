import math


class ConfidenceInterval:

    @staticmethod
    def Get_sample_variance(sample: [float]) -> float:
        mean = sum(sample) / len(sample)
        sample_variance = 0
        for i in range(len(sample)):
            sample_variance += math.pow(sample[i] - mean, 2)
        return sample_variance / (len(sample) - 1)

    @staticmethod
    def Get_sample_standard_deviation(sample: [float]) -> float:
        return math.sqrt(ConfidenceInterval.Get_sample_variance(sample))

    @staticmethod
    def Get_confidence_interval(mean: float, sample_deviation: int, sample_size: int, t_value: float) -> (float, float):
        value = t_value * (sample_deviation / math.sqrt(sample_size))
        return mean - value, mean + value
