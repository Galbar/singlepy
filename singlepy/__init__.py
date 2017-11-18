import weakref


class Singleton(type):

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._INSTANCES = {}
        cls._KEYS = {}

        if not hasattr(cls, "_make_singleton_key"):
            cls._make_singleton_key = Singleton._default_make_singleton_key

    def __call__(cls, *args, **kwargs):
        key = cls._make_singleton_key(*args, **kwargs)
        ref = cls._INSTANCES.get(key)
        if ref is None:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._INSTANCES[key] = cls._pack_ref(instance)
            cls._KEYS[id(instance)] = key
        else:
            instance = cls._unpack_ref(ref)
        return instance

    @staticmethod
    def _pack_ref(instance):
        return instance

    @staticmethod
    def _unpack_ref(ref):
        return ref

    @staticmethod
    def _default_make_singleton_key(*args, **kwargs):
        return (args, tuple(sorted(kwargs.items(), key=lambda x: x[0])))


class WeakSingleton(Singleton):

    def __init__(cls, name, bases, dict):
        super(WeakSingleton, cls).__init__(name, bases, dict)
        cls.__del__ = WeakSingleton._get_del(cls)

    @staticmethod
    def _pack_ref(instance):
        return weakref.ref(instance)

    @staticmethod
    def _unpack_ref(ref):
        return ref()

    @staticmethod
    def _get_del(cls):
        original_del = None
        if hasattr(cls, "__del__"):
            original_del = cls.__del__

        def new_del(self):
            id_ = id(self)
            key = cls._KEYS[id_]
            del cls._KEYS[id_]
            del cls._INSTANCES[key]
            if original_del is not None:
                original_del(self)

        return new_del
