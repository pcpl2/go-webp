# Lint as: python2, python3
# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_libwebp')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_libwebp')
    _libwebp = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_libwebp', [dirname(__file__)])
        except ImportError:
            import _libwebp
            return _libwebp
        if fp is not None:
            try:
                _mod = imp.load_module('_libwebp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _libwebp = swig_import_helper()
    del swig_import_helper
else:
    import _libwebp
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def WebPGetDecoderVersion():
    """WebPGetDecoderVersion() -> int"""
    return _libwebp.WebPGetDecoderVersion()

def WebPGetInfo(data):
    """WebPGetInfo(uint8_t data) -> (width, height)"""
    return _libwebp.WebPGetInfo(data)

def WebPDecodeRGB(data):
    """WebPDecodeRGB(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeRGB(data)

def WebPDecodeRGBA(data):
    """WebPDecodeRGBA(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeRGBA(data)

def WebPDecodeARGB(data):
    """WebPDecodeARGB(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeARGB(data)

def WebPDecodeBGR(data):
    """WebPDecodeBGR(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeBGR(data)

def WebPDecodeBGRA(data):
    """WebPDecodeBGRA(uint8_t data) -> (rgb, width, height)"""
    return _libwebp.WebPDecodeBGRA(data)

def WebPGetEncoderVersion():
    """WebPGetEncoderVersion() -> int"""
    return _libwebp.WebPGetEncoderVersion()

def wrap_WebPEncodeRGB(rgb, unused1, unused2, width, height, stride, quality_factor):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeRGB(rgb, unused1, unused2, width, height, stride, quality_factor)

def wrap_WebPEncodeBGR(rgb, unused1, unused2, width, height, stride, quality_factor):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeBGR(rgb, unused1, unused2, width, height, stride, quality_factor)

def wrap_WebPEncodeRGBA(rgb, unused1, unused2, width, height, stride, quality_factor):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeRGBA(rgb, unused1, unused2, width, height, stride, quality_factor)

def wrap_WebPEncodeBGRA(rgb, unused1, unused2, width, height, stride, quality_factor):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeBGRA(rgb, unused1, unused2, width, height, stride, quality_factor)

def wrap_WebPEncodeLosslessRGB(rgb, unused1, unused2, width, height, stride):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessRGB(rgb, unused1, unused2, width, height, stride)

def wrap_WebPEncodeLosslessBGR(rgb, unused1, unused2, width, height, stride):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessBGR(rgb, unused1, unused2, width, height, stride)

def wrap_WebPEncodeLosslessRGBA(rgb, unused1, unused2, width, height, stride):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessRGBA(rgb, unused1, unused2, width, height, stride)

def wrap_WebPEncodeLosslessBGRA(rgb, unused1, unused2, width, height, stride):
    """private, do not call directly."""
    return _libwebp.wrap_WebPEncodeLosslessBGRA(rgb, unused1, unused2, width, height, stride)

_UNUSED = 1


def WebPEncodeRGB(rgb, width, height, stride, quality_factor):
  """WebPEncodeRGB(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
  webp = wrap_WebPEncodeRGB(
      rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeRGBA(rgb, width, height, stride, quality_factor):
  """WebPEncodeRGBA(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
  webp = wrap_WebPEncodeRGBA(
      rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeBGR(rgb, width, height, stride, quality_factor):
  """WebPEncodeBGR(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
  webp = wrap_WebPEncodeBGR(
      rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeBGRA(rgb, width, height, stride, quality_factor):
  """WebPEncodeBGRA(uint8_t rgb, int width, int height, int stride, float quality_factor) -> lossy_webp"""
  webp = wrap_WebPEncodeBGRA(
      rgb, _UNUSED, _UNUSED, width, height, stride, quality_factor)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeLosslessRGB(rgb, width, height, stride):
  """WebPEncodeLosslessRGB(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
  webp = wrap_WebPEncodeLosslessRGB(rgb, _UNUSED, _UNUSED, width, height, stride)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeLosslessRGBA(rgb, width, height, stride):
  """WebPEncodeLosslessRGBA(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
  webp = wrap_WebPEncodeLosslessRGBA(rgb, _UNUSED, _UNUSED, width, height, stride)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeLosslessBGR(rgb, width, height, stride):
  """WebPEncodeLosslessBGR(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
  webp = wrap_WebPEncodeLosslessBGR(rgb, _UNUSED, _UNUSED, width, height, stride)
  if len(webp[0]) == 0:
    return None
  return webp[0]


def WebPEncodeLosslessBGRA(rgb, width, height, stride):
  """WebPEncodeLosslessBGRA(uint8_t rgb, int width, int height, int stride) -> lossless_webp"""
  webp = wrap_WebPEncodeLosslessBGRA(rgb, _UNUSED, _UNUSED, width, height, stride)
  if len(webp[0]) == 0:
    return None
  return webp[0]

# This file is compatible with both classic and new-style classes.


