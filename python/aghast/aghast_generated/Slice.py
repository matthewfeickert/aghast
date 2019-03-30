# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class Slice(object):
    __slots__ = ['_tab']

    # Slice
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Slice
    def Start(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Slice
    def Stop(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # Slice
    def Step(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # Slice
    def HasStart(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # Slice
    def HasStop(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(21))
    # Slice
    def HasStep(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(22))

def CreateSlice(builder, start, stop, step, hasStart, hasStop, hasStep):
    builder.Prep(8, 24)
    builder.Pad(1)
    builder.PrependBool(hasStep)
    builder.PrependBool(hasStop)
    builder.PrependBool(hasStart)
    builder.PrependInt32(step)
    builder.PrependInt64(stop)
    builder.PrependInt64(start)
    return builder.Offset()
