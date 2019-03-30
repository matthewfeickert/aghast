# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class Modes(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsModes(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Modes()
        x.Init(buf, n + offset)
        return x

    # Modes
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Modes
    def ValuesType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Modes
    def Values(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Modes
    def Filter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .StatisticFilter import StatisticFilter
            obj = StatisticFilter()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ModesStart(builder): builder.StartObject(3)
def ModesAddValuesType(builder, valuesType): builder.PrependUint8Slot(0, valuesType, 0)
def ModesAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def ModesAddFilter(builder, filter): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(filter), 0)
def ModesEnd(builder): return builder.EndObject()
