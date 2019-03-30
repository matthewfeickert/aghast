# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

# ///////////////////////////////////////////////// functions
class Parameter(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsParameter(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Parameter()
        x.Init(buf, n + offset)
        return x

    # Parameter
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Parameter
    def Identifier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Parameter
    def ValuesType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Parameter
    def Values(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Parameter
    def ErrorsType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Parameter
    def Errors(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def ParameterStart(builder): builder.StartObject(5)
def ParameterAddIdentifier(builder, identifier): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(identifier), 0)
def ParameterAddValuesType(builder, valuesType): builder.PrependUint8Slot(1, valuesType, 0)
def ParameterAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def ParameterAddErrorsType(builder, errorsType): builder.PrependUint8Slot(3, errorsType, 0)
def ParameterAddErrors(builder, errors): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(errors), 0)
def ParameterEnd(builder): return builder.EndObject()
