def slice_to_range(item):
    if isinstance(item, slice):
      r = range(item.start if item.start is not None else 0,
               item.stop if item.stop is not None else 0,
               item.step if item.step is not None else 1)
    return r
  
