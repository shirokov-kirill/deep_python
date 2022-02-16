import numbers
import numpy as np


class ToFileMixin:
    def __toFile__(self, file):
        f = open(file, 'w')
        f.write(self.__str__())


class GetSetMixin:

    def __init__(self, value):
        self._value = np.asarray(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class StrMixin:
    def __str__(self):
        result = "Your array: [\n"
        for el in self.value:
            result += '   '
            result += el.__str__()
            result += '\n'
        result += ']'
        return result


class MixinMatrix(np.lib.mixins.NDArrayOperatorsMixin, ToFileMixin, StrMixin, GetSetMixin):

    # One might also consider adding the built-in list type to this
    # list, to support operations like np.add(array_like, list)
    _HANDLED_TYPES = (np.ndarray, numbers.Number, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use ArrayLike instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES + (MixinMatrix,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x._value if isinstance(x, MixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._value if isinstance(x, MixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self._value)
