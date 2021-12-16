import functools

class Bitstream:
    def __init__(self, data):
        self.stream = bytearray.fromhex(data)
        self.byte_index = 0
        self.bit_index = 0

    def next_bit(self):
        mask = 1 << (7 - self.bit_index)
        result = 1 if self.stream[self.byte_index] & mask else 0
        self.bit_index += 1
        if self.bit_index == 8:
            self.byte_index += 1
            self.bit_index = 0
        return result

    def read_bits(self, count):
        result = 0
        for i in range(count):
            result = result * 2 + self.next_bit()
        return result

    def position(self):
        return self.byte_index * 8 + self.bit_index

class Packet:
    def __init__(self, stream):
        self.version = stream.read_bits(3)
        self.packet_type_id = stream.read_bits(3)
        self.subpackets = []
        if self.packet_type_id == 4:
            self.literal_value = self.read_literal_value(stream)
        else:
            length_type_id = stream.next_bit()
            if length_type_id:
                num_subpackets = stream.read_bits(11)
                for i in range(num_subpackets):
                    self.subpackets.append(Packet(stream))
            else:
                total_length = stream.read_bits(15)
                start_pos = stream.position()
                while stream.position() < start_pos + total_length:
                    self.subpackets.append(Packet(stream))

    def read_literal_value(self, stream):
        result = 0
        while True:
            last = stream.next_bit()
            group = stream.read_bits(4)
            result = result * 16 + group
            if not last: break
        return result

    def evaluate(self):
        if self.packet_type_id == 4:
            return self.literal_value
        subpacket_values = [s.evaluate() for s in self.subpackets]
        match self.packet_type_id:
            case 0: return sum(subpacket_values)
            case 1: return functools.reduce(lambda x, y: x*y, subpacket_values)
            case 2: return min(subpacket_values)
            case 3: return max(subpacket_values)
            case 5: return 1 if subpacket_values[0] > subpacket_values[1] else 0
            case 6: return 1 if subpacket_values[0] < subpacket_values[1] else 0
            case 7: return 1 if subpacket_values[0] == subpacket_values[1] else 0

def version_sum(packet):
    return packet.version + sum([version_sum(s) for s in packet.subpackets])

p = Packet(Bitstream(open("day16input.txt").read()))
print(version_sum(p))
print(p.evaluate())

