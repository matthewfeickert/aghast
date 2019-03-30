# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

# ///////////////////////////////////////////////// axis
class Axis(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAxis(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Axis()
        x.Init(buf, n + offset)
        return x

    # Axis
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Axis
    def BinningType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Axis
    def Binning(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Axis
    def Expression(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Axis
    def Statistics(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Statistics import Statistics
            obj = Statistics()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Axis
    def StatisticsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Axis
    def Title(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Axis
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Axis
    def Decoration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Decoration import Decoration
            obj = Decoration()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def AxisStart(builder): builder.StartObject(7)
def AxisAddBinningType(builder, binningType): builder.PrependUint8Slot(0, binningType, 0)
def AxisAddBinning(builder, binning): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(binning), 0)
def AxisAddExpression(builder, expression): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(expression), 0)
def AxisAddStatistics(builder, statistics): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(statistics), 0)
def AxisStartStatisticsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AxisAddTitle(builder, title): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(title), 0)
def AxisAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def AxisAddDecoration(builder, decoration): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(decoration), 0)
def AxisEnd(builder): return builder.EndObject()
