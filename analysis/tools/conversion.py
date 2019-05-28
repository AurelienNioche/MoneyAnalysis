class Converter:

    map = {
        3: {
            0: 0,
            1: 2,
            2: 1
        },
        4: {
            0: 0,
            1: 3,
            2: 2,
            3: 1
        }
    }

    inv_map = {
        3: {v: k for k, v in map[3].items()},
        4: {v: k for k, v in map[4].items()}
    }

    @classmethod
    def convert(cls, array_like, n_good):

        for i, v in enumerate(array_like):
            array_like[i] = cls.map[n_good][v]
        return array_like

    @classmethod
    def convert_value(cls, v, n_good):
        return cls.map[n_good][v]

    @classmethod
    def reverse_value(cls, v, n_good):
        return cls.inv_map[n_good][v]
