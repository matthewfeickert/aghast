# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class RawExternalBuffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRawExternalBuffer(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RawExternalBuffer()
        x.Init(buf, n + offset)
        return x

    # RawExternalBuffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RawExternalBuffer
    def Pointer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # RawExternalBuffer
    def Numbytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # RawExternalBuffer
    def ExternalSource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # RawExternalBuffer
    def Location(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def RawExternalBufferStart(builder): builder.StartObject(4)
def RawExternalBufferAddPointer(builder, pointer): builder.PrependUint64Slot(0, pointer, 0)
def RawExternalBufferAddNumbytes(builder, numbytes): builder.PrependUint64Slot(1, numbytes, 0)
def RawExternalBufferAddExternalSource(builder, externalSource): builder.PrependUint32Slot(2, externalSource, 0)
def RawExternalBufferAddLocation(builder, location): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(location), 0)
def RawExternalBufferEnd(builder): return builder.EndObject()
