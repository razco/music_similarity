'''
Created on Aug 31, 2017
@author: Raz
'''


DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DIAGONAL = range(3)


class PartialSimilarPath(object):
    def __init__(self, direction, is_success, prev_similar_path=None):
        # ep is an abbreviation for "previous error":
        # the error prior to the last success
        self._ep = 0 if prev_similar_path is None else prev_similar_path.ep
        # lp is an abbreviation for "previous length":
        # the path length prior to the last success
        self._lp = 0 if prev_similar_path is None else prev_similar_path.lp
        # el is an abbreviation for "left error":
        # the left error after the last success
        self._el = 0 if prev_similar_path is None else prev_similar_path.el
        # eu is an abbreviation for "up error":
        # the up error after the last success
        self._eu = 0 if prev_similar_path is None else prev_similar_path.eu
        # 1 - num_errors/path_length. Current path score
        self._score = (
            0 if prev_similar_path is None else prev_similar_path.score)

        if prev_similar_path is not None:
            self.__set_new_params(is_success, direction)

    @classmethod
    def empty_instance(cls):
        return cls(None, None, None)

    def __set_new_params(self, is_success, direction=DIRECTION_DIAGONAL):
        if not is_success:
            if direction == DIRECTION_LEFT:
                self._el += 1
            elif direction == DIRECTION_UP:
                self._eu += 1
            else:
                assert False  # other directions are not available on failure
            max_curr_error = max(self._el, self._eu)
        elif is_success:
            if direction == DIRECTION_DIAGONAL:
                max_curr_error = max(self._el, self._eu)
                self._ep += max_curr_error
                self._lp += max_curr_error + 1
                self._el = 0
                self._eu = 0
                max_curr_error = 0
            else:
                assert False  # other directions are not available on success
        else:
            assert False  # it's either success or failure!
        self._score = (
            1 - (max_curr_error + self._ep)/(max_curr_error + self._lp))

    @property
    def score(self):
        return self._score

    @property
    def lp(self):
        return self._lp
